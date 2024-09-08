# Generated by Django 3.1.8 on 2023-09-14 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0016_auto_20230903_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.product')),
            ],
        ),
    ]