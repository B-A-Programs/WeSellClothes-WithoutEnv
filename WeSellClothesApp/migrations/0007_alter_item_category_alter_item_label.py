# Generated by Django 4.0.4 on 2022-08-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeSellClothesApp', '0006_alter_ordereditem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Out wear')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('N', 'danger'), ('B', 'primary')], max_length=1, null=True),
        ),
    ]
