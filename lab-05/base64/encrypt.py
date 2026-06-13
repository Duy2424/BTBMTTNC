# Ma hoa thong tin su dung Base64
import base64


def base64_encode(message):
    # Chuyen chuoi thanh byte roi ma hoa Base64
    message_bytes = message.encode("utf-8")
    encoded_bytes = base64.b64encode(message_bytes)
    return encoded_bytes.decode("utf-8")


if __name__ == "__main__":
    text = input("Nhap chuoi can ma hoa: ")
    print("Chuoi sau khi ma hoa Base64:", base64_encode(text))
