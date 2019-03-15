# Generated by Django 2.0 on 2018-01-29 09:36

from django.db import migrations, models
import system.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_attach_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=500)),
                ('image_url', models.ImageField(storage=system.storage.ImageStorage(), upload_to='img/%Y/%m')),
                ('event_id', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_dept_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.CharField(max_length=10)),
                ('dept_name', models.CharField(max_length=50)),
                ('parent_dept_id', models.CharField(max_length=10)),
                ('order', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_event_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=50)),
                ('event_date', models.DateField(max_length=10)),
                ('event_code', models.CharField(max_length=10)),
                ('event_level_code', models.CharField(max_length=10)),
                ('event_state_code', models.CharField(max_length=10)),
                ('event_desc', models.CharField(max_length=500)),
                ('user_id', models.CharField(max_length=20)),
                ('contact_name', models.CharField(max_length=20)),
                ('contact_mobile', models.CharField(max_length=20)),
                ('processor_id', models.CharField(max_length=20)),
                ('process_desc', models.CharField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_event_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_code', models.CharField(max_length=10)),
                ('event_name', models.CharField(max_length=50)),
                ('event_code_state', models.CharField(max_length=1)),
                ('department_id', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
                ('parent_event_code', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_notice_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_id', models.CharField(max_length=50)),
                ('notice_title', models.CharField(max_length=50)),
                ('notice_summary', models.CharField(max_length=100)),
                ('notice_author', models.CharField(max_length=20)),
                ('notice_content', models.CharField(max_length=2000)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_sys_param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_name', models.CharField(max_length=50)),
                ('param_key', models.CharField(max_length=50)),
                ('param_value', models.CharField(max_length=500)),
                ('param_desc', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_dept_id', models.CharField(max_length=100)),
                ('user_position', models.CharField(max_length=50)),
                ('user_mobile', models.CharField(max_length=20)),
                ('user_gender', models.CharField(max_length=1)),
                ('user_email', models.CharField(max_length=100)),
                ('user_avatar', models.CharField(max_length=500)),
                ('user_status', models.CharField(max_length=1)),
                ('isleader', models.CharField(max_length=1)),
                ('extattr', models.CharField(max_length=500)),
                ('user_eng_name', models.CharField(max_length=50)),
                ('user_tel', models.CharField(max_length=20)),
                ('enable', models.CharField(max_length=1)),
                ('hide_mobile', models.CharField(max_length=20)),
                ('order', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]