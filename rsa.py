from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import xml.etree.ElementTree as ET
import base64


def int_to_string_decode(input):
    modulus_bytes = input.to_bytes((input.bit_length() + 7) // 8, 'big')
    return base64.b64encode(modulus_bytes).decode('utf-8')



# Your private key in PEM format
private_key_pem = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCz8mX2easUuFid
GdJ/bEldErNNNtdnaRzr76J2eRHKl3zs5n8ZPg2FUL/A1QZl2p53bGgwI37/PRIk
CrLOlg0/jTj7Y4IYSFdATOIjwT2Y3s6oWQZWn42RgUp/NKeetCl5KcwdyUZC1wXQ
hUmhCr4CJ75H2geji9H/dazDjWsICdEE9RhifSladsX/3j/tNYL3fi+srFlSdIFX
oNUPFZvhnupfeqAI17kY9jtHr5pfJGnxv0LkNFVl2vrzTN/ZbIrxi2bedoYZkk7w
Rb8qE4R47ElVm/T00YOfcY3UXOCrU81cRwtb3kRKfvsRblZmV5BMbCnFKfGLH2W9
C1Sqoe2TAgMBAAECggEAE83U+ZVWW3IWaTkoTixwE+A0/4XORcFEakBLVFfqugMw
v9nLmc7sf1mYYPPmP7DEc/GTCIk/jCj/0BulUNB5e3RiwGKpNLGcI1AoKzXfPkMh
4gE6OK+tTZrkb1ovgGs6N+1+W2DawgxsGruF6PAHuAZWY2NUJ+RWzj34hOURfHwj
YvRmMkaQNqRj2pr8vghxxLX0yvRuM2KpMH1ysZSivwsgIct56256lELOLOKk1RPS
dEor/W679z+LtDND19odxltmKLupqRPT5DerU4QNTf++UEQyUtW1+wjwJSiksOoK
CpT7Kxd5jP20H8oPD8scGh+WOc/0SLmGr0s/IIA7sQKBgQDm6q8i2Mr+xaUe3I/k
pKSmXgeCzsWcJc4PHohsizBN6bZd6d/fWurTiTdbCdQLQ4LbIGFbZKdfhulOR8ny
yZHcxZRWZZh83tLvVlHuCer4LQhaF439//OiD7GQn7hZSmMFaNLhwFbvIpkvmQDK
hJzwD5J6jwkXF61jJB33rM2+hQKBgQDHflkJiDOy5zBaxMsmXM1ZWi1jROHxHoRa
NmYerTvHIS36kt1fHLJzdduD5kdlqXA3JVhPY4heIGkiWbl9Ph1xvuN6PKdWyolX
mhwnPLeIUcTIvm1HOp8Nkfcafu/x9+b/lQeJ7uolddHU7fmARNfmTf4ioflDZE7w
tBHuDIuzNwKBgQDEJMynGOc1CcV8NXW0jXWeK3jNz71jKWmixhizundJdyAFHcef
/aZCEOgIWIzZFHtujk6kRxc0uXAroicUJ8vSb7HUwW+JgexCiFwHij0gmX/ipudh
vavBGPuHEWSR0/HQgn2+bJZrgkQEfj6Bx6tW7qNJn33lM6N/9wnNe+c30QKBgGWS
VxMbXfdA7sXIXQbzSTqtR167u65gs1KbT/NekIkaw6ZJEJ1UpydSYqoNnVyNoKzz
PrttGgmSxvTOajryXVuErZ2XNDxkcvk/ZgY0S94EhAURr+IMXt8x6nZ7GwBAEEUh
Q+1ez6izDFs1r0s3whVosHRBtAA0Gl1D0b06dgaRAoGAaW/wX+ApsQUU3SKscLEe
fLDTc1a5P6cylPqI+/zxsiWu1aPwsDH02nJhrnhBX5cGH6hAEGx7rbbKhOWPJ4Fi
VPtG6IHipq2SFDCFDea/AeaX7UCEooUSJMwkU5NAB5md2roOLTbat54wvu6P9LQ4
ShyoLQfWVBYpaFF4W2RPozk=
-----END PRIVATE KEY-----
"""

# Load private key from PEM format
private_key = serialization.load_pem_private_key(
    private_key_pem.encode("utf-8"),
    password=None,
    backend=default_backend()
)

# Get the RSA public key parameters
public_key_parameters = private_key.public_key().public_numbers()

# Print the RSA public key parameters
print(f"Modulus: {public_key_parameters.n}")
print(f"Exponent: {public_key_parameters.e}")

# Get the RSA private key parameters
private_key_parameters = private_key.private_numbers()

# Print the additional RSA private key parameters
print(f"D: {private_key_parameters.d}")
print(f"P: {private_key_parameters.p}")
print(f"Q: {private_key_parameters.q}")
print(f"DP: {private_key_parameters.dmp1}")
print(f"DQ: {private_key_parameters.dmq1}")
print(f"InverseQ: {private_key_parameters.iqmp}")

modulus = public_key_parameters.n
exponent = public_key_parameters.e
d = private_key_parameters.d
p = private_key_parameters.p
q = private_key_parameters.q
dp = private_key_parameters.dmp1
dq = private_key_parameters.dmq1
inverse_q = private_key_parameters.iqmp

# Create an XML element tree
root = ET.Element("RSAParameters")

# Add child elements for each parameter
ET.SubElement(root, "Modulus").text = int_to_string_decode(modulus)
ET.SubElement(root, "Exponent").text = int_to_string_decode(exponent)
ET.SubElement(root, "D").text = int_to_string_decode(d)
ET.SubElement(root, "P").text = int_to_string_decode(p)
ET.SubElement(root, "Q").text = int_to_string_decode(q)
ET.SubElement(root, "DP").text = int_to_string_decode(dp)
ET.SubElement(root, "DQ").text = int_to_string_decode(dq)
ET.SubElement(root, "InverseQ").text = int_to_string_decode(inverse_q)

# Create an ElementTree object and write to an XML file
tree = ET.ElementTree(root)
with open("rsa_parameters.xml", "wb") as file:
    tree.write(file)
