# Generated by Django 4.2.5 on 2023-09-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_alter_product_picture_alter_team_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='picture',
            field=models.ImageField(default=0, upload_to='products'),
        ),
    ]
