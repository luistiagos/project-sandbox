import os

pasta = 'C:\projetos\emuladores.github.io\50emul\images\compresspng'  # Substitua pelo caminho da sua pasta

for nome_arquivo in os.listdir(pasta):
    caminho_completo = os.path.join(pasta, nome_arquivo)
    
    if os.path.isfile(caminho_completo):
        novo_nome = nome_arquivo.replace('-min', '')
        novo_caminho = os.path.join(pasta, novo_nome)
        
        os.rename(caminho_completo, novo_caminho)
        print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome}")
