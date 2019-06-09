# Python and C/C++ Tutorial : A Comparative Approach

## Overview

* Audiences : Starting graduate students

* Programming language : Python and C/C++

* Operating system : Linux


## Contents

| Ch  | Sec | Subject                           | Linux | Python | C++ |
|:---:|:---:|:----------------------------------:|:-----:|:------:|:---:|
|  0  |  0  | Overview<br>Introducing Linux bash |   ✓   |        |     |
|     |  1  | Introducing Python<br>Installing [Anaconda](https://www.anaconda.com/download/) <br>`print('Hello World!')`<br>`python hello.py` |       |   ✓    |     |
|     |  2  | Introducing C/C++<br>Installing `g++` and `make`<br>`printf("Hello World!\n");` / `cout << "Hello World\n";`<br>`g++ -Wall hello.cpp -o hello && ./hello` |       |        |  ✓  |
|  1  |  0  | Introducing [git](https://git-scm.com/)<br>`git clone`, `git config --list`, `git status`, `git log`, `git add -p`, `git commit -m '<message>'`, `git push -u <remote> <branch>`<br>[github](https://www.github.com), and [travis-ci](https://www.travis-ci.org) |   ✓   |        |     |
|     |  1  | Representing Data types <br> integers and 2's complements <br> floating point and complex numbers <br> characters and strings<br>`list` and `tuple` vs array<br>`dict` vs `struct` and `union` |       |   ✓    |  ✓  |
|     |  2  | Operating<br>`+` `-` `*` `/`, `%`, {`++`, `--`}, (`//`, `**`)<br>`+=` and `*=` vs assembly<br>`<<`, `>>`, `\|`, `&` |       |   ✓    |  ✓  |
|  2  |  0  | *Control*ling flow : conditional<br>`if`-`else if`-`else`<br>`switch`-`case` |       |   ✓    |  ✓  |
|     |  1  | *Control*ling flow : repetition<br>`for`<br>`while`<br>`do while` |       |   ✓    |  ✓  |
|     |  2  | Wrapping into Functions and calling by value      |       |   ✓    |  ✓  |
|  3  |  0  | Interpreting Pointers and *Call*ing *by Reference* |       |        |  ✓  |
|     |  1  | Managing memory with `malloc` and `free` |       |        |  ✓  |
|     |  2  | Opening the hood of python : `list` of `list`s and references |       |   ✓    |     |
|  4  |  0  | Modularizing and `namespace`s |       |   ✓    |  ✓  |
|     |  1  | Instantiating and inheriting `class`es |       |   ✓    |  ✓  |
|     |  2  | Controlling access to Attributes |       |   ✓    |  ✓  |
|  5  |  0  | [SciPy Stack](https://www.scipy.org/) : [`numpy`](http://www.numpy.org/), [`matplotlib`](https://matplotlib.org/gallery/index.html) |       |   ✓    |     |
|     |  1  | SciPy Stack : [`scipy`](https://docs.scipy.org/doc/scipy/reference/tutorial/io.html), [`sympy`](https://docs.sympy.org/latest/modules/printing.html#module-sympy.printing.ccode) |       |   ✓    |     |
|     |  2  | Bridging between Python & C/C++ : [`cython`](https://cython.org) |       |   ✓    |  ✓  |

## Builds
| subtree | status |
|:----:|:----:|
| 00 | ![00 master](https://travis-ci.org/kangwonlee/18pycpp-00.svg?branch=master) |
| 01 | ![01 master](https://travis-ci.org/kangwonlee/18pycpp-01.svg?branch=master) |
| 02 | ![02 master](https://travis-ci.org/kangwonlee/18pycpp-02.svg?branch=master) |
| 03 | ![03 master](https://travis-ci.org/kangwonlee/18pycpp-03.svg?branch=master) |
| 04 | ![04 master](https://travis-ci.org/kangwonlee/18pycpp-04.svg?branch=master) |
| 05 | ![05 master](https://travis-ci.org/kangwonlee/18pycpp-05.svg?branch=master) |

