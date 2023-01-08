#!/usr/bin/python3
def no_c(my_string):
    m_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            m_string = m_string + i
    return m_string
