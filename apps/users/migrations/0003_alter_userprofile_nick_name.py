# Generated by Django 3.2.3 on 2022-04-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_nick_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(blank=True, default='王菲', max_length=128, null=True, verbose_name='昵称'),
        ),
    ]
