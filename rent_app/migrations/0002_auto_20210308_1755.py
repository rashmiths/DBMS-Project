# Generated by Django 3.1.4 on 2021-03-08 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
