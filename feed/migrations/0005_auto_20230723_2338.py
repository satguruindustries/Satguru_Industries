# Generated by Django 3.1.8 on 2023-07-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_post_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ans',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='opt1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='opt2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='opt3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='opt4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='ques',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub',
            field=models.CharField(max_length=255),
        ),
    ]
