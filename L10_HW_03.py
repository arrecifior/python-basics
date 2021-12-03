##########################################################
###   This program reads student's marks from a file   ###
##########################################################

from os import strerror, path

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line, message):
        Exception.__init__(self, message)
        self.line = line

class FileEmpty(StudentsDataException):
    def __init__(self, filename, message):
        Exception.__init__(self, message)
        self.filename = filename

marks = {}

try:
    # asking user to provide a student data file name
    filename = input("Enter student's data filename: ")
    f = open(filename, "r")

    # checking if the file is empty
    if path.getsize(filename) == 0:
        raise FileEmpty(filename, "file is empty")

    # reading the file
    for line in f:
        data = line.split()
        if len(data) != 3: # checking if line has exactly 3 data pieces
            raise BadLine(line, "Invalid data on line")
        try: # checking if a mark value is a number
            mark = float(data[2])
        except:
            raise BadLine(line, "Invalid mark value on line")
        print(line, end="")
        marks.update({data[0] + ' ' + data[1]: data[2]}) # data[0], [1] and [2] are name, surename and mark respectively

    f.close()
    print(marks)
except BadLine as bd:
    print(bd, ":", bd.line)
except FileEmpty as fe:
    print(fe.filename, ':', fe)
except Exception as exc:
    print("File reading error:", strerror(exc.errno))
