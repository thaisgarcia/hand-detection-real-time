import cv2
import mediapipe as mp
import numpy as np

# Inicializa MediaPipe Hands e as utilidades de desenho
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Erro ao abrir a câmera")
    exit()

# Inicializa o detector de mãos com MediaPipe
with mp_hands.Hands(
    max_num_hands=2,  # Detectar até 2 mãos
    min_detection_confidence=0.5,  # Confiança mínima de detecção
    min_tracking_confidence=0.5  # Confiança mínima de rastreamento
) as hands:
    while True:
        ret, img = capture.read()
        
        if not ret:
            print("Falha ao capturar imagem")
            break
        
        # Converte o BGR para RGB (necessário para MediaPipe)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Processa a imagem para detectar as mãos
        result = hands.process(img_rgb)

        # Se forem detectadas mãos
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Desenha as landmarks das mãos na imagem
                mp_drawing.draw_landmarks(
                    img,  # Imagem original
                    hand_landmarks,  # Coordenadas da mão
                    mp_hands.HAND_CONNECTIONS  # Conexões entre os pontos da mão
                )

        # Mostra a imagem com as mãos detectadas
        cv2.imshow("Imagem ao vivo", img)

        # Pressione 'q' para sair
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

# Libera os recursos
capture.release()
cv2.destroyAllWindows()
