# Generated by Django 4.0.4 on 2022-04-19 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djeet', '0002_alter_djeet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djeet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='djeets', to=settings.AUTH_USER_MODEL),
        ),
    ]