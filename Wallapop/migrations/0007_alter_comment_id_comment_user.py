# Generated by Django 4.2 on 2023-05-20 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Wallapop', '0006_alter_comment_id_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id_comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
