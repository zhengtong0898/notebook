# Generated by Django 3.1.7 on 2021-03-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('tags', models.CharField(max_length=100, verbose_name='文章标签, 用空格分隔')),
                ('author', models.CharField(max_length=50, verbose_name='文章作者')),
                ('date_joined', models.DateTimeField(verbose_name='发布时间')),
                ('date_changed', models.DateTimeField(verbose_name='最后一次')),
            ],
        ),
    ]
