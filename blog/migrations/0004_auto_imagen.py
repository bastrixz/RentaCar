# Generated by Django 2.2.6 on 2019-11-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_auto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='imagen',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]