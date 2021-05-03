from XoR_DeCrypter import XoR_DeCrypter  #kendi yazdigim bir modul
siff="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hexy=[int(siff[i:i+2],16) for i in range(0,len(siff),2)]
for i in range(128):
    print("".join([chr(int(x)^i) for x in hexy]))  # ilk cozdugum sifrelenmis metin ve algoritmasi.ILKLER UNUTULMAZ!

#Çözüldü cevap:Cooking MC's like a pound of bacon
