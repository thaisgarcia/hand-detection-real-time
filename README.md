# Detecção de Mãos em Tempo Real com MediaPipe

Este projeto utiliza a biblioteca OpenCV e o MediaPipe para detectar e exibir as mãos em tempo real usando a câmera do computador.

## Pré-requisitos

Antes de executar o código, você precisará instalar as seguintes bibliotecas:

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/guide?hl=pt-br)
- [NumPy](https://numpy.org/)

Você pode instalar essas dependências usando o seguinte comando:

```bash
pip install opencv-python mediapipe numpy
```

## Como Usar

1. Clone este repositório:

   ```bash
   
   git clone https://github.com/thaisgarcia/hand-detection-real-time.git
   cd hand-detection-real-time
   ```

2. Execute o script Python:

   ```bash
   python detector.py
   ```

   O código tenta acessar a câmera padrão usando o índice `0`. Se você tiver mais de uma câmera conectada ao seu computador, você pode precisar alterar este número (de `0` para `1`, `2`, etc.) no seguinte trecho do código:

   ```python
   capture = cv2.VideoCapture(0)
   ```

3. **Tratamento de Erros**:
   Se o programa não conseguir abrir a câmera, uma mensagem de erro será exibida:

   ```
   Erro ao abrir a câmera
   ```

   Nesse caso, verifique:

   - Se a câmera está conectada corretamente e funcionando.
   - Se outra aplicação não está usando a câmera.
   - Tente alterar o índice da câmera (por exemplo, de `0` para `1`) no código.
   - Verifique se os drivers da câmera estão atualizados.

4. Para encerrar o programa, pressione a tecla `q`.

## Descrição do Código

- **Inicialização**:
  O código começa inicializando o MediaPipe Hands e as utilidades de desenho.

- **Captura de Vídeo**:
  A captura de vídeo é iniciada usando a câmera padrão (índice `0`).

- **Detecção de Mãos**:
  Com a configuração do detector de mãos, o código processa cada frame da imagem capturada e detecta as mãos, desenhando as landmarks (pontos) correspondentes.

- **Exibição**:
  A imagem ao vivo com as mãos detectadas é exibida em uma janela.

- **Finalização**:
  O programa libera os recursos da câmera e fecha todas as janelas ao sair.
