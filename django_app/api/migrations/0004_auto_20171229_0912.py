# Generated by Django 2.0 on 2017-12-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171209_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='sns',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=140, unique=True),
        ),
    ]
