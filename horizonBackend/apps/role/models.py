from django.db import models
from apps.user.models import User
# Create your models here.
class Role(models.Model):
  name=models.CharField(max_length=125,unique=True,null=False)
  createTime = models.DateTimeField(auto_now=True)
  users = models.ManyToManyField(User,through="UserRole")
  class Meta:
    db_table="role"

class UserRole(models.Model):
  user_id=models.ForeignKey(User,to_field="user_id",db_column="user_id",on_delete=models.CASCADE)
  role_id=models.ForeignKey(to="Role",to_field="id",db_column="role_id",on_delete=models.CASCADE)
  createTime = models.DateTimeField(auto_now=True)
  class Meta:
    unique_together = (('user_id', 'role_id'),)
    db_table="user_role"