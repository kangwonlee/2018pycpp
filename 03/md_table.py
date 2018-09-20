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

    contents_list = malloc(size_t, no_cell, base_addr)

    show(contents_list)


def show(contents_list):
    """
    Show md table in the ipynb
    """
    rows_list = get_md_table(contents_list)

    IPython.display.display(IPython.display.Markdown('\n'.join(rows_list)))


def malloc(element_size, num_elements,base_addr=0x60000000):
    """
    Build a list of list of strings for a memory map starting a base memory address
    """
    contents_list = [
        ['Address (hex)','Content (hex)'], # header list
    ]

    # adjustable to element_size
    content_formatter = f'<pre>%0{2*element_size}x</pre>'

    # Content builder loop
    for i in range(base_addr, base_addr+(num_elements*element_size)+1, element_size):

        one_row_list = [f'<pre>{i:08x}</pre>', content_formatter % py.randint(0, 2**31-1)]
        contents_list.append(one_row_list)

    return contents_list


def get_md_table(contents_list):
    """
    Convert list of list into a multiline md table string
    contents_list : list of list of strings
    """
    rows_list = [
        '|'.join(contents_list[0]), # header list -> header string
        '|'.join([':-----:'] * len(contents_list[0])) # separator string
    ]

    # Markdown converter table
    for columns_list in contents_list:

        # Indicate a row of the table
        rows_list.append('|'.join(columns_list))
    return rows_list


if "__main__" == __name__:
    main()

