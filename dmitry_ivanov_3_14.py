"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program resets bits 2 and 3 to 0

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# input value
binary = int('0101010111', 2)
# mask for bits 2 and 3
mask = int('1111111001', 2)

# this operation sets bits provided in mask to 0
print("Input        : ", bin(binary))
print("Mask applied : ", bin(binary&mask))
