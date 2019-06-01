# Generated by Django 2.1.3 on 2019-05-30 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(allow_unicode=True, max_length=20, unique=True)),
                ('batch', models.CharField(max_length=20)),
                ('problems_added', models.PositiveIntegerField(default=4)),
                ('cut_off', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SheetMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solve_count', models.PositiveIntegerField(default=0)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sheet', to=settings.AUTH_USER_MODEL)),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='sheets.Sheet')),
            ],
        ),
        migrations.AddField(
            model_name='sheet',
            name='members',
            field=models.ManyToManyField(through='sheets.SheetMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='sheetmember',
            unique_together={('sheet', 'member')},
        ),
    ]