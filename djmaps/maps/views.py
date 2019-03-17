from django.shortcuts import render

# Create your views here.

mapbox_access_token = 'pk.eyJ1IjoiamVmZnBlbmciLCJhIjoiY2p0YnppcTZvMHI3dDN5bDhnZGJmYTl3MSJ9.ed_AkRMblXOKMLV42YMvyg'


def default_map(request):
    return render(request, 'default.html', {'mapbox_access_token': mapbox_access_token})
