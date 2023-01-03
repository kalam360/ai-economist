import os
from Crypto.PublicKey import RSA
file_path = "/media/kalam/anchorblock/github_testing/ai-economist/ai_economist/foundation/scenarios/covid19/key_to_check_activation_code_against"
with open(file_path, 'r') as f:

    key_pair = RSA.import_key(f.read())


print(hex(key_pair.e))