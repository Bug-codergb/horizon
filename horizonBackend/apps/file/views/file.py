from rest_framework.views import APIView
from utils.response import RetResponse
from apps.file.models import File
from django.conf import settings
from utils.general import getFileSuffix,generateID,getStrMD5
import os
class UploadView(APIView):
  def post(self,request):
    file_obj= request.data.get("file")
    #获取文件基本信息
    file_size = file_obj.size
    file_content_type = file_obj.content_type
    file_name = file_obj.name

    dir=getStrMD5(file_content_type)
    #创建文件夹
    upload_dir = os.path.join(settings.MEDIA_ROOT, dir)
    os.makedirs(upload_dir, exist_ok=True)

    suffix = getFileSuffix(file_name)
    unique = generateID()
    file_unique_name = str(unique)+suffix

    file_url = settings.MEDIA_URL+dir+"/"+file_unique_name
    try:
      file_path = os.path.join(upload_dir, file_unique_name)
      with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
          destination.write(chunk)

      File.objects.create(url=file_url,
                          originalname=file_name,
                          type=file_content_type,
                          dest=settings.RELATIVE_MEDIA_PATH+"/"+dir,
                          size=file_size,
                          filename=file_unique_name
                          )
    except Exception as e:
      print(e)
      return RetResponse.error(None,None)
    return RetResponse.success(None,None)

class DeleteFileView(APIView):
  def post(self,request,id):
    ret = File.objects.filter(id=id)
    length = len(ret)
    try:
      if length != 0:
        item = ret.values("dest", "filename")[0]
        file_path = os.path.join(item["dest"], item['filename'])
        full_path = os.path.join(settings.BASE_DIR, file_path)
        if os.path.exists(full_path):
          os.remove(full_path)
    except Exception as e:
      print(e)
    finally:
      ret.delete()
    return RetResponse.success(None,None)