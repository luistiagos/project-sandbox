from PIL import Image
import os

def converter_para_webp_e_reduzir(imagem_path, destino_path, qualidade=50, nova_largura=0):
    img = Image.open(imagem_path)
    
    # Reduzir a largura da imagem, mantendo a proporção
    largura_original, altura_original = img.size
    nova_altura = altura_original
    if nova_largura == 0:
        nova_largura = largura_original
    else:
        nova_altura =  int((nova_largura / largura_original) * altura_original) 
    #nova_largura = largura_maxima
    #nova_altura = int(altura_original * (nova_largura / largura_original))
    img = img.resize((nova_largura, nova_altura), Image.ANTIALIAS)
    
    # Salvar a imagem no formato WebP
    nome_arquivo, _ = os.path.splitext(os.path.basename(imagem_path))
    arq = nome_arquivo + _
    if arq in destino_path:
        destino_path = destino_path.replace(arq, '')
    destino = os.path.join(destino_path, f"{nome_arquivo}.webp")
    img.save(destino, "WEBP", quality=qualidade)
    
def processar_pasta(pasta_origem, pasta_destino, qualidade, largura_maxima):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for arquivo in os.listdir(pasta_origem):
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            imagem_path = os.path.join(pasta_origem, arquivo)
            converter_para_webp_e_reduzir(imagem_path, pasta_destino,qualidade,largura_maxima)
            
def processar_arquivo(imagem_path, pasta_destino, qualidade, largura_maxima):
    if imagem_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        converter_para_webp_e_reduzir(imagem_path, pasta_destino, qualidade, largura_maxima)
        print(f"Conversão concluída para {os.path.basename(imagem_path)}")


caminho_origem = "C:\\projetos\\emuladores.github.io\\52emul\\images\\sale.png"
caminho_destino = caminho_origem
qualidade = 90
largura_maxima = 350

            
if os.path.isdir(caminho_origem):
    processar_pasta(caminho_origem, caminho_destino, qualidade, largura_maxima)
elif os.path.isfile(caminho_origem):
    processar_arquivo(caminho_origem, caminho_destino, qualidade, largura_maxima)
else:
    print("Caminho inválido.")

print("Conversão e redução concluídas!")
