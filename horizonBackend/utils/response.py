from rest_framework.response import Response
class RetResponse:
  def __init__(self,code,message,data,rows):
    self.__code = code
    self.__message = message
    self.__data = data
    self.__rows = rows
  @property
  def code(self):
    return self.__code
  @code.setter
  def code(self,val):
    self.__code = val
  @property
  def message(self):
    return self.__message
  @message.setter
  def message(self,val):
    self.__message = val
  @property
  def data(self):
    return self.__data
  @data.setter
  def data(self,val):
    self.__data = val
  @property
  def rows(self):
    return self.__rows
  @rows.setter
  def rows(self,val):
    self.__rows = val

  @staticmethod
  def success(data,rows):
    return Response({
      "code":200,
      "message":"success",
      "data":data,
      "rows":rows
    })

  @staticmethod
  def error(data, rows):
    return Response({
      "code":500,
      "message":"error",
      "data":data,
      "rows":rows
    })
  @staticmethod
  def info(code,message,data,rows):
    return Response({
      "code":code,
      "message":message,
      "data":data,
      "rows":rows
    })