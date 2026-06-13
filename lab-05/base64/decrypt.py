# Giai ma thong tin su dung Base64
import base64


def base64_decode(encoded_message):
    # Giai ma Base64 ve lai chuoi ban dau
    encoded_bytes = encoded_message.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_bytes)
    return decoded_bytes.decode("utf-8")


if __name__ == "__main__":
    text = input("Nhap chuoi Base64 can giai ma: ")
    print("Chuoi sau khi giai ma:", base64_decode(text))
