import os
import nbformat
import sys
import re


def has_gpp():
    """
    Check if this system has g++ compiler
    """
    result = os.system('bash which g++')
    print(f"has_gpp() result = {result}")
    return not (result)


def get_cpp_src_from_ipynb(path):
    with open(path, encoding='utf-8') as ipynb:
        nb = nbformat.read(ipynb, nbformat.NO_CONVERT)

    # choose markdown cells only
    markdown_cells = filter(
        lambda cell: 'markdown' == cell['cell_type'],
        nb['cells']
    )

    # markdown cells with source code
    markdown_code_cells = []
    for cell in markdown_cells:
        src = cell['source'].strip()
        if (src.startswith('```') 
            and src.endswith('```')):
            markdown_code_cells.append(cell)

    for cell in markdown_code_cells:
        print(cell['source'])


def main(arg):
    get_cpp_src_from_ipynb(arg[0])


if "__main__" == __name__:
    main(sys.argv[1:])
