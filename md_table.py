# https://stackoverflow.com/questions/35160256/how-do-i-output-lists-as-a-table-in-jupyter-notebook
# http://nbviewer.jupyter.org/github/ipython/ipython/blob/4.0.x/examples/IPython%20Kernel/Rich%20Output.ipynb
# https://meta.stackexchange.com/questions/5916/allow-marking-text-as-fixed-width-font

import IPython
import pylab as py


def main():
    base_addr = 0x60000000
    size_t = 4
    no_cell = 20

    memory_map_random(base_addr, size_t, no_cell)


def memory_map_random(base_addr, size_t, no_cell):

    rows_list = [''' Address (hex) | Content (hex) \n'''
                ''':-------------:|:-------------:''']

    contet_formatter = '<pre>%0' + str(2*size_t) + 'x</pre>'

    # Decimal number loop
    for i in range(base_addr, base_addr+(no_cell*size_t)+1, size_t):

        columns_list = [f'<pre>{i:08x}</pre>',contet_formatter % py.randint(0, 2**31-1)]

        # Indicate a row of the table
        rows_list.append('|'.join(columns_list))

    IPython.display.display(IPython.display.Markdown('\n'.join(rows_list)))


if "__main__" == __name__:
    main()

