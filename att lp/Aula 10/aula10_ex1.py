import os # biblioteca
from pathlib import Path # biblioteca

def listar_arquivos(diretorio="C:\\senai"):  # nome da variável
    arquivos = os.listdir(diretorio) # os arquivos de dentro do diretorio devem ser listados 
    print(arquivos)  # imprime o nome de cada arquivo 
    return arquivos # retorna "arquivos"

def obter_tamanho_arquivo(nome_arquivo):  # nome da variável
    arquivo = Path(nome_arquivo)  # manipula o caminho dos arquivos de acordo com o nome dentro do diretório
    if arquivo.exists():  # se o arquivo existe
        tamanho_bytes = arquivo.stat().st_size  # Obtém o tamanho em bytes
        tamanho_kb = tamanho_bytes / 1_024  # Converte para kilobytes (1 KB = 1.024 bytes)
        return round(tamanho_kb, 3)  # Retorna o tamanho em KB com 2 casas decimais
    return None  # Retorna None se o arquivo não existir

def salvar_tamanho_arquivo(nome_arquivo, nome_saida): # nome da variável
    tamanho = obter_tamanho_arquivo(nome_arquivo) # obtem o tamanho do arquivo
    if tamanho is not None: # se o tamanho não for inexistente 
        with open(nome_saida, "w") as f: # abre um arquivo para escrita levando em conta o nome qu sera dado após revisão (nome_saida)
            f.write(f"O tamanho do arquivo '{nome_arquivo}' é {tamanho} bytes.\n") # escreve a saida
        print("Tamanho salvo com sucesso!") # imprime que deu certo, pois o arquivo está de acordo
    else:
        print("Arquivo não encontrado.") # imprime que deu errado, pois o arquivo não está de acordo
        
tamanho = obter_tamanho_arquivo("C:\\senai\\doce.txt")

print(tamanho)

salvar_tamanho_arquivo("C:\\senai\\doce.txt", "C:\\senai\\coco.txt")
