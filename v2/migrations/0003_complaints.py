# Generated by Django 2.1.4 on 2019-01-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v2', '0002_fooddata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('complain', models.CharField(max_length=1000)),
            ],
        ),
    ]