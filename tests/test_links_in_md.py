"""
Test that all links in README.md are valid.
"""
import os
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
def server() -> str:
    return os.environ["GITHUB_SERVER_URL"]


@pytest.fixture(scope="session")
def repository() -> str:
    return os.environ["GITHUB_REPOSITORY"]


@pytest.fixture(scope="session")
def branch() -> str:
    return os.environ["GITHUB_REF"]


def get_full_url(path_in_repo:str, repository_name:str, branch_name:str) -> str:
    return up.urlunparse((
        "https", "github.com", f"/{repository_name}/tree/{branch_name}/{path_in_repo}", None, None, None,
    ))


@pytest.fixture(scope="session")
def full_links_in_readme_md(links_in_readme_md: Tuple[Tuple[str]], repository, branch) -> Tuple[str]:

    result = []

    for info in links_in_readme_md:
        assert 2 == len(info)
        url = info[1]

        parsed = up.urlparse(url)

        if parsed.scheme and parsed.netloc:
            full_link = url
        else:
            full_link = get_full_url(url, repository, branch)

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


def test_number_of_links_in_readme_md(links_in_readme_md: Tuple[Tuple[str]]):
    assert isinstance(links_in_readme_md, (tuple, list))
    assert isinstance(links_in_readme_md[0], (tuple, list))

    assert isinstance(links_in_readme_md[0][0], str)
    assert isinstance(links_in_readme_md[0][1], str)

    assert 5 < len(links_in_readme_md)


@pytest.mark.skipif("GITHUB_SERVER_URL" not in os.environ, reason="Not in GitHub Actions")
def test_fixture_full_links_in_readme_md(full_links_in_readme_md: Tuple[str]):
    assert isinstance(full_links_in_readme_md, (tuple, list, set))
    assert isinstance(full_links_in_readme_md[0], str)

    assert 5 < len(full_links_in_readme_md)

    assert ("https://cython.org" in full_links_in_readme_md), (
        full_links_in_readme_md
    )


@pytest.mark.skipif("GITHUB_SERVER_URL" not in os.environ, reason="Not in GitHub Actions")
def test_full_links_in_readme_md(full_links_in_readme_md: Tuple[str]):
    for url in full_links_in_readme_md:

        assert isinstance(url, str)
        assert url.startswith("http")

        r = requests.get(url)
        assert r.ok, url


if "__main__" == __name__:
    pytest.main([__file__])
