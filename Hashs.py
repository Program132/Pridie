import hashlib
import codecs
import base64


def NTLM_Encode(string):
    utf16le_password = string.encode('utf-16le')
    md4_hash = hashlib.new('md4', utf16le_password).digest()
    ntlm_hash = codecs.encode(md4_hash, 'hex').decode()

    return ntlm_hash


def Base64_Encode(string):
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')


def Base64_Decode(string):
    return base64.b64decode(string).decode('utf-8')


def UTF16_Encode(string):
    return string.encode('utf-16le')


def MD4_Encode(string):
    return hashlib.new('md4', string).digest()