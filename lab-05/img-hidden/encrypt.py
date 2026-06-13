# Giau thong tin trong anh bang ky thuat LSB (Least Significant Bit)
from PIL import Image

# Chuoi danh dau ket thuc thong diep
DELIMITER = "#####"


def to_binary(message):
    # Chuyen chuoi thanh chuoi nhi phan 8 bit moi ky tu
    return "".join(format(ord(char), "08b") for char in message)


def encode_image(image_path, message, output_path):
    # Mo anh va chuyen sang che do RGB
    image = Image.open(image_path)
    image = image.convert("RGB")

    # Them delimiter de danh dau diem ket thuc thong diep
    message += DELIMITER
    binary_message = to_binary(message)

    data = list(image.getdata())
    new_data = []
    index = 0

    for pixel in data:
        r, g, b = pixel
        # Giau bit vao bit cuoi cung (LSB) cua tung kenh mau
        if index < len(binary_message):
            r = (r & ~1) | int(binary_message[index])
            index += 1
        if index < len(binary_message):
            g = (g & ~1) | int(binary_message[index])
            index += 1
        if index < len(binary_message):
            b = (b & ~1) | int(binary_message[index])
            index += 1
        new_data.append((r, g, b))

    image.putdata(new_data)
    # Luu duoi dinh dang PNG (khong nen, bao toan LSB) du ten file la .jpg
    # JPEG la dinh dang nen mat du lieu nen se lam hong bit da giau
    image.save(output_path, format="PNG")
    print("Da giau thong diep va luu vao:", output_path)


if __name__ == "__main__":
    message = input("Nhap thong diep can giau: ")
    encode_image("image.jpg", message, "encoded_image.jpg")
