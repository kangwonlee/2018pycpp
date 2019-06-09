# ref : Francesco Mosconi, Travis + Anaconda + Jupyter, https://github.com/ghego/travis_anaconda_jupyter

import os
import subprocess
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import check_links_in_ipynb as cli
import get_cpp_from_ipynb as gcpp


def check_kernel_spec():
    """
    Present Jupyter kernel spec
    """

    # https://jupyter-client.readthedocs.io/en/latest/api/kernelspec.html
    import jupyter_client.kernelspec as jk

    kernel_spec_manager = jk.KernelSpecManager()

    print(kernel_spec_manager.get_all_specs())


def _exec_notebook(path):
    """
    Run the ipynb file of path

    Raise exception if any error
    """
    # http://nbconvert.readthedocs.io/en/latest/execute_api.html
    # ijstokes et al, Command line execution of a jupyter notebook fails in default Anaconda 4.1, https://github.com/Anaconda-Platform/nb_conda_kernels/issues/34
    # obtain a temporary filename
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        # prepare a command running .ipynb file while converting
        args = [
            "jupyter", # name of program
           "nbconvert", # option
           "--to", "notebook", # conver to another ipynb file
           "--execute", # run while convering
           "--ExecutePreprocessor.timeout=1000",
           "--ExecutePreprocessor.kernel_name=python",
           "--output", fout.name, # output file name
           path    # input file name
        ]
        # run the command above
        # and raise if error
        subprocess.check_call(args)


def get_ipynb_file_list(base_path):
        # Prepare a list of ipynb files of the base_path
        ipynb_file_list = []
        for name in os.listdir(base_path):
                pardir_item_full_path = os.path.join(base_path, name)
                assert isinstance(pardir_item_full_path, str)
                assert os.path.exists(pardir_item_full_path)
                if os.path.isdir(pardir_item_full_path):
                        for subfolder_name in os.listdir(pardir_item_full_path):
                                subfolder_item_name = os.path.join(pardir_item_full_path, subfolder_name)
                                assert isinstance(subfolder_item_name, str)
                                assert os.path.exists(subfolder_item_name)
                                if subfolder_name.endswith('.ipynb') and os.path.isfile(subfolder_item_name):
                                        ipynb_file_list.append(os.path.join(pardir_item_full_path, subfolder_name))

        assert ipynb_file_list

        return ipynb_file_list


def get_base_path():
        # Find absolute path of the parent folder
        # This file assumes the parent folder contains a number of .ipynb files
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

        assert os.path.exists(base_path)
        assert os.path.isdir(base_path)

        return base_path


base_path = get_base_path()
ipynb_file_list = get_ipynb_file_list(base_path)


# https://docs.pytest.org/en/latest/example/parametrize.html
@pytest.mark.parametrize("filename", ipynb_file_list)
def test_execute_ipynb(filename):
    print('execute_ipynb() : %s %s' % (base_path, filename))
    # run .ipynb file
    _exec_notebook(os.path.join(base_path, filename))


# https://docs.pytest.org/en/latest/example/parametrize.html
@pytest.mark.parametrize("filename", ipynb_file_list)
def test_cpp_in_ipynb(filename):
    print('test_cpp_in_ipynb() : %s %s' % (base_path, filename))
    # separate .cpp code blocks from the ipynb file,
    # build, and run
    assert gcpp.get_cpp_src_from_ipynb(os.path.join(base_path, filename))


@pytest.mark.parametrize("filename", ipynb_file_list)
def test_urls_in_ipynb(filename):
    cli.check_links_in_ipynb(filename)
