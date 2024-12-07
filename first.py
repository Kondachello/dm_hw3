import hashlib

def calculate_hash_operations():
    s = "DM Fall 2024 HW3".encode("utf-8")
    hash_hex = hashlib.sha256(s).hexdigest()

    hash_bin = bin(int(hash_hex, 16))[2:].zfill(256)

    slices = [int(hash_bin[i:i + 32], 2) for i in range(0, 256, 32)]

    d = slices[0]
    for r in slices[1:]:
        d ^= r

    w = d ^ 0x7613a0ca

    return {
        "hash_hex": hash_hex,
        "hash_bin": hash_bin,
        "slices": slices,
        "d": d,
        "w": w,
    }


result = calculate_hash_operations()
print("SHA-256 hash (hex):", result["hash_hex"])
print("Binary hash:", result["hash_bin"])
print("32-bit slices:", result["slices"])
print("Value of d (decimal):", result["d"], "(bin):", bin(result["d"])[2:])
print("Value of w (decimal):", result["w"], "(bin):", bin(result["w"])[2:])