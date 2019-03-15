# Generated by Django 2.0 on 2018-01-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_common_qu_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qu_id', models.CharField(max_length=50)),
                ('qu_title', models.CharField(max_length=50)),
                ('qu_desc', models.CharField(max_length=500)),
                ('solution', models.CharField(max_length=2000)),
                ('event_code', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
