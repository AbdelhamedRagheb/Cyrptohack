from pwn import xor
# xor can do encode and decode 
#k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
#k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
#flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
#print(xor(k1,k2_3,flag))

# can xor with integer 
#print(xor(b'label',13))  

#flag=bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
#key = flag[0] ^ ord('c')
#print(key)
#print(xor(flag,key))


secrt = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(secrt,b'crypto{'))
print(xor(secrt,b'myXORkey'))