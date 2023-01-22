"""
Test that all links in README.md are valid.
"""

import pathlib
import re
import urllib.parse as up

from typing import Tuple

import pytest
import requests


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


@pytest.fixture(scope="session")
def links_in_readme_md(readme_md: str) -> Tuple[Tuple[str]]:
    return tuple(re.findall(r"\[(.*?)\]\((.*?)\)", readme_md))


@pytest.fixture(scope="session")
def ipynb_links_in_readme_md(links_in_readme_md: Tuple[Tuple[str]]) -> Tuple[Tuple[str]]:
    return tuple(
        filter(
            lambda x: x[1].endswith(".ipynb"),
            links_in_readme_md,
        )
    )


@pytest.fixture(scope="session")
def ipynb_full_links_in_readme_md(ipynb_links_in_readme_md: Tuple[Tuple[str]]) -> Tuple[Tuple[str]]:
    def get_full_url(x: Tuple[str]) -> str:
        return up.urlunparse((
            "https", "github.com", f"/kangwonlee/2018pycpp/tree/main/{x[1]}", None, None, None,
        ))

    result = []

    for info in ipynb_links_in_readme_md:
        assert 2 == len(info)
        path = info[1]
        full_link = get_full_url(info)
        result.append(full_link)

    return tuple(result)


def test_test_file_path(test_file_path: pathlib.Path):
    assert test_file_path.exists()
    assert test_file_path.is_file()


def test_test_folder(test_folder, test_file_path: pathlib.Path):
    assert test_folder.exists()
    assert test_folder.is_dir()

    assert (test_folder / test_file_path.name).exists()
    assert (test_folder / test_file_path.name) == test_file_path


def test_number_of_links_in_readme_md(links_in_readme_md: Tuple[str]):
    assert 5 < len(links_in_readme_md)


def test_number_of_links_in_ipynb_readme_md(ipynb_links_in_readme_md: Tuple[str]):
    assert 5 < len(ipynb_links_in_readme_md)
    assert all(map(lambda x: x[1].endswith(".ipynb"), ipynb_links_in_readme_md))


def test_ipynb_full_links_in_readme_md(ipynb_full_links_in_readme_md: Tuple[str]):
    assert 5 < len(ipynb_full_links_in_readme_md)
    for url in ipynb_full_links_in_readme_md:
        r = requests.get(url)
        assert r.ok, url


if "__main__" == __name__:
    pytest.main()
