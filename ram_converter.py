ram_input = input("Enter you RAM in gb :")

gb = float(ram_input)
mb = gb * 1024
kb = mb * 1024

print("\n=== CONVERSION RESULTS ===")
print(f"Input: {gb} GB")
print(f"-> Megabytes: {mb} MB")
print(f"-> Kilobytes: {kb} KB")
print(f"-> Bytes: {kb * 1024:,} bytes")