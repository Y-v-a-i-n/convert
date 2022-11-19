def prefixDel(number,prefix):
    return str(number).split(prefix)[1]
def convert(number):
    BCD="";
    for hihi in list(str(number)):
        bae=prefixDel(bin(int(hihi)),"0b");
        while len(bae)!=4:
            bae="0"+bae;
        BCD+=bae+" ";
    return {"binaire": prefixDel(bin(number),"0b"), 'octal': prefixDel(oct(number),"0o"), 'decimal': str(int(number)), "hexadecimal": prefixDel(hex(number),"0x"), "BCD": BCD}
def BCD(number):
    finalNumber="";
    ifBCDValid=True;
    for binary in str(number).split(" "):
        toDec=eval("0b"+binary);
        if toDec<=9 and toDec>=0 and ifBCDValid:
            finalNumber+=str(toDec);
        else:
            ifBCDValid=False;
    if ifBCDValid:
        return convert(int(finalNumber));
def count(N):
    number = 0;
    while number != N+1:
        print(convert(number));
        number+=1;
