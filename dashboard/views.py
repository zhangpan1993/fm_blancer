from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext,loader
from django.http import HttpResponse
from fm_balancer.views import is_auth
from nginx.views import *
import json
import time

# Create your views here.

@login_required(login_url="/login/")
def view(request):
    sysinfo = get_sys_info()
    user = {
        'name':request.user,
        'date':time.time()
    }

    return render_to_response('dashboard/view.html',{'sysinfo':sysinfo,'user':user})

@is_auth
def get_status_info(request):
    req_status = get_req_status()
    r_stat = []
    for r in req_status:
        if r[0] == 'zone_name':
            continue
        rs = {
            'req_url':r[1],
            'max_active':r[2],
            'max_bw': r[3],
            'traffic': r[4],
            'requests': r[5],
            'active': r[6],
            'bandwidth': r[7],
            'zone_name': r[0]

        }
        r_stat.append(rs)
    context = {

        'flag':'Success',
        'context':{
            'sysstatus':get_sys_status(),
            'reqstatus':r_stat
        }
    }
    return HttpResponse(json.dumps(context))
