# Generated by Django 4.0.4 on 2022-08-02 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WeSellClothesApp', '0005_alter_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]