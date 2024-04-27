import zlib

# String que você deseja compactar
texto_original = "Esta é uma string para compactar usando zlib."

# Compactar a string
texto_compactado = zlib.compress(texto_original.encode())

# Descompactar a string
texto_descompactado = zlib.decompress(texto_compactado).decode()

print("Texto original:", texto_original)
print("Texto compactado:", texto_compactado)
print("Texto descompactado:", texto_descompactado)