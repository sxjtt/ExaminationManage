# Generated by Django 3.2.3 on 2022-03-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(blank=True, default='朱朱朱', max_length=128, null=True, verbose_name='昵称'),
        ),
    ]
