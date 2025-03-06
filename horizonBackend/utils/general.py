import time
import hashlib
def generateID():
  return int(time.time() * 1000)

def getFileSuffix(str):
  index = str.rfind(".")
  return str[index:]
def getStrMD5(s):
  md5_hash = hashlib.md5()
  # 更新哈希对象（需要将字符串编码为字节）
  md5_hash.update(s.encode('utf-8'))
  # 获取十六进制格式的哈希值
  md5_hex = md5_hash.hexdigest()
  return md5_hex
