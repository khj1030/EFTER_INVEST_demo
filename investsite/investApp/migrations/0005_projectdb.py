# Generated by Django 4.1.5 on 2023-01-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investApp', '0004_alter_userlogin_user_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectDB',
            fields=[
                ('proj_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'project_id',
            },
        ),
    ]
