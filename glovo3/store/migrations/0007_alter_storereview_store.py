# Generated by Django 5.1.3 on 2024-12-01 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_storereview_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storereview',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='store.store'),
        ),
    ]
