# Generated by Django 4.0.4 on 2022-06-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TayfunBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='TayfunBugraBas', max_length=255),
        ),
    ]