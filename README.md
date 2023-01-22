[![CI](https://github.com/kangwonlee/2018pycpp/actions/workflows/conda_env_test.yml/badge.svg)](https://github.com/kangwonlee/2018pycpp/actions/workflows/conda_env_test.yml)

# Python and C/C++ Tutorial : A Comparative Approach

## Overview

* Audiences : Starting graduate students

* Programming language : Python and C/C++

* Operating system : Linux


## Contents

| Ch  | Sec | Subject                           | Linux | Python | C++ |
|:---:|:---:|:----------------------------------:|:-----:|:------:|:---:|
|  [0](00.python-c-cpp/)  |  [0](00.python-c-cpp/00.python.ipynb)  | Overview<br>Introducing Linux bash |   ✓   |        |     |
|     |  [1](00.python-c-cpp/10.c-cpp.ipynb)  | Introducing Python<br>Installing [Anaconda](https://www.anaconda.com/download/) <br>`print('Hello World!')`<br>`python hello.py` |       |   ✓    |     |
|     |  [2](00.python-c-cpp/20.bash.ipynb)  | Introducing C/C++<br>Installing `g++` and `make`<br>`printf("Hello World!\n");` / `cout << "Hello World\n";`<br>`g++ -Wall hello.cpp -o hello && ./hello` |       |        |  ✓  |
|  [1](10.data-types-and-operators/)  |  [0](10.data-types-and-operators/00.git.ipynb)  | Introducing [git](https://git-scm.com/)<br>`git clone`, `git config --list`, `git status`, `git log`, `git add -p`, `git commit -m '<message>'`, `git push -u <remote> <branch>`<br>[github](https://www.github.com), and [travis-ci](https://www.travis-ci.org) |   ✓   |        |     |
|     |  [1](10.data-types-and-operators/10.types.ipynb)  | Representing Data types <br> integers and 2's complements <br> floating point and complex numbers <br> characters and strings<br>`list` and `tuple` vs array<br>`dict` vs `struct` and `union` |       |   ✓    |  ✓  |
|     |  [2](10.data-types-and-operators/20.operators.ipynb)  | Operating<br>`+` `-` `*` `/`, `%`, {`++`, `--`}, (`//`, `**`)<br>`+=` and `*=` vs assembly<br>`<<`, `>>`, `\|`, `&` |       |   ✓    |  ✓  |
|  [2](20.control-flow/)  |  [0](20.control-flow/00.if.ipynb)  | *Control*ling flow : conditional<br>`if`-`else if`-`else`<br>`switch`-`case` |       |   ✓    |  ✓  |
|     |  [1](20.control-flow/10.for-while.ipynb)  | *Control*ling flow : repetition<br>`for`<br>`while`<br>`do while` |       |   ✓    |  ✓  |
|     |  [2](20.control-flow/20.functions.ipynb)  | Wrapping into Functions and calling by value      |       |   ✓    |  ✓  |
|  [3](30.pointers-and-memory-management/)  |  [0](30.pointers-and-memory-management/00.pointers.ipynb)  | Interpreting Pointers and *Call*ing *by Reference* |       |        |  ✓  |
|     |  [1](30.pointers-and-memory-management/10.calloc-free.ipynb)  | Managing memory with `malloc` and `free` |       |        |  ✓  |
|     |  [2](30.pointers-and-memory-management/20.python.list-reference.ipynb)  | Opening the hood of python : `list` of `list`s and references |       |   ✓    |     |
|  [4](40.object-oriented-programming/)  |  [0](40.object-oriented-programming/00.module-namespace.ipynb)  | Modularizing and `namespace`s |       |   ✓    |  ✓  |
|     |  [1](40.object-oriented-programming/10.class.ipynb)  | Instantiating and inheriting `class`es |       |   ✓    |  ✓  |
|     |  [2](40.object-oriented-programming/20.private-protected-public.ipynb)  | Controlling access to Attributes |       |   ✓    |  ✓  |
|     |  [3](40.object-oriented-programming/30.state-space-in-class.ipynb)  | State space representation in class |       |   ✓    |     |
|     |  [4](40.object-oriented-programming/40.dataclasses.dataclass.ipynb)  | Dataclass |       |   ✓    |     |
|  [5](05/)  |  [0](05/00.ipynb)  | [SciPy Stack](https://www.scipy.org/) : [`numpy`](http://www.numpy.org/), [`matplotlib`](https://matplotlib.org/gallery/index.html) |       |   ✓    |     |
|     |  [1](05/01.ipynb)  | SciPy Stack : [`scipy`](https://docs.scipy.org/doc/scipy/reference/tutorial/io.html), [`sympy`](https://docs.sympy.org/latest/modules/printing.html#module-sympy.printing.ccode) |       |   ✓    |     |
|     |  [2](05/02.ipynb)  | Bridging between Python & C/C++ : [`cython`](https://cython.org) |       |   ✓    |  ✓  |
