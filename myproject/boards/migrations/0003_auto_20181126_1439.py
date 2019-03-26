# Generated by Django 2.1.3 on 2018-11-26 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20181126_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='boards.Board'),
        ),
    ]
