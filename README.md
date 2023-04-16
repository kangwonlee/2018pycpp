[![CI](https://github.com/kangwonlee/2018pycpp/actions/workflows/conda_env_test.yml/badge.svg)](https://github.com/kangwonlee/2018pycpp/actions/workflows/conda_env_test.yml)

# Python and C/C++ Tutorial : A Comparative Approach

## Overview

* Audiences : Starting graduate students

* Programming language : Python and C/C++

* Operating system : Linux


## Contents

| Ch  | Sec | Subject                           | Linux | Python | C++ |
|:---:|:---:|:----------------------------------:|:-----:|:------:|:---:|
|  [00](00.python-c-cpp/)  |  [00](00.python-c-cpp/00.python.ipynb)  | Overview<br>Introducing Linux bash |   ✓   |        |     |
|     |  [10](00.python-c-cpp/10.c-cpp.ipynb)  | Introducing Python<br>Installing [Anaconda](https://www.anaconda.com/download/) <br>`print('Hello World!')`<br>`python hello.py` |       |   ✓    |     |
|     |  [20](00.python-c-cpp/20.bash.ipynb)  | Introducing C/C++<br>Installing `g++` and `make`<br>`printf("Hello World!\n");` / `cout << "Hello World\n";`<br>`g++ -Wall hello.cpp -o hello && ./hello` |       |        |  ✓  |
|  [10](10.data-types-and-operators/)  |  [00](10.data-types-and-operators/00.git.ipynb)  | Introducing [git](https://git-scm.com/)<br>`git clone`, `git config --list`, `git status`, `git log`, `git add -p`, `git commit -m '<message>'`, `git push -u <remote> <branch>`<br>[github](https://www.github.com), and [travis-ci](https://www.travis-ci.org) |   ✓   |        |     |
|     |  [10](10.data-types-and-operators/10.types.ipynb)  | Representing Data types <br> integers and 2's complements <br> floating point and complex numbers <br> characters and strings<br>`list` and `tuple` vs array<br>`dict` vs `struct` and `union` |       |   ✓    |  ✓  |
|     |  [20](10.data-types-and-operators/20.operators.ipynb)  | Operating<br>`+` `-` `*` `/`, `%`, {`++`, `--`}, (`//`, `**`)<br>`+=` and `*=` vs assembly<br>`<<`, `>>`, `\|`, `&` |       |   ✓    |  ✓  |
|  [20](20.control-flow/)  |  [00](20.control-flow/00.if.ipynb)  | *Control*ling flow : conditional<br>`if`-`else if`-`else`<br>`switch`-`case` |       |   ✓    |  ✓  |
|     |  [10](20.control-flow/10.for-while.ipynb)  | *Control*ling flow : repetition<br>`for`<br>`while`<br>`do while` |       |   ✓    |  ✓  |
|     |  [20](20.control-flow/20.functions.ipynb)  | Wrapping into Functions and calling by value      |       |   ✓    |  ✓  |
|  [30](30.pointers-and-memory-management/)  |  [00](30.pointers-and-memory-management/00.pointers.ipynb)  | Interpreting Pointers and *Call*ing *by Reference* |       |        |  ✓  |
|     |  [10](30.pointers-and-memory-management/10.calloc-free.ipynb)  | Managing memory with `malloc` and `free` |       |        |  ✓  |
|     |  [20](30.pointers-and-memory-management/20.python.list-reference.ipynb)  | Opening the hood of python : `list` of `list`s and references |       |   ✓    |     |
|  [40](40.object-oriented-programming/)  |  [00](40.object-oriented-programming/00.module-namespace.ipynb)  | Modularizing and `namespace`s |       |   ✓    |  ✓  |
|     |  [10](40.object-oriented-programming/10.class.ipynb)  | Instantiating and inheriting `class`es |       |   ✓    |  ✓  |
|     |  [20](40.object-oriented-programming/20.private-protected-public.ipynb)  | Controlling access to Attributes |       |   ✓    |  ✓  |
|     |  [30](40.object-oriented-programming/30.state-space-in-class.ipynb)  | State space representation in class |       |   ✓    |     |
|     |  [40](40.object-oriented-programming/40.dataclasses.dataclass.ipynb)  | Dataclass |       |   ✓    |     |
|  [50](50.under-the-hood/)  |  [00](50.under-the-hood/00.gdb.ipynb)  | `gdb` debugger |       |        |  ✓   |
|     |  [10](50.under-the-hood/10.cython.ipynb)  | Bridging between Python & C/C++ : [`cython`](https://cython.org) |       |   ✓    |  ✓  |
|     |  [20](50.under-the-hood/20.assembly.md)  | Programming in lower level |       |        |  ✓   |
|     |  [22](50.under-the-hood/22.working_with_bits_operators.ipynb)  | Working with bits : operators |       |        |  ✓   |
|     |  [24](50.under-the-hood/24.working_with_bits_operators_results.md)  | Results from "Working with bits" |       |        |  ✓   |
|     |  [28](50.under-the-hood/28.working_with_bits_struct_union.ipynb)  | Working with bits : `struct` and `union` |       |        |  ✓   |
