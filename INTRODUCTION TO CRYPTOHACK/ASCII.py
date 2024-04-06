
def decodeAscII(flag:list)->str:
    #this fun convert ascii to the real massage 
    return(''.join(chr(o) for o in flag)) #decode the massage 

def encodeAscii(flag:str)->list:
    #this fun convert massage to ascii 
    return([ord(o) for o in flag]) # encode the massage in ASCII format 
if __name__ == "__main__":
    print(decodeAscII([99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]))
    print(encodeAscii("crypto{ASCII_pr1nt4bl3}"))
