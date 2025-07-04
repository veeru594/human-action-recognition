# Generated by Django 2.2 on 2021-09-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('login_user', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('actions', models.CharField(max_length=100)),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'UserActions',
            },
        ),
    ]
