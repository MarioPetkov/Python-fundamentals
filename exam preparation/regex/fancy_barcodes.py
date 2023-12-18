import re

def barcode_validator(barcode_data):
    pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
    for barcode in barcode_data:
        valid_barcode = re.fullmatch(pattern, barcode)
        if valid_barcode:
            product_group = ''.join(re.findall(r'\d', barcode))
            product_group = product_group if product_group else "00"
            print(f"Product group: {product_group}")
        else: 
            print("Invalid barcode")
num_barcodes = int(input())
data = [input() for _ in range(num_barcodes)]
barcode_validator(data)