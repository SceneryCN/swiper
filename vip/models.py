from django.db import models


class Vip(models.Model):
    name = models.CharField(max_length=16, unique=True)
    level = models.IntegerField(unique=True)
    price = models.FloatField()

    class Meta:
        ordering = ['level']

    def permissions(self):
        '''当前 VIP 具有的所有权限'''
        relations = VipPermRelation.objects.filter(vip_id=self.id)
        perm_id_list = [r.perm_id for r in relations]
        return Permission.objects.filter(id__in=perm_id_list)

    def has_perm(self, perm_name):
        '''检查该等级 VIP 是否具有某权限'''
        try:
            perm = Permission.get(name=perm_name)
        except Permission.DoesNotExist:
            return False
        else:
            return VipPermRelation.objects.filter(vip_id=self.id,
                                                  perm_id=perm.id).exists()


class Permission(models.Model):
    name = models.CharField(max_length=32, unique=True)
    desc = models.TextField()


class VipPermRelation(models.Model):
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()
