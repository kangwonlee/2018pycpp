# https://stackoverflow.com/questions/35160256/how-do-i-output-lists-as-a-table-in-jupyter-notebook
# http://nbviewer.jupyter.org/github/ipython/ipython/blob/4.0.x/examples/IPython%20Kernel/Rich%20Output.ipynb
# https://meta.stackexchange.com/questions/5916/allow-marking-text-as-fixed-width-font

import IPython
import pylab as py
import collections


def main():
    base_addr = 0x60000000
    size_t = 4
    no_cell = 20

    memory_map_random(base_addr, size_t, no_cell)


def memory_map_random(base_addr, size_t, no_cell):

    contents_dict = malloc(size_t, no_cell, base_addr)

    show(contents_dict)


def show(contents_dict):
    """
    Show md table in the ipynb
    """
    rows_list = get_md_table(contents_dict)

    IPython.display.display(IPython.display.Markdown('\n'.join(rows_list)))


def malloc(element_size, num_elements,base_addr=0x60000000):
    """
    Build an OrderdDict of (int : int) pairs for a memory map starting a base memory address
    """
    contents_dict = collections.OrderedDict(
        {
            'header': ['Address (hex)','Content (hex)'], # header list
            'content_formatter': f'<pre>%0{2*element_size}x</pre>' # adjustable to element_size
        }
    )

    # Content builder loop
    for i in range(base_addr, base_addr+(num_elements*element_size)+1, element_size):
        key = i
        value = py.randint(0, 2**31-1)

        contents_dict[key] = value

    return contents_dict


def get_md_table(contents_dict):
    """
    Convert an OrderdDict of (int : int) pairs into a multiline md table string
    contents_dict : orderd dictionary of (int : int) pairs
    """
    rows_list = [
        '|'.join(contents_dict['header']), # header list -> header string
        '|'.join([':-----:'] * len(contents_dict['header'])) # separator string
    ]

    # Markdown converter table
    for key in contents_dict:
        if  not isinstance(key, str): # to skip keys of strings
            columns_list = [f'<pre>{key:08x}</pre>', 
            contents_dict['content_formatter'] % contents_dict[key]]

            # Indicate a row of the table
            rows_list.append('|'.join(columns_list))

    return rows_list


if "__main__" == __name__:
    main()

