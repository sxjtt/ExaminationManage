# Generated by Django 3.2.3 on 2022-04-21 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_nick_name'),
        ('courses', '0002_subject_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='score',
            field=models.FloatField(verbose_name='分数'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.IntegerField(default=0, verbose_name='0:单选题  1:多选题  2:判断题  3:填空题  4:简答题'),
        ),
        migrations.CreateModel(
            name='StudentRecordingScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=32, verbose_name='学习录屏文件名')),
                ('translate_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.translateclass')),
                ('userprofile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
    ]