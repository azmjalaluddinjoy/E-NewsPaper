# Generated by Django 2.1.2 on 2018-11-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]