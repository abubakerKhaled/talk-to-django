# Generated by Django 5.0.9 on 2024-09-20 07:32

import pgvector.django
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='embedding',
            field=pgvector.django.VectorField(blank=True, dimensions=1000, null=True),
        ),
    ]
