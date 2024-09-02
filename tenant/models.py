from django.db import models
# tenants will share the same database but they will be separated by the sub-domains


# Create your models here.
class Tenant(models.Model):
  name = models.CharField(max_length=255)
  subdomain = models.CharField(max_length=255)
  
class TenantAwareModel(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
  
class Member(TenantAwareModel):
  name = models.CharField(max_length=255)
    