# Generated by Django 2.1.4 on 2018-12-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181229_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', to_field='identy'),
        ),
    ]