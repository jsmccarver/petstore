# Generated by Django 4.0.1 on 2022-04-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_topic_pet_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
