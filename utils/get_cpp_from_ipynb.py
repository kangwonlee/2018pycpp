import os
import nbformat
import sys


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
    for cell in nb['cells']:
        if 'markdown' == cell['cell_type']:
            print(cell['source'])


def main(arg):
    get_cpp_src_from_ipynb(arg[0])


if "__main__" == __name__:
    main(sys.argv[1:])
