# Generated by Django 4.1.5 on 2023-01-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investApp', '0005_projectdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdb',
            name='proj_id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
