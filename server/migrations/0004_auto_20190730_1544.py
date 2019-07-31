# Generated by Django 2.2.3 on 2019-07-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20190730_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='protocol',
            field=models.SmallIntegerField(choices=[(0, '其他'), (1, 'ssh'), (2, 'telnet'), (3, 'rdp'), (4, 'vnc'), (5, 'sftp'), (6, 'ftp')], default=1, verbose_name='协议'),
        ),
        migrations.AlterField(
            model_name='remoteuser',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='登陆后是否su跳转超级用户'),
        ),
    ]
