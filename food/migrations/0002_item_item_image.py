# Generated by Django 3.0 on 2020-06-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.idfood.co.uk/wp-content/plugins/woocommerce/assets/images/placeholder.png', max_length=500, null=True),
        ),
    ]
