from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

mon_cha ={
    "jan": "month1",
    "feb": "month2"

}

def index(request):
    list_item = ""
    months=list(mon_cha.keys())
    for month in months:
        month_path= reverse("monthly_chal",args=[month])
        list_item += f"<li><a href=\"{month_path}\">{month}</a></li>"
        res_data= f"<ul>{list_item}</ul>"
    return HttpResponse(res_data)


def mon_chall_num(request,month):
    months=list(mon_cha.keys())
    if month>len(months):
         return HttpResponse("Not a month")
    red_mon= months[month - 1]
    red_path = reverse("monthly_chal",args=[red_mon])
    return HttpResponseRedirect(red_path)

       

def mon_chall(request,month):
    try:
        res_text = mon_cha[month]
        return HttpResponse(res_text)
    except:
        return HttpResponseNotFound("nodata")
    