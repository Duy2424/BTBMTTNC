# Ham bam SHA-3 (sha3_256) su dung thu vien hashlib co san
import hashlib


def sha3_hash(message):
    return hashlib.sha3_256(message.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    text = input("Nhap chuoi can bam SHA-3: ")
    print("Gia tri bam SHA-3:", sha3_hash(text))
