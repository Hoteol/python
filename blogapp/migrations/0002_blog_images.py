# Generated by Django 3.0.7 on 2020-07-01 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
