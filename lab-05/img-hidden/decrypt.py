# Giai ma thong diep da giau trong anh bang ky thuat LSB
from PIL import Image

# Chuoi danh dau ket thuc thong diep
DELIMITER = "#####"


def decode_image(image_path):
    # Mo anh chua thong diep
    image = Image.open(image_path)
    image = image.convert("RGB")

    data = list(image.getdata())
    binary_message = ""

    # Lay bit cuoi cung (LSB) cua tung kenh mau
    for pixel in data:
        r, g, b = pixel
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)

    # Chuyen tung nhom 8 bit thanh ky tu
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        message += char
        # Kiem tra delimiter de dung
        if message.endswith(DELIMITER):
            return message[:-len(DELIMITER)]

    return "Khong tim thay thong diep an."


if __name__ == "__main__":
    result = decode_image("encoded_image.jpg")
    print("Thong diep da giai ma:", result)
