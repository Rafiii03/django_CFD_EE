# Generated by Django 3.1.7 on 2021-03-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FraudDetectCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Filename', models.CharField(max_length=100)),
                ('Percentage', models.FloatField(max_length=50)),
                ('FalsePos', models.IntegerField(max_length=50)),
                ('Suspicious', models.IntegerField(max_length=50)),
                ('NewCust', models.IntegerField(max_length=50)),
            ],
        ),
    ]
