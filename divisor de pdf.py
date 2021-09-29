from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

def dividir_pdf(caminho, arquivo_saida, quantidade = 1, inicio = 0, limite = None):
    """
    Método divide arquivo pdf por um número determinado de paginas.

    Param obrigatórios:
    - caminho: caminho do arquivo
    - arquivo_saida: nome de saída do arquivo

    Param opcionais:
    - quantidade: quantidade de páginas por arquivo/divisão
    - inicio: a partir de onde ele começará a fazer a divisão
    - até onde ele fará a divisão
    """

    pdf = PdfFileReader(caminho, strict = False)

    if limite is None:
        limite = pdf.getNumPages()
    
    parte = 1
    
    for i in range(inicio, limite, quantidade):
        novo_pdf = PdfFileWriter()
        
        for pagina in range(i, quantidade + i):
            if pagina == pdf.getNumPages():
                break
            
            novo_pdf.addPage(pdf.getPage(pagina))
            
            
        saida = f'{arquivo_saida}{str(parte)}.pdf'
        arquivo = open(saida, 'wb')
        novo_pdf.write(arquivo)
        parte += 1





if __name__ == "__main__":
    caminho = input('Digite o caminho do pdf: ')
    caminho = str(Path(caminho))
    dividir_pdf(caminho, 'divisao_', 2, 4, 8)
    
