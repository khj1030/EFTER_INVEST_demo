# Generated by Django 4.1.5 on 2023-01-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='user_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
