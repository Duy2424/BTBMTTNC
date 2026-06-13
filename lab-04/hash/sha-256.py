# Ham bam SHA-256 su dung thu vien hashlib co san
import hashlib


def sha256_hash(message):
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    text = input("Nhap chuoi can bam SHA-256: ")
    print("Gia tri bam SHA-256:", sha256_hash(text))
