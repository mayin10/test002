# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DmsProjekte(models.Model):
    prjlist = models.CharField(db_column='PRJLIST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gesamt_prio = models.FloatField(db_column='GESAMT_PRIO', blank=True, null=True)  # Field name made lowercase.
    g_prio = models.IntegerField(db_column='G_PRIO', blank=True, null=True)  # Field name made lowercase.
    id_beauftragung = models.FloatField(db_column='ID_BEAUFTRAGUNG', blank=True, null=True)  # Field name made lowercase.
    id_projektart = models.FloatField(db_column='ID_PROJEKTART', blank=True, null=True)  # Field name made lowercase.
    id_sap_prj = models.CharField(db_column='ID_SAP_PRJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zustõndige_region = models.CharField(db_column='ZUST─NDIGE_REGION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tef_standort_nr = models.IntegerField(db_column='TEF_STANDORT_NR', blank=True, null=True)  # Field name made lowercase.
    ne_typ = models.IntegerField(db_column='NE_TYP', blank=True, null=True)  # Field name made lowercase.
    ne_nr = models.IntegerField(db_column='NE_NR', blank=True, null=True)  # Field name made lowercase.
    project_group_name = models.CharField(db_column='PROJECT_GROUP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gu_projekt = models.CharField(db_column='GU_PROJEKT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projekt_id = models.IntegerField(db_column='PROJEKT_ID', blank=True, null=True)  # Field name made lowercase.
    template_bezeichnung = models.CharField(db_column='TEMPLATE_BEZEICHNUNG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projektart = models.CharField(db_column='PROJEKTART', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projektstand = models.CharField(db_column='PROJEKTSTAND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prepac = models.CharField(db_column='PREPAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vkn_gruppe_id = models.IntegerField(db_column='VKN_GRUPPE_ID', blank=True, null=True)  # Field name made lowercase.
    vkn_gruppe_name = models.CharField(db_column='VKN_GRUPPE_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vkn_gruppe_typ = models.CharField(db_column='VKN_GRUPPE_TYP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vkn_gruppe_verknuepfte_projekte = models.CharField(db_column='VKN_GRUPPE_VERKN▄PFTE_PROJEKTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dim_versorgung = models.CharField(db_column='DIM_VERSORGUNG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sap_order_daten = models.TextField(db_column='SAP_ORDER_DATEN', blank=True, null=True)  # Field name made lowercase.
    demand = models.CharField(db_column='DEMAND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dim_beauftragungsform = models.CharField(db_column='DIM_BEAUFTRAGUNGSFORM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gebõudeart = models.CharField(db_column='GEB─UDEART', max_length=255, blank=True, null=True)  # Field name made lowercase.
    site_type = models.CharField(db_column='SITE_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projekt_equipment = models.CharField(db_column='PROJEKT_EQUIPMENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    programm = models.CharField(db_column='PROGRAMM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_st56y_zusatz = models.CharField(db_column='MASTER_ST56Y_ZUSATZ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_st56z_zusatz = models.CharField(db_column='MASTER_ST56Z_ZUSATZ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    layer_service = models.CharField(db_column='LAYER_SERVICE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plz = models.IntegerField(db_column='PLZ', blank=True, null=True)  # Field name made lowercase.
    ort = models.CharField(db_column='ORT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ziel_des_projekts = models.CharField(db_column='ZIEL_DES_PROJEKTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projekt_frequenzflag = models.CharField(db_column='PROJEKT_FREQUENZFLAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dim_squads_mac = models.CharField(db_column='DIM_SQUADS_MAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dim_verzug_ohne_gu_vertretung = models.CharField(db_column='DIM_VERZUG_OHNE_GU_VERTRETUNG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sto_owner = models.CharField(db_column='STO_OWNER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wbst = models.CharField(db_column='WBST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_56y_plan_forecast = models.CharField(db_column='56Y*PLAN_FORECAST', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    strasse = models.CharField(db_column='STRASSE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    site_ok = models.CharField(db_column='SITE_OK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sto_dim_obli_demand_2022 = models.CharField(db_column='STO_DIM_OBLI_DEMAND_2022', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sto_dim_opti_demand = models.CharField(db_column='STO_DIM_OPTI_DEMAND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pmac_obli_demand_2022_rolling = models.CharField(db_column='PMAC_OBLI_DEMAND_2022_ROLLING', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_st56y_zusatz_fc = models.CharField(db_column='MASTER_ST56Y_ZUSATZ_FC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dim_accept_sonderfreigabe_func = models.CharField(db_column='DIM_ACCEPT_SONDERFREIGABE_FUNC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dim_accept_sonderfreigabe_tech = models.CharField(db_column='DIM_ACCEPT_SONDERFREIGABE_TECH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dim_accept_verzug = models.CharField(db_column='DIM_ACCEPT_VERZUG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ast_begruendung = models.CharField(db_column='AST_BEGRUENDUNG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    averzug_begruendung = models.CharField(db_column='AVERZUG_BEGRUENDUNG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nrg_transition = models.CharField(db_column='NRG_TRANSITION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    infrastruktur_soll_baseframe = models.CharField(db_column='INFRASTRUKTUR_SOLL_BASEFRAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dms_projekte'


class DmsStatus(models.Model):
    project_status_id = models.IntegerField(db_column='PROJECT_STATUS_ID', blank=True, null=True)  # Field name made lowercase.
    template_status_id = models.IntegerField(db_column='TEMPLATE_STATUS_ID', blank=True, null=True)  # Field name made lowercase.
    project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
    required = models.TextField(db_column='REQUIRED', blank=True, null=True)  # Field name made lowercase.
    datum_ist = models.DateTimeField(db_column='DATUM_IST', blank=True, null=True)  # Field name made lowercase.
    datum_ist_gesetzt = models.DateTimeField(db_column='DATUM_IST_GESETZT', blank=True, null=True)  # Field name made lowercase.
    datum_plan = models.DateTimeField(db_column='DATUM_PLAN', blank=True, null=True)  # Field name made lowercase.
    datum_plan_gesetzt = models.DateTimeField(db_column='DATUM_PLAN_GESETZT', blank=True, null=True)  # Field name made lowercase.
    datum_soll = models.DateTimeField(db_column='DATUM_SOLL', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    creauser = models.TextField(db_column='CREAUSER', blank=True, null=True)  # Field name made lowercase.
    creadate = models.DateTimeField(db_column='CREADATE', blank=True, null=True)  # Field name made lowercase.
    lastuser = models.TextField(db_column='LASTUSER', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LASTUPDATE', blank=True, null=True)  # Field name made lowercase.
    auto_plan_date = models.IntegerField(db_column='AUTO_PLAN_DATE', blank=True, null=True)  # Field name made lowercase.
    sync_actual_date = models.IntegerField(db_column='SYNC_ACTUAL_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dms_status'


class TblDmsProjectAdditionalData(models.Model):
    baumassnahme_id = models.DecimalField(db_column='BAUMASSNAHME_ID', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bm_verantwortlicher = models.CharField(db_column='BM_VERANTWORTLICHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mitnutzungskoordinator = models.CharField(db_column='MITNUTZUNGSKOORDINATOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tk_gu = models.CharField(db_column='TK_GU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projektleiter = models.CharField(db_column='PROJEKTLEITER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    funkplaner = models.CharField(db_column='FUNKPLANER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bauleiter = models.CharField(db_column='BAULEITER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    akquisiteur = models.CharField(db_column='AKQUISITEUR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    abnahmeverantwortlicher = models.CharField(db_column='ABNAHMEVERANTWORTLICHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creauser = models.CharField(db_column='CREAUSER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    creadate = models.DateTimeField(db_column='CREADATE', blank=True, null=True)  # Field name made lowercase.
    lastuser = models.CharField(db_column='LASTUSER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LASTUPDATE', blank=True, null=True)  # Field name made lowercase.
    incentive = models.DecimalField(db_column='INCENTIVE', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    in_advance = models.DecimalField(db_column='IN_ADVANCE', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pm_su = models.CharField(db_column='PM_SU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order_package = models.CharField(db_column='ORDER_PACKAGE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    integrationskoordinator = models.CharField(db_column='INTEGRATIONSKOORDINATOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arbeitsvorbereitung = models.CharField(db_column='ARBEITSVORBEREITUNG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cityverantwortlicher = models.CharField(db_column='CITYVERANTWORTLICHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sitemanager = models.CharField(db_column='SITEMANAGER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    integrationmanager = models.CharField(db_column='INTEGRATIONMANAGER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    acceptancemanager = models.CharField(db_column='ACCEPTANCEMANAGER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pp_gu_plan = models.CharField(db_column='PP_GU_PLAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pp_gu_ist = models.CharField(db_column='PP_GU_IST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cw_gu_plan = models.CharField(db_column='CW_GU_PLAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bearbeiter_auslieferung = models.CharField(db_column='BEARBEITER_AUSLIEFERUNG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bearbeiter_retoure = models.CharField(db_column='BEARBEITER_RETOURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spoc = models.CharField(db_column='SPOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doku_pruefer = models.CharField(db_column='DOKU_PRUEFER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ia_sitemanger = models.CharField(db_column='IA_SITEMANGER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    funknetzplaner_qualitõt = models.CharField(db_column='FUNKNETZPLANER_QUALIT─T', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transport_qualitõt = models.CharField(db_column='TRANSPORT_QUALIT─T', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_dms_project_additional_data'
