# Generated by Django 4.2.5 on 2023-09-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('picture', models.ImageField(default=0, upload_to='jeehWebsite/static/images')),
                ('description', models.TextField(max_length=500)),
                ('model', models.CharField(blank=True, choices=[('T', 'Toyota'), ('V', 'Volkswagen Group'), ('G', 'General Motors'), ('F', 'Ford Motor Company'), ('H', 'Honda'), ('N', 'Nissan'), ('HY', 'Hyundai Motor Group'), ('BM', 'BMW Group'), ('MB', 'Mercedes-Benz'), ('TSLA', 'Tesla, Inc.'), ('FCA', 'Fiat Chrysler Automobiles (now part of Stellantis)'), ('ST', 'Stellantis (formed by the merger of FCA and PSA Group)'), ('SU', 'Subaru (a division of Subaru Corporation)'), ('K', 'Kia Motors Corporation'), ('M', 'Mazda'), ('RG', 'Renault Group (part of the Renault-Nissan-Mitsubishi Alliance)'), ('MM', 'Mitsubishi Motors (part of the Renault-Nissan-Mitsubishi Alliance)'), ('VC', 'Volvo Cars (owned by Geely Holding Group)'), ('TM', 'Tata Motors'), ('SAIC', 'SAIC Motor Corporation'), ('GH', 'Geely Holding Group'), ('BYD', 'BYD Auto'), ('CA', 'Changan Automobile'), ('GW', 'Great Wall Motors'), ('DMC', 'Dongfeng Motor Corporation'), ('SMC', 'Suzuki Motor Corporation')], default='Toyota', max_length=5)),
                ('product_date', models.DateField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('Price', models.FloatField(default=0, max_length=10)),
                ('fuel_efficiency_city', models.DecimalField(decimal_places=1, default=0.0, max_digits=4)),
                ('fuel_efficiency_highway', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('horsepower', models.IntegerField(blank=True, default=135)),
                ('key_features', models.TextField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Position', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('picture', models.ImageField(default=0, upload_to='products')),
                ('facebook_link', models.URLField(default='')),
                ('twitter_link', models.URLField(default='')),
                ('instagram_link', models.URLField(default='')),
                ('youtube_link', models.URLField(default='')),
            ],
            options={
                'ordering': ['Id', 'Position'],
            },
        ),
        migrations.CreateModel(
            name='Testominals',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Testominalstext', models.TextField(max_length=500)),
                ('picture', models.ImageField(default=0, upload_to='products')),
                ('position', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['Id', 'Firstname'],
            },
        ),
    ]
