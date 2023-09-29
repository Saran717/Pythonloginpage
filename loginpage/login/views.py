from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
        # res_data=render_to_string("login/login.html")
        return render(request,"login/login.html",{
            "text":res_text, 
            "month_name":month
        })
    except:
        return HttpResponseNotFound("nodata")
    
def mon_sep(request):
    # try:
        months=list(mon_cha.keys())
        return render(request,"login/Allmonth.html",
                      {
                          "months":months
                      })
    # except:
    #     return HttpResponseNotFound("nodata")