# Generated by Django 3.1.3 on 2020-11-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='my_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
