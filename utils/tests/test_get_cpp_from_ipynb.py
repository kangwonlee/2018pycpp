import utils.get_cpp_from_ipynb as gcpp 
import pytest


def test_get_main_function_pattern():
    r = gcpp.get_main_function_pattern()
    test_case_1 = """
void main (){
}
"""

    test_case_2 = """
int main (int argn, char * argv[]){
    return 0;
}
"""
    assert r.findall(test_case_1), "Unable to match case 1"
    assert r.findall(test_case_2), "Unable to match case 2"
