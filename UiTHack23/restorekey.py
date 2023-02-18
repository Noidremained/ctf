from   pickle import load
from   sys import argv
import math


def B(s:str) -> int:
    return int.from_bytes(s.encode(), byteorder="big")

def E(p:str, q:str) -> int:
    return B(p)^q


if __name__ == "__main__":
    if len(argv) != 3:
        exit(f"usage: python {__file__} <key-file> <jungle-file> ")

    jungle, (KFile, JFile) = "jungle-of-keys.bin", argv[1:]
    thejungle = load(open(jungle, "rb"))
    J = open(JFile, encoding="utf-8").readlines()
    K = open(KFile, "w")
    
    numberlist = []
    for i in thejungle:
        numbers = [int(s) for s in i.split("/") if s.isdigit()]
        for number in numbers:
            if number not in numberlist:
                numberlist.append(number)
    
    key = []
    for i in range(len(numberlist)):
        keypart = E(J[i], numberlist[i])
        length = math.ceil(keypart.bit_length() / 8)
        keypart = keypart.to_bytes(length=length, byteorder="big").decode()
        key.append(keypart)
        
    key = "-".join(key)
    K.write(key)
    K.close()
    print("key restored")