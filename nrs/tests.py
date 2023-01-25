from nrs.models import  DmsProjekte

for p in DmsProjekte.objects.raw('SELECT * FROM dms_projekte'): # django默认的表名是app名加类名
    print(p)
