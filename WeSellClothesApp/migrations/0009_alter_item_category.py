# Generated by Django 4.0.4 on 2022-08-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeSellClothesApp', '0008_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirts'), ('SW', 'Sport wear'), ('OW', 'Out wear')], max_length=2, null=True),
        ),
    ]
