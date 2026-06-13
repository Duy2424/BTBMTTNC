import math


K = [int(abs(math.sin(i + 1)) * (2 ** 32)) & 0xFFFFFFFF for i in range(64)]

S = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21,
]


def left_rotate(x, c):
    x = x & 0xFFFFFFFF
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF


def md5(message):
    message = bytearray(message.encode("utf-8"))
    orig_len_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF

    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)

    message += orig_len_bits.to_bytes(8, byteorder="little")

    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset:chunk_offset + 64]
        M = [int.from_bytes(chunk[i:i + 4], byteorder="little")
             for i in range(0, 64, 4)]

        A, B, C, D = a0, b0, c0, d0

        for i in range(64):
            if 0 <= i <= 15:
                F = (B & C) | (~B & D)
                g = i
            elif 16 <= i <= 31:
                F = (D & B) | (~D & C)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7 * i) % 16

            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + left_rotate(F, S[i])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    result = b"".join(x.to_bytes(4, byteorder="little")
                      for x in (a0, b0, c0, d0))
    return result.hex()


if __name__ == "__main__":
    text = input("Nhap chuoi can bam MD5: ")
    print("Gia tri bam MD5:", md5(text))
