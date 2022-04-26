import string

if __name__ == "__main__":
    one_byte = "h"
    print("Encode:", one_byte.encode("utf-8"))
    print(len(one_byte.encode("utf-8")))
    one_or_four_bytes = "😃"
    print("----------")
    print(one_or_four_bytes.encode("utf-8"))
    print(len(one_or_four_bytes.encode("utf-8")))
    print(string.ascii_lowercase.index("a"))
    print(ascii({"key": "this is a value"}))
    print(bin(2))
    print(chr(223))
    print("Fromating a {} with {} {}".format("string", "format", "method"))
    print('Changing {1} with {2} {0}'.format('method','order','format'))
    # python 2 vs python 3
    print('----Python 2 vs 3----')
    print(type(b'byte type exist in python 3'))
    for element in bytearray(b'arreglo de bytes'):
        print('byte:', element)
    print('add string to byte' + b'throws error')
    