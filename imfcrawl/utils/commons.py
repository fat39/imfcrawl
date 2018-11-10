# -*- coding:utf-8 -*-

def hash_sha1(val):
    import hashlib
    ha = hashlib.sha1()
    ha.update(bytes(val, encoding='utf-8'))
    key = ha.hexdigest()
    return key