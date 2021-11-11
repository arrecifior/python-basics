###########################################################
### Playing with print() function and output formatting ###
###########################################################

# Standard output
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****", end="\n\n")

# Output using one print() statement 
print("    *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *", "  *****", sep="\n", end="\n\n")

# Larger arrow
print(" ", " ", " ", " ", "*", " ", " ", " ", " ", end="\n\n")
print(" ", " ", " ", "*", " ", "*", " ", " ", " ", end="\n\n")
print(" ", " ", "*", " ", " ", " ", "*", " ", " ", end="\n\n")
print(" ", "*", " ", " ", " ", " ", " ", "*", " ", end="\n\n")
print("*", "*", "*", " ", " ", " ", "*", "*", "*", end="\n\n")
print(" ", " ", "*", " ", " ", " ", "*", " ", " ", end="\n\n")
print(" ", " ", "*", " ", " ", " ", "*", " ", " ", end="\n\n")
print(" ", " ", "*", "*", "*", "*", "*", " ", " ", end="\n\n\n")

# Duplicating the arrow
print('    *    '*2)
print('   * *   '*2)
print('  *   *  '*2)
print(' *     * '*2)
print('***   ***'*2)
print('  *   *  '*2)
print('  *   *  '*2)
print('  *****  '*2, end="\n\n")