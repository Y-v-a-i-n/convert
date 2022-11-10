# convert
A simple algorithm in python to convert values in binary, octal, decimal, hexadecimal and BCD
```py
print(convert(0b1010))
-> "binaire : 1010 | octal : 12 | decimal : 10 | hexadecimal : a | BCD : 0001 0000"
print(convert(0o76))
-> "binaire : 111110 | octal : 76 | decimal : 62 | hexadecimal : 3e | BCD : 0110 0010"
print(convert(98))
-> "binaire : 1100010 | octal : 142 | decimal : 98 | hexadecimal : 62 | BCD : 1001 1000"
print(convert(0xFF))
-> "binaire : 11111111 | octal : 377 | decimal : 255 | hexadecimal : ff | BCD : 0010 0101 0101"
print(BCD("0101 0101"))
-> "binaire : 110111 | octal : 67 | decimal : 55 | hexadecimal : 37 | BCD : 0101 0101"
```
