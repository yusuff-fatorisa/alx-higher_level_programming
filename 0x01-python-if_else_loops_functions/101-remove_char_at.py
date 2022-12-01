#!/usr/bin/python3
def remove_char_at(strs, n):
    str_copy = ""
    if n < 0 or n > len(strs) - 1:
        return strs
    else:
        for count in range(len(strs)):
            if count != n:
                str_copy += strs[count]
        return str_copy
