# Generated by Django 4.1.4 on 2022-12-13 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_produc_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='description',
        ),
        migrations.AddField(
            model_name='feature',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
