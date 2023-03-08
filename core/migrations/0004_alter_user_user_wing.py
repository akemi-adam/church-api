# Generated by Django 4.1.7 on 2023-03-08 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230308_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_wing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wing_user_set', to='core.wing', verbose_name='Wing'),
        ),
    ]
