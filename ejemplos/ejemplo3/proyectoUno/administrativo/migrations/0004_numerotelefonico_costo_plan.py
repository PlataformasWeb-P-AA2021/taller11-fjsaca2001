# Generated by Django 3.2.4 on 2021-06-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0003_auto_20210624_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='numerotelefonico',
            name='costo_plan',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
            preserve_default=False,
        ),
    ]