ciphertext = "Mom zgldmpx aspjl, lpw tedspbxk uywgsk, xjv kewrepvy deszgj tvp usmfl, ls tvxkxc h zijmgra wh tskl, ql'k nzox e vltwalisp tlhsv fhlw ty xjv akrb vn i fjmgeh."
key = "thisisasecretkey"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def findThePlaintext_VigenereCipher(ctext):
    plaintext = ""
    
    c = 0
    while c < len(ciphertext):
        dtext = []
        for k in key:
            if ctext[c].isalpha():
                dt = (alphabet.find(ctext[c]) - alphabet.find(k)) % 52
                dtext.append(dt)
                c = c + 1

                if c >= len(ciphertext):
                    break
            else:
                dtext.append(ctext[c])
                c = c + 1
                
                if c >= len(ciphertext):
                    break
        
        for d in dtext:
            if isinstance(d, int):
                plaintext = plaintext + alphabet[d]
            else:
                plaintext = plaintext + d
    
    return plaintext
            
plaintext = findThePlaintext_VigenereCipher(ciphertext)
print(plaintext.upper())