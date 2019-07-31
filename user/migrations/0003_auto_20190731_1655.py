# Generated by Django 2.2.3 on 2019-07-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190729_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginlog',
            name='event_type',
            field=models.SmallIntegerField(choices=[(0, '其他'), (1, '登陆'), (2, '退出'), (3, '登陆错误'), (4, '修改密码失败'), (5, '修改密码成功'), (6, '添加用户'), (7, '删除用户'), (8, '添加用户组'), (9, '删除用户组'), (10, '更新用户'), (11, '更新用户组'), (12, '添加主机'), (13, '删除主机'), (14, '更新主机'), (15, '添加主机账号'), (16, '删除主机账号'), (17, '更新主机账号')], default=1, verbose_name='事件类型'),
        ),
    ]
