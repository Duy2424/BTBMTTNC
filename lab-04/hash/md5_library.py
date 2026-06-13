# Ham bam MD5 su dung thu vien hashlib co san
import hashlib


def md5_hash(message):
    return hashlib.md5(message.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    text = input("Nhap chuoi can bam MD5: ")
    print("Gia tri bam MD5:", md5_hash(text))
