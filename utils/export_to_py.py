'''
Utility to export a Python script from a Jupyter notebook.
Convert one ipynb or all recursively.
'''

import argparse
import multiprocessing as mp
import pathlib
import subprocess
import sys

from typing import List


import nbformat
import nbconvert


def parse_argv(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Export Jupyter notebooks to Python scripts.')
    parser.add_argument('notebook', type=str, nargs='*', help='Path to the notebook(s) to convert.')
    parser.add_argument('--destination', type=pathlib.Path, default=get_proj_folder() / 'temp', help='Destination directory for the converted scripts.')
    parser.add_argument('--recursive', action='store_true', help='Recursively convert all notebooks in subdirectories.')
    return parser.parse_args(argv[1:])


def get_proj_folder() -> pathlib.Path:
    """Get the project root folder."""
    return pathlib.Path(__file__).parent.parent.resolve()


def main(argv:List[str]):
    args = parse_argv(argv)
    notebooks = args.notebook

    # get list of notebooks if not specified
    if not notebooks:
        notebooks = [
            path for path in get_proj_folder().rglob('*.ipynb')
        ] if args.recursive else [
            path for path in get_proj_folder().glob('*.ipynb')
        ]

    # exclude notebooks in the utils and tests folders
    notebooks = [
        notebook for notebook in notebooks
        if (
            ('utils' not in notebook.parts)
        and
            ('tests' not in notebook.parts)
        )
    ]

    converter = nbconvert.PythonExporter()

    print(f'Using {mp.cpu_count()} processes for conversion.')
    pool = mp.Pool(mp.cpu_count())
    results = pool.starmap(
        convert,
        zip(
            notebooks,
            [args.destination]*len(notebooks),
            [converter]*len(notebooks),
        )
    )
    pool.close()
    pool.join()

    print(f'Converted {len(results) - results.count(None)} / {len(results)} notebooks to Python scripts.')


def convert(notebook:pathlib.Path, destination:pathlib.Path, converter:nbconvert.Exporter) -> subprocess.CompletedProcess:
    """Convert a single notebook to a Python script."""
    if not notebook.is_file() or not notebook.suffix == '.ipynb':
        print(f'Skipping non-notebook file: {notebook.relative_to(get_proj_folder())}')
        result = None
    else:
        nb = nbformat.read(notebook, as_version=nbformat.NO_CONVERT)
        try:
            nbformat.validate(nb)
        except nbformat.ValidationError as e:
            print(f'Skipping invalid notebook: {notebook.relative_to(get_proj_folder())}')
            result = None
        else:
            script_path = destination / ((notebook.relative_to(get_proj_folder())).with_suffix('.py'))
            script_path.parent.mkdir(exist_ok=True)
            print(f'Converting {notebook.relative_to(get_proj_folder())} to {script_path.relative_to(get_proj_folder())}')
            output, resources_dict = nbconvert.export(converter, nb, output=script_path)
            script_path.write_text(output, encoding='utf-8')
            result = output
    return result


if "__main__" == __name__:
    # Run the main function with command line arguments
    main(sys.argv)
