from django.shortcuts import render

from .models import Member

from .utilities import get_tenant

# Create your views here.
def our_team(request):
  tenant = get_tenant(request)
  print(f'Tenant: {tenant}')  # Agrega esto para depurar
  members = Member.objects.filter(tenant=tenant)
  print(f'Members: {members}')  # Agrega esto para depurar
  return render(request,'our_team.html', {'tenant':tenant, 'members': members})
  
# def member_detail(request, member_id):
#   tenant = get_tenant(request)
#   member = Member.objects.filter(tenant=tenant, id=member_id).first()
#   return render(request,'member_detail.html', {'member': member})

