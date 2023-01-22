"""
Test that all links in README.md are valid.
"""
import pathlib


import pytest


@pytest.fixture(scope="session")
def test_folder() -> pathlib.Path:
    return pathlib.Path(__file__).parent.absolute()


@pytest.fixture(scope="session")
def test_file_path() -> pathlib.Path:
    return pathlib.Path(__file__).absolute()


@pytest.fixture(scope="session")
def proj_folder(test_folder:pathlib.Path) -> pathlib.Path:
    return test_folder.parent.absolute()


@pytest.fixture(scope="session")
def readme_md_path(proj_folder: pathlib.Path) -> str:
    return (proj_folder / "README.md")


@pytest.fixture(scope="session")
def readme_md(readme_md_path: pathlib.Path) -> str:
    with readme_md_path.open(encoding="utf-8") as f:
        txt = f.read()
    return txt


def test_test_file_path(test_file_path: pathlib.Path):
    assert test_file_path.exists()
    assert test_file_path.is_file()


def test_test_folder(test_folder, test_file_path: pathlib.Path):
    assert test_folder.exists()
    assert test_folder.is_dir()

    assert (test_folder / test_file_path.name).exists()
    assert (test_folder / test_file_path.name) == test_file_path


if "__main__" == __name__:
    pytest.main()
