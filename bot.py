import pyautogui
import time

# Configurações
imagens_numeros = {
    '1': 'imagens_numeros/numero_1.png',
    '2': 'imagens_numeros/numero_2.png',
    '3': 'imagens_numeros/numero_3.png',
    '4': 'imagens_numeros/numero_4.png'
}

imagens_circulo_laranja = [
    'imagens_circulo_laranja/circulo_laranja_1.png',
    'imagens_circulo_laranja/circulo_laranja_2.png',
    'imagens_circulo_laranja/circulo_laranja_3.png',
    'imagens_circulo_laranja/circulo_laranja_4.png',
    'imagens_circulo_laranja/circulo_laranja_5.png',
    'imagens_circulo_laranja/circulo_laranja_6.png',
    'imagens_circulo_laranja/circulo_laranja_7.png',
    'imagens_circulo_laranja/circulo_laranja_8.png',
    'imagens_circulo_laranja/circulo_laranja_9.png',
    'imagens_circulo_laranja/circulo_laranja_10.png',
    'imagens_circulo_laranja/circulo_laranja_11.png',
    'imagens_circulo_laranja/circulo_laranja_12.png',
    'imagens_circulo_laranja/circulo_laranja_13.png',
    'imagens_circulo_laranja/circulo_laranja_14.png',
    'imagens_circulo_laranja/circulo_laranja_15.png',
    'imagens_circulo_laranja/circulo_laranja_16.png',
    'imagens_circulo_laranja/circulo_laranja_17.png',
    'imagens_circulo_laranja/circulo_laranja_18.png',
    # Adicione mais imagens conforme necessário
]

def encontrar_imagem(imagem, confianca=0.94422222111):
    """
    Função para encontrar a imagem na tela.
    :param imagem: Caminho da imagem a ser encontrada.
    :param confianca: Nível de confiança para a correspondência (entre 0 e 1).
    :return: Localização da imagem (x, y) ou None se não encontrada.
    """
    try:
        localizacao = pyautogui.locateCenterOnScreen(imagem, confidence=confianca)
        if localizacao:
            print(f"Imagem {imagem} encontrada na localização {localizacao}.")
        else:
            print(f"Imagem {imagem} não encontrada.")
        return localizacao
    except pyautogui.ImageNotFoundException:
        print(f"Imagem {imagem} não encontrada (exception).")
        return None

def detectar_circulo_laranja():
    """
    Função para detectar o círculo laranja na tela usando uma lista de imagens.
    :return: True se qualquer imagem do círculo laranja for detectada, False caso contrário.
    """
    for imagem in imagens_circulo_laranja:
        if encontrar_imagem(imagem):
            return True
    return False

def main():
    while True:
        # Verificar se algum número está na tela
        numero_encontrado = None
        for numero, imagem in imagens_numeros.items():
            if encontrar_imagem(imagem):
                numero_encontrado = numero
                break
        
        if numero_encontrado:
            print(f"Número {numero_encontrado} encontrado.")
            
            # Esperar até que a barra branca se torne laranja
            while not detectar_circulo_laranja():
                time.sleep(0.1)
            
            print("Círculo laranja encontrado, pressionando tecla.")
            
            # Pressionar a tecla correspondente ao número encontrado
            pyautogui.press(numero_encontrado)
            print(f"Tecla {numero_encontrado} pressionada.")
        
        # Aguardar um pouco antes da próxima verificação
        time.sleep(0.5)

if __name__ == '__main__':
    main()
