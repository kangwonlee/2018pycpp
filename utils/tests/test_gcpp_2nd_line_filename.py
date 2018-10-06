import utils.get_cpp_from_ipynb as gcpp 
import pytest


cpp_compile_test_case = """//```\n// Begin account_module_user.cpp
#include <iostream>
#include <cstdint>

namespace account_a{
    #include "account_module.h"
}

namespace account_b{
    #include "account_module.h"
}

using namespace std;

int32_t main(int32_t argn, char ** argv){

}
"""

cpp_test_cases = [
    ("""//```
void main (){
}
""", ""),

    ("""// ```
int main (int argn, char * argv[]){
    return 0;
}
""", ""),

    ("""// ```
int mann (int argn, char * argv[]){
    return 0;
}
""", ""),

    ("""// ```
int mann (int argn, char * argv[]){
    return main(a, b);
}
""", ""),

    ("""#include <iostream>
#include <cstdint>

namespace account_a{
    #include "account_module.h"
}

namespace account_b{
    #include "account_module.h"
}

using namespace std;

int32_t main (int argn, char * argv[]){
    return 0;
}
""", ""),
    (cpp_compile_test_case, "account_module_user.cpp"),
    ('''// ``` C++
// Begin account_module.h
#include <cstdint>


void deposit (int32_t amount);
void withdraw (int32_t amount);
int32_t check();
// End account_module.h\n// ```''', "account_module.h")
]


# https://docs.pytest.org/en/latest/example/parametrize.html
@pytest.mark.parametrize("cpp_txt, expected", cpp_test_cases)
def test_get_filename_in_second_line(cpp_txt, expected):
    result = gcpp.get_filename_in_second_line(cpp_txt)
    message = f"Unable to match case :{cpp_txt}"

    if expected:
        assert result, message
    else:
        assert not (result), message
