# Generated by Django 3.2.4 on 2021-06-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='area',
            field=models.CharField(choices=[('46,5', '46,5'), ('43,5', '43,5'), ('49,2', '49,2'), ('43,8', '43,8'), ('72,1', '72,1'), ('72,4', '72,4'), ('100,1', '100,1'), ('93,2', '93,2')], default=0, max_length=6),
            preserve_default=False,
        ),
    ]
