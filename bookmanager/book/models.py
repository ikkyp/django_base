from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=20, verbose_name='名称')


class PeopleInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
