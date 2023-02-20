# Generated by Django 4.1.3 on 2023-02-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblSbsDms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(blank=True, db_column='VENDOR', max_length=255, null=True)),
                ('site_id', models.CharField(blank=True, db_column='SITE_ID', max_length=255, null=True)),
                ('projekt_id', models.IntegerField(blank=True, db_column='PROJEKT_ID', null=True)),
                ('doku_container_id', models.IntegerField(blank=True, db_column='DOKU_CONTAINER_ID', null=True)),
                ('flag_indms', models.SmallIntegerField(blank=True, db_column='FLAG_INDMS', null=True)),
                ('flag_indms_user', models.CharField(blank=True, db_column='FLAG_INDMS_USER', max_length=255, null=True)),
                ('flag_indmsdate', models.DateTimeField(blank=True, db_column='FLAG_INDMSDATE', null=True)),
            ],
            options={
                'db_table': 'tbl_sbs_dms',
                'managed': False,
            },
        ),
    ]