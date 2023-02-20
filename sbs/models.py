
from django.db import models


class TblSbsDms(models.Model):
    vendor = models.CharField(db_column='VENDOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    site_id = models.CharField(db_column='SITE_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projekt_id = models.IntegerField(db_column='PROJEKT_ID', blank=True, null=True)  # Field name made lowercase.
    doku_container_id = models.IntegerField(db_column='DOKU_CONTAINER_ID', blank=True, null=True)  # Field name made lowercase.
    flag_indms = models.SmallIntegerField(db_column='FLAG_INDMS', blank=True, null=True)  # Field name made lowercase.
    flag_indms_user = models.CharField(db_column='FLAG_INDMS_USER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flag_indmsdate = models.DateTimeField(db_column='FLAG_INDMSDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sbs_dms'
