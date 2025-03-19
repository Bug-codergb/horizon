import jwt
from datetime import datetime, timedelta,UTC
from django.conf import settings
import os

blacklist = set()
class JsonWebToken:
  def __init__(self,**kwargs):
    self.__token=""
    self.payload={
      "iat": datetime.now(UTC),  # 签发时间
      "exp": datetime.now(UTC) + timedelta(hours=24*7),  # 过期时间
      "sub": kwargs.get("userId"),  # 用户 ID
      "name": kwargs.get("userName"),
    }
  @property
  def token(self):
    return self.__token
  @token.setter
  def tok(self,val):
    self.__token= val

  def sign(self):
    private_key_path = os.path.join(settings.BASE_DIR, "content/private.key")
    with open(private_key_path, "r") as f:
      private_key = f.read()
    token = jwt.encode(self.payload, private_key, algorithm="RS256")
    self.__token = token

  def validate(self,token):
    public_key_path = os.path.join(settings.BASE_DIR, "content/public.key")
    with open(public_key_path, "r") as f:
      public_key = f.read()
    try:
      decoded = jwt.decode(token, public_key, algorithms=["RS256"])
      return None if token in blacklist else decoded
    except jwt.ExpiredSignatureError:
      return None
    except jwt.InvalidTokenError:
      return None