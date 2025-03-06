from django.contrib import admin

# Register your models here.
from rest_framework import pagination
from rest_framework.response import Response
class CustomPageNumberPagination(pagination.PageNumberPagination):
  page_size=5
  page_size_query_param="page_size"
  page_query_param="page_num"
  def paginate_queryset(self, queryset, request, view=None):
        """
        重写 paginate_queryset 方法，当页码超出范围时返回空列表。
        """
        try:
            return super().paginate_queryset(queryset, request, view)
        except pagination.NotFound:
            return []  # 返回空列表
  def get_paginated_response(self, data):
        try:
          if self.page is None:
               # 如果页码超出范围，返回空列表和默认的分页信息
              return Response({
                'count': 0,  # 总记录数为 0
                'next': None,
                'previous': None,
                'results': data,  # 空列表
              })
          else:
             # 正常分页情况
              return Response({
                'count': self.page.paginator.count,
                'next': None,
                'previous':None,
                 'rows': data,
              })
        except AttributeError as r:
           return Response({
                'count': 0,  # 总记录数为 0
                'next': None,
                'previous': None,
                'rows': data,  # 空列表
              })
