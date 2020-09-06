#!/usr/bin/python
import binascii
import hashlib
import sys
from ecdsa import numbertheory, util
from ecdsa import VerifyingKey, SigningKey
from os.path import commonprefix
from binascii import hexlify, unhexlify

# Badge version info:
# Firmware Digest: c8c366901c1b6b16dc1f18c026a9010f4140888a67e57bbcef595fb2a5e6f8b7
# Firmware Signature: 5e360eb8b0a077f39482c0ffed76cdaed812db64a9c0a22da0d9953605858011a6282ba0728b828221cbc4ed38ab3f351666be302c7897e22cc0da3cfbc2b72d
# Partition Table Digest: c4682ef52a5d54fc66b2a898e83218821d5af26df00d3da6568ad3c4ba4dabd7
# Partition Table Signature: 5e360eb8b0a077f39482c0ffed76cdaed812db64a9c0a22da0d9953605858011256ea3cee22f9f9549538b277149b691ba706b576db7e14b3acc13f260ce6c40
# Bootloader PubKey:
# -----BEGIN PUBLIC KEY-----
# MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE5UQ/BT52Hda1iGUfrgifjNykXpLD
# YRY3hSNrqYODGQOfWHbOP8NeN2KMlRazbg92viuDiKnx8Z/ngvWMqi85Og==
# -----END PUBLIC KEY-----


PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE5UQ/BT52Hda1iGUfrgifjNykXpLD
YRY3hSNrqYODGQOfWHbOP8NeN2KMlRazbg92viuDiKnx8Z/ngvWMqi85Og==
-----END PUBLIC KEY----
"""

PRIVATE_DER_FILE = "private.der"

vk = VerifyingKey.from_pem(PUBLIC_KEY.strip())

# Firmware Digest: 
msg1_sha256 = 'c8c366901c1b6b16dc1f18c026a9010f4140888a67e57bbcef595fb2a5e6f8b7'
# Firmware Signature: 
sig1 = '5e360eb8b0a077f39482c0ffed76cdaed812db64a9c0a22da0d9953605858011a6282ba0728b828221cbc4ed38ab3f351666be302c7897e22cc0da3cfbc2b72d'
# Partition Table Digest: 
msg2_sha256 = 'c4682ef52a5d54fc66b2a898e83218821d5af26df00d3da6568ad3c4ba4dabd7'
# Partition Table Signature: 
sig2 = '5e360eb8b0a077f39482c0ffed76cdaed812db64a9c0a22da0d9953605858011256ea3cee22f9f9549538b277149b691ba706b576db7e14b3acc13f260ce6c40'

res = commonprefix( (sig1, sig2) )
prefix = len(res)
print('common prefix len = %s' % prefix)

r  = int(sig1[:prefix], 16)
s1 = int(sig1[prefix:], 16)
s2 = int(sig2[prefix:], 16)
z1 = int(msg1_sha256, 16)
z2 = int(msg2_sha256, 16)

k = (z1 - z2) * numbertheory.inverse_mod(s1 - s2, vk.pubkey.order) % vk.pubkey.order
d = (s1 * k - z1) * numbertheory.inverse_mod(r, vk.pubkey.order) % vk.pubkey.order

sk = SigningKey.from_secret_exponent(d, curve=vk.curve, hashfunc=hashlib.sha256)

pem = sk.to_pem()
print("PEM:\n{}\n".format(pem.decode()))

der = sk.to_der()

with open(PRIVATE_DER_FILE, "wb+") as file:
  file.write(der)
print("DER key writed to: {}\n".format(PRIVATE_DER_FILE))

der_hex = hexlify(der)
print("DER HEX:\n{}\n".format(der_hex))
print("SHA256(DER):\n{}\n".format(hashlib.sha256(der).hexdigest()))
print("SHA256(DER_HEX):\n{}\n".format(hashlib.sha256(der_hex).hexdigest()))
