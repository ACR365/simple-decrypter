ciphertext = 'hpGsl7pG46nnp44q6ww0G5lvpyGnzy53zwGzqG5spGpypx0G4611w0GwtypKGcptyqz3npxpy54Gl3pGpyG3z65pG5zGz63G1z4t5tzyKGZ63G4nz654Gsl7pG3p1z35poGspl70Gpypx0Gln5t7t50Gl5G5spGyz35sKGhpGyppoG5zGmpG13p1l3poGqz3GlyGl55lnvGl5Gol8yK'
list_of_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.'

def findThePlainText(ctext): #Decrypt ciphertext to plaintext
 
    for los in list_of_symbols:
        key = ord(los)
        print("Key: ", los)

        plaintext = ""
        for c in ciphertext:
            pt = list_of_symbols[((list_of_symbols.find(c) - key) + len(list_of_symbols)) % len(list_of_symbols)] #.find() => finds the symbol within the list and then decrypts
            plaintext = plaintext + pt
        
        print(plaintext)

findThePlainText(ciphertext)


