# Generated by Django 2.0.4 on 2018-04-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analysis', '0002_delete_hotlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_generated', models.IntegerField(blank=True, null=True)),
                ('text', models.CharField(max_length=1000)),
                ('number', models.CharField(max_length=1000)),
                ('mms', models.BooleanField()),
                ('sender', models.BooleanField()),
                ('datetime', models.CharField(max_length=1000)),
                ('timestamp_client', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
