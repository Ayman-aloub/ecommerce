# Generated by Django 4.0.5 on 2022-06-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_homeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='homeimage',
            field=models.FileField(default='E:\\django\\django_projects\\ecomerce\\images\\default.jpg', upload_to='E:\\django\\django_projects\\ecomerce\\images'),
        ),
    ]
