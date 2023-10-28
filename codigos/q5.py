frase = input("fala ai uma frase: ")

palavras = frase.split()

palavrasReversas = [palavra[::-1] for palavra in palavras]

fraseReversa = ' '.join(palavrasReversas)

print("sua frase ao contrario e: ", faseReversa)