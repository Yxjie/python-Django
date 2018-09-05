from django.db import models

# Create your models here.
'''
1.创建模型类 继承 models.Model
2.终端命令行生成迁移文件：python manage.py makemigrations
3.终端执行迁移命令： python manage.py migrate
'''


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name
