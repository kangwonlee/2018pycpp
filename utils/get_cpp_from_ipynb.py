import os
import nbformat
import sys
import re
import tempfile


def has_gpp():
    """
    Check if this system has g++ compiler
    """
    result = os.system('bash which g++')
    print(f"has_gpp() result = {result}")
    return not (result)


def get_cpp_src_from_ipynb(path):
    """
    Get cpp source code from markdown cells of the ipynb file

    To test C++ source codes of the documents

    + Choose markdown cells
    + Choose C++ source code cells
    + Save to a temporary file and try to build
    """
    with open(path, encoding='utf-8') as ipynb:
        nb = nbformat.read(ipynb, nbformat.NO_CONVERT)

    # choose markdown cells only
    markdown_cells = filter(
        lambda cell: 'markdown' == cell['cell_type'],
        nb['cells']
    )

    # markdown cells with C++ source code
    markdown_code_cells = []
    for cell in markdown_cells:
        src = cell['source'].strip()
        if (src.startswith('```') 
            and src.endswith('```')):
            if "c++" in src.splitlines()[0].lower():
                markdown_code_cells.append(cell)

    result_list = []

    # save the C++ source code and try to build it
    for cell in markdown_code_cells:
        txt = cell['source'].replace('```', '// ```')
        # obtain temporary file name
        with tempfile.NamedTemporaryFile(suffix=".cpp", mode='wt') as cpp_file:
            cpp_file_name = cpp_file.name

        # open the temporary file and write to it
        with open(cpp_file_name, 'wt') as cpp_file:
            cpp_file.write(txt)

        # try to build the code
        compile_command = f"g++ -Wall -g {cpp_file_name}"
        compile_result = os.system(compile_command)
        result_list.append(compile_result)

        if os.path.exists(cpp_file_name):
            os.remove(cpp_file_name)

    return not(any(result_list))


def main(arg):
    get_cpp_src_from_ipynb(arg[0])


if "__main__" == __name__:
    if 2 < len(sys.argv):
        main(sys.argv[1:])
    else:
        main(
            [os.path.abspath(
                os.path.join(
                    os.path.split(os.path.abspath(__file__))[0], os.pardir, '01', '01.ipynb'
                )
            )]
        )
