# Generated by Django 5.1 on 2024-10-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materia',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('creditos', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
