# Generated by Django 3.0.8 on 2020-07-16 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200716_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='facebook',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='course',
            name='branches',
        ),
        migrations.RemoveField(
            model_name='course',
            name='contacts',
        ),
        migrations.AddField(
            model_name='branch',
            name='branches',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='api.Course'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contacts',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='api.Course'),
        ),
        migrations.AddField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[(1, 'Facebook'), (2, 'Phone'), (3, 'Email')], default=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
    ]