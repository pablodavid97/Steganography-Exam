import cv2
from PIL import Image, ImageChops
import pytesseract
import caesar

def main():
    '''
        PARTE I: MANIPULACION DE IMAGEN Y CAPTURA DE MENSAJE SECRETO
    '''
    img = Image.open('matroska.png')
    format = img.format
    size = img.size
    mode = img.mode

    print("Image Format: ", format, "Image Size: ", size, "Image Mode: ", mode)

    img_width = size[0]
    img_height = size[1]

    img_bitmap = img.load()

    # Convierte el archivo en blanco y negro

    print("filtering image...")
    for i in range(img_width):
        for j in range(img_height):
            old_pixel = img_bitmap[i, j]
            red = old_pixel[0]
            green = old_pixel[1]
            blue = old_pixel[2]

            new_pixel = pixel_filter(red, green, blue)

            img_bitmap[i, j] = new_pixel

    img.save('matroska-filtered.png')

    print("done...")

    message_img = cv2.imread('matroska-filtered-message.png')
    ciphered_text = message_extract(message_img)

    print("Ciphered Message: ", ciphered_text)

    ciphered_text_lines = ciphered_text.split("{!@#$%}")
    ciphered_text_lines.pop()
    ciphered_text_lines[:] = [item for item in ciphered_text_lines if item]
    length = len(ciphered_text_lines)

    for i in range(length):
        ciphered_text_lines[i] = ciphered_text_lines[i].replace(" ", "")

    print("Lines in text: ", length)
    # for line in ciphered_text_lines:
    #     print(line + "\n")

    with open("ciphered-message.txt", "w") as cFile:
        for line in ciphered_text_lines:
            cFile.write(line + "\n")

    '''
        PARTE II: PROCESO DE DESENCRIPCION DEL MENSAJE

    '''

    # text = caesar.decrypt("EXXEGOexsrgi", 4)
    # print("Decripted message: ", text)

    for key in range(1, 51):
        # print("Key: ", key)
        with open("decoded-message" + str(key) + ".txt", "w") as dFile:
            for line in ciphered_text_lines:
                text = caesar.decrypt(line, key)
                dFile.write(text + "\n")

    deciphered_text = []

    with open("decoded-message31.txt", "r") as rFile:
        line = rFile.readline()
        while line:
            deciphered_text.append(line)
            line = rFile.readline()

    length = len(deciphered_text)
    for i in range(length):
        deciphered_text[i] = deciphered_text[i].replace("X", " ")
        deciphered_text[i] = deciphered_text[i].replace("=", "")
        print(deciphered_text[i] + "\n")


def pixel_filter(red, green, blue):
    new_red = 0
    new_green = 0
    new_blue = 0

    if(red % 2 == 0):
        new_red = 1
    else:
        new_red = 0

    if(green % 2 == 0):
        new_green = 1
    else:
        new_green = 0

    if(blue % 2 == 0):
        new_blue = 1
    else:
        new_blue = 0

    return (new_red, new_green, new_blue)

# returns Image object with just the text
def message_extract(image):
    text = pytesseract.image_to_string(image)

    text = text.replace("\n", "{!@#$%}")

    result = text

    return result

if __name__ == "__main__":
    main()

