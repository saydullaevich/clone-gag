# Generated by Django 3.2.7 on 2021-09-15 02:56

from django.db import migrations, models
import gag.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Foydalanuvchi', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=gag.helpers.UploadTo('profile')),
        ),
    ]
