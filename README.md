学习使用Django框架，使用数据库为默认sqlite

## 生成requirements.txt文件
pip freeze > requirements.txt
## 安装requirements.txt依赖
pip install -r requirements.txt



Django 教程：
创建项目：django-admin startproject 项目名
进入项目目录
创建应用：python manage.py startapp 应用名

1.使用模型
    a.定义模型类
    b.生成迁移,生成sql脚本：python manage.py makemigrations
    c.执行迁移，根据迁移文件创建表：python manage.py migrate


2.数据库操作命令
    终端执行：python manage.py shell

    创建book=BookInfo()
        book.?=?
        book.save()
    修改：book= BookInfo.objects.get(id=?)
        book.?=?
        book.save()
    删除：book.delete()
    查询：所有 BookInfo.objects.all()
            BookInfo.objects.get(id=?)

注：path与url是两个不同的模块,效果都是响应返回页面, path调用的是python第三方模块或框架,而url则是自定义的模块,如Views下的def函数对应你url中的参数值.
