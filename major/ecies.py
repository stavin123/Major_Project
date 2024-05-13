import sslcrypto

# Create curve object
curve = sslcrypto.ecc.get_curve("brainpoolP256r1")

# Generate private key, both compressed and uncompressed keys are supported
private_key = curve.new_private_key(is_compressed=True)

# Find a matching public key
public_key = curve.private_to_public(private_key)
print(private_key)
print(public_key)
# If required, you can change public key format to whatever you want
x, y = curve.decode_public_key(public_key)
electrum_public_key = x + y
# Encrypt something. You can specify a cipher if you want to, aes-256-cbc is the
# default value
data = b"Hello, world!"
ciphertext = curve.encrypt(data, public_key, algo="aes-256-ofb")

# Decrypt
assert curve.decrypt(ciphertext, private_key, algo="aes-256-ofb") == data

