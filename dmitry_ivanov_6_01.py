###################################################################
###                                                             ###
###   This program outputs system information at user request   ###
###                                                             ###
###################################################################

from platform import python_version
from platform import machine
from platform import processor

'''
'do_print' parameter tells functions if they should
print data to the console themselves.
It is advised to put "print" or nothing
into it for code readability.
'''

# python version
def python_ver(do_print = False):
    if do_print:
        print('''
╒══════════════════════════════════════════╕
┆ Your Python version:                     ┆
└╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
  ''', python_version(), "\n└──────────────────────────────────────────┘", sep="")
    return python_version()

# CPU mode
def cpu_mode(do_print = False):
    if machine() == "x86":
        mode = "32 bit"
    elif machine() == "x86_64" or machine() == "AMD64":
        mode = "64 bit"
    else:
        mode = machine()
    if do_print:
        print('''
╒══════════════════════════════════════════╕
┆ Your CPU mode:                           ┆
└╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
  ''', mode, "\n└──────────────────────────────────────────┘", sep="")
    return mode

# CPU definition
def cpu_def(do_print = False):
    if do_print:
        print('''
╒══════════════════════════════════════════╕
┆ Your CPU definition:                     ┆
└╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
  ''', processor(), "\n└───────────────────────────────────────────", sep="")
    return processor()

# write all info to a file
def info_write():
    file = open("system_info.txt","w")
    file.write("Python version:\n")
    file.write(python_ver())
    file.write("\n")
    file.write("CPU mode:\n")
    file.write(cpu_mode())
    file.write("\n")
    file.write("CPU definition:\n")
    file.write(cpu_def())
    file.write("\n")
    file.close
    print('''
╒══════════════════════════════════════════╕
┆ Data written to system_info.txt          ┆
└╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘''')

# read info from a file
def info_read():
    file = open("system_info.txt","r")
    data = file.read()
    file.close
    print('''
╒══════════════════════════════════════════╕
┆ Data from system_info.txt                ┆
└╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘''')
    print(data, end="")
    print("────────────────────────────────────────────")

##############################
###   Main program logic   ###
##############################

print('''
╔══════════════════════════════════════════╗
║                                          ║
║         System Info Lookup v0.1          ║
║                                          ║
╚══════════════════════════════════════════╝''')

while True: # main loop

    print('''
╒══════════════════════════════════════════╕
│        Please choose an operation:       │
├╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┤
│  v Python (v)ersion                      │
│  m CPU (m)ode (32 bit or 64 bit)         │
│  d CPU (d)efinition                      │
│                                          │
│  w (W)rite data to a file                │
│  r (R)ead data from a file               │
│                                          │
│  q (Q)uit the program                    │
└──────────────────────────────────────────┘''')

    # request user input
    oper = input(":")

    # handling user input
    if oper.lower() == "v" or oper.lower() == "version":
        python_ver("print")
    elif oper.lower() == "m" or oper.lower() == "mode":
        cpu_mode("print")
    elif oper.lower() == "d" or oper.lower() == "definition":
        cpu_def("print")
    elif oper.lower() == "w" or oper.lower() == "write":
        info_write()
    elif oper.lower() == "r" or oper.lower() == "read":
        info_read()
    elif oper.lower() == "q" or oper.lower() == "quit":
        break
    else:
        print("Invalid input. Please try again.")

print("Closing the program ...")
