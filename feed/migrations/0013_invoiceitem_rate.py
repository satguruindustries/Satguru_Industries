# Generated by Django 3.1.8 on 2023-08-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_auto_20230805_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
