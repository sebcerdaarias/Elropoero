# Generated by Django 2.2.16 on 2020-11-17 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
