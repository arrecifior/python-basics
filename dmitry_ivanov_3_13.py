"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program sets a second bit to 1 if it not equal 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# input value
binary = int('0101010101', 2)
# mask for bit 2
mask = int('0000000010', 2)

# this operation sets bits provided in mask to 1
print("Input        : ", bin(binary))
print("Mask applied : ", bin(binary|mask))
