try:
    stream = open("file.txt", "rt")
    # processing
    stream.close
except Exception as exc:
    print("Cannot open file:", exc)

###

import errno
try:
    s = open("file.txt", "rt")
    # processing
    s.close
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("This file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)

###

from os import strerror

try:
    s = open("file.txt", "rt")
    # processing
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))