#hexhexadecimal
from ASCII import *
def hexdecode(hexstring:str)->str:
    return decodeAscII(bytes.fromhex(hexstring)) #decode hex -> ascii -> string 

def hexencode(normalstring:str):
    return (bytes.hex(normalstring.encode())) #encode hex  <- bytes <- ascii <- string 

if __name__ == "__main__":
    print(hexdecode("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))
    print(hexencode("crypto{You_will_be_working_with_hex_strings_a_lot}"))


