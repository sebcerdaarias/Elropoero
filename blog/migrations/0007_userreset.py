# Generated by Django 2.2.16 on 2020-11-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201119_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='userreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreusuario', models.CharField(max_length=50)),
            ],
        ),
    ]
