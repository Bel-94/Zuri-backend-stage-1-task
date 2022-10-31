# Generated by Django 4.1.2 on 2022-10-31 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=30)),
                ('backend', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=100)),
            ],
        ),
    ]
