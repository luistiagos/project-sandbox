import youtube_dl

def baixar_video_vimeo(url, nome_arquivo):
    ydl_opts = {
        'outtmpl': nome_arquivo,
        'format': 'bestvideo+bestaudio/best',
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f'O vídeo foi baixado com sucesso e salvo como {nome_arquivo}.')
    except youtube_dl.DownloadError as e:
        print(f'Ocorreu um erro durante o download do vídeo: {str(e)}')

# Exemplo de uso
url_vimeo = 'https://player.vimeo.com/video/790980638?h=85dae4790b'  # Insira o URL do vídeo do Vimeo aqui
nome_arquivo_saida = 'video.mp4'  # Insira o nome do arquivo de saída aqui

baixar_video_vimeo(url_vimeo, nome_arquivo_saida)
