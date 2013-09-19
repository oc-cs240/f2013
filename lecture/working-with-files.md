Working With Files
==================

Accessing a file object
-----------------------

    open()      (preferred)
    file()      (deprecated)

    open(name[, mode[, buffering]])

### File modes

* r - Read (default)
* w - Write (also erase!)
* a - Append (like w, but without the erase)

Examples

    output = open('output.txt', 'w')
    input = open('input.txt', 'r')


