
base = 31694
key_number = (base * 7919 + 12345) % 100000000
answer = str(key_number).zfill(8)
print(f"Calculated answer: {answer}")
