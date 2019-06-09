![master](https://travis-ci.org/kangwonlee/2018pycpp.svg?branch=master)

# Python and C/C++ Tutorial : A Comparative Approach

## Overview

* Audiences : Starting graduate students

* Programming language : Python and C/C++

* Operating system : Linux


## Contents

| Ch  | Sec | Subject                           | Linux | Python | C++ |
|:---:|:---:|:----------------------------------:|:-----:|:------:|:---:|
|  [0](00/)  |  [0](00/00.ipynb)  | Overview<br>Introducing Linux bash |   ✓   |        |     |
|     |  [1](00/01.ipynb)  | Introducing Python<br>Installing [Anaconda](https://www.anaconda.com/download/) <br>`print('Hello World!')`<br>`python hello.py` |       |   ✓    |     |
|     |  [2](00/02.ipynb)  | Introducing C/C++<br>Installing `g++` and `make`<br>`printf("Hello World!\n");` / `cout << "Hello World\n";`<br>`g++ -Wall hello.cpp -o hello && ./hello` |       |        |  ✓  |
|  [1](01/)  |  [0](01/00.ipynb)  | Introducing [git](https://git-scm.com/)<br>`git clone`, `git config --list`, `git status`, `git log`, `git add -p`, `git commit -m '<message>'`, `git push -u <remote> <branch>`<br>[github](https://www.github.com), and [travis-ci](https://www.travis-ci.org) |   ✓   |        |     |
|     |  [1](01/01.ipynb)  | Representing Data types <br> integers and 2's complements <br> floating point and complex numbers <br> characters and strings<br>`list` and `tuple` vs array<br>`dict` vs `struct` and `union` |       |   ✓    |  ✓  |
|     |  [2](01/02.ipynb)  | Operating<br>`+` `-` `*` `/`, `%`, {`++`, `--`}, (`//`, `**`)<br>`+=` and `*=` vs assembly<br>`<<`, `>>`, `\|`, `&` |       |   ✓    |  ✓  |
|  [2](02/)  |  [0](02/00.ipynb)  | *Control*ling flow : conditional<br>`if`-`else if`-`else`<br>`switch`-`case` |       |   ✓    |  ✓  |
|     |  [1](02/01.ipynb)  | *Control*ling flow : repetition<br>`for`<br>`while`<br>`do while` |       |   ✓    |  ✓  |
|     |  [2](02/02.ipynb)  | Wrapping into Functions and calling by value      |       |   ✓    |  ✓  |
|  [3](03/)  |  [0](03/00.ipynb)  | Interpreting Pointers and *Call*ing *by Reference* |       |        |  ✓  |
|     |  [1](03/01.ipynb)  | Managing memory with `malloc` and `free` |       |        |  ✓  |
|     |  [2](03/02.ipynb)  | Opening the hood of python : `list` of `list`s and references |       |   ✓    |     |
|  [4](04/)  |  [0](04/00.ipynb)  | Modularizing and `namespace`s |       |   ✓    |  ✓  |
|     |  [1](04/01.ipynb)  | Instantiating and inheriting `class`es |       |   ✓    |  ✓  |
|     |  [2](04/02.ipynb)  | Controlling access to Attributes |       |   ✓    |  ✓  |
|  [5](05/)  |  [0](05/00.ipynb)  | [SciPy Stack](https://www.scipy.org/) : [`numpy`](http://www.numpy.org/), [`matplotlib`](https://matplotlib.org/gallery/index.html) |       |   ✓    |     |
|     |  [1](05/01.ipynb)  | SciPy Stack : [`scipy`](https://docs.scipy.org/doc/scipy/reference/tutorial/io.html), [`sympy`](https://docs.sympy.org/latest/modules/printing.html#module-sympy.printing.ccode) |       |   ✓    |     |
|     |  [2](05/02.ipynb)  | Bridging between Python & C/C++ : [`cython`](https://cython.org) |       |   ✓    |  ✓  |
