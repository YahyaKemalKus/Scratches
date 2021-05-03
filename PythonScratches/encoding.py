def char_to_bytes(harfler,encodings):#encoder
    assert isinstance(harfler,str) and isinstance(encodings,list),\
        "ilk parametreye string,ikinci parametreye liste girmelisiniz."

    print("HARF".ljust(20),end="")
    for encoding in encodings:
        print(f"{(encoding+':byte').upper().ljust(20)+(encoding+':int').upper().ljust(20)}",end="")

    for harf in harfler:
        sonuc="\n"+harf.ljust(20)
        for encoding in encodings:
            sonuc += str(harf.encode(encoding,errors="replace")).ljust(20) + \
                str(int.from_bytes(bytes(harf, encoding,errors="ignore"), "big")).ljust(20)
        print(sonuc)

#char_to_bytes("ş",["utf-8","cp1254","unicode_escape"])  #ornek kullanim.

def bytes_to_char(byte,encodings):#decoder
    assert isinstance(byte,bytes) and isinstance(encodings,list),\
        "girdiginiz ilk parametreye byte,ikinci parametreye liste girmelisiniz"
    for encoding in encodings:
        print(f"{(encoding.upper()+':karakter').ljust(20)}",end="")
    print()
    for encoding in encodings:
        print(byte.decode(encoding=encoding,errors="replace").ljust(20),end="")

#bytes_to_char(b'\xc5',["utf8","cp1250"])  #ornek kullanim