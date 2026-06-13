# Ham bam Blake2 (blake2b) su dung thu vien hashlib co san
import hashlib


def blake2_hash(message):
    return hashlib.blake2b(message.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    text = input("Nhap chuoi can bam Blake2: ")
    print("Gia tri bam Blake2:", blake2_hash(text))
