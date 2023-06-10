from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import center, owner, registration, inspection
from django.utils import timezone


def center1(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def center_list(request):
    centers = center.objects.all()
    # centers_dict = centers.values()
    # print(centers)
    # return render(request, 'centers.html', {'centers': centers})
    data = list(centers.values())
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def owner_list(request):
    owners = owner.objects.all()
    # centers_dict = centers.values()
    # print(centers)
    # return render(request, 'owners.html', {'owners': owners})
    data = list(owners.values())
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def registration_list(request):
    registrations = registration.objects.all()
    # Chuyển đổi QuerySet thành danh sách các đối tượng dict
    data = list(registrations.values())
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def inspection_list(request):
    inspections = inspection.objects.all()
    data = list(inspections.values())
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def month_center(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for val in center_list:
        data_list = []
        for i in range(1, 13):
            count = 0
            List_car = []
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    monthis = dat.insp_date.month
                    if i == monthis:
                        count += 1
                        List_car.append(dat.reg_id.id)
            data_list.append(
                {'monthly': i, 'count': count, 'List_car': List_car})
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def quarter_center(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for val in center_list:
        data_list = []
        for i in range(1, 5):
            count = 0
            List_car = []
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    quarteris =  dat.insp_date.month
                    if (i + (i - 1) * 2 <= quarteris) & (quarteris <= i * 3):
                        count += 1
                        List_car.append(dat.reg_id.id)
            data_list.append(
                {'quarter': i, 'count': count, 'List_car': List_car})
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def year_center(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for val in center_list:
        data_list = []
        for i in range(2010, 2024):
            count = 0
            List_car = []
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    yearis = dat.insp_date.year
                    if i == yearis:
                        count += 1
                        List_car.append(dat.reg_id.id)
            data_list.append(
                {'year': i, 'count': count, 'List_car': List_car})
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def month_Area(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for AREA in range(3):
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        data_list = []
        for i in range(1, 13):
            count = 0
            List_car = []
            for val in center_list:
                # print(val.id)
                if val.region == nameA :
                    
                    for dat in inspection_list:
                        # print(dat.center_id)
                        if val.id == dat.center_id.id:
                            monthis = dat.insp_date.month
                            # print(monthis)
                            if i == monthis:
                                count += 1
                                List_car.append(dat.reg_id.id)
            data_list.append(
                        {'monthly': i, 'count': count, 'List_car': List_car})        
        Res.append({"Area": nameA, "Ds": data_list})   
        data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def quarter_Area(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for AREA in range(3):
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        data_list = []
        for i in range(1, 5):
            count = 0
            List_car = []
            for val in center_list:
                # print(val.id)
                if val.region == nameA :
                    
                    for dat in inspection_list:
                        # print(dat.center_id)
                        if val.id == dat.center_id.id:
                            quarteris =  dat.insp_date.month
                            if (i + (i - 1) * 2 <= quarteris) & (quarteris <= i * 3):
                                count += 1
                                List_car.append(dat.reg_id.id)
            data_list.append(
                        {'quarter': i, 'count': count, 'List_car': List_car})        
        Res.append({"Area": nameA, "Ds": data_list})   
        data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})



def year_Area(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for AREA in range(3):
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        data_list = []
        for i in range(2014, 2024):
            count = 0
            List_car = []
            for val in center_list:
                # print(val.id)
                if val.region == nameA :
                    
                    for dat in inspection_list:
                        # print(dat.center_id)
                        if val.id == dat.center_id.id:
                            yearis = dat.insp_date.year
                            if i == yearis:
                                count += 1
                                List_car.append(dat.reg_id.id)
            data_list.append(
                        {'year': i, 'count': count, 'List_car': List_car})        
        Res.append({"Area": nameA, "Ds": data_list})   
        data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def month_Country(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    data_list = []
    for i in range(1, 13):
        count = 0
        List_car = []
        for val in center_list:
            # print(val.id)
                for dat in inspection_list:
                    # print(dat.center_id)
                    if val.id == dat.center_id.id:
                        monthis = dat.insp_date.month
                        # print(monthis)
                        if i == monthis:
                            count += 1
                            List_car.append(dat.reg_id.id)
        data_list.append(
                    {'monthly': i, 'count': count, 'List_car': List_car})        
    Res.append({"Ds": data_list})   
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def quarter_Country(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    data_list = []
    for i in range(1, 5):
        count = 0
        List_car = []
        for val in center_list:
            # print(val.id)
                for dat in inspection_list:
                    # print(dat.center_id)
                    if val.id == dat.center_id.id:
                        quarteris =  dat.insp_date.month
                        if (i + (i - 1) * 2 <= quarteris) & (quarteris <= i * 3):
                            count += 1
                            List_car.append(dat.reg_id.id)
        data_list.append(
                    {'quarter': i, 'count': count, 'List_car': List_car})        
    Res.append({"Ds": data_list})   
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})



def year_Country(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
  
    data_list = []
    for i in range(2014, 2024):
        count = 0
        List_car = []
        for val in center_list:
            # print(val.id)
                for dat in inspection_list:
                    # print(dat.center_id)
                    if val.id == dat.center_id.id:
                        yearis = dat.insp_date.year
                        if i == yearis:
                            count += 1
                            List_car.append(dat.reg_id.id)
        data_list.append(
                    {'year': i, 'count': count, 'List_car': List_car})        
    Res.append({"Ds": data_list})   
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def expired_month_center(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    
    for val in center_list:
        data_list = []
        count = 0
        List_car = []
        for dat in inspection_list:
            if val.id == dat.center_id.id:
                monthis = dat.exp_date.month
                yearis = dat.exp_date.year
                current_month = timezone.now().month
                current_year = timezone.now().year
                if (monthis == current_month) & (yearis == current_year) :
                    count += 1
                    List_car.append(dat.reg_id.id)
        data_list.append(
            {'count': count, 'List_car': List_car})
        
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def expired_month_Area(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    # print(timezone.now().month, ' ', timezone.now().year)
    for AREA in range(3):
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        data_list = []
        count = 0
        List_car = []
        for val in center_list:
            if val.region == nameA:   
                for dat in inspection_list:
                    if val.id == dat.center_id.id:
                        monthis = dat.exp_date.month
                        yearis = dat.exp_date.year
                        current_month = timezone.now().month
                        current_year = timezone.now().year
                        # if (monthis == current_month) & (yearis == current_year) :
                        #     print(monthis, ' ', yearis)
                        if (monthis == current_month) & (yearis == current_year) :
                            # print(monthis, ' ', yearis)
                            count += 1
                            List_car.append(dat.reg_id.id)

        data_list.append(
            {'count': count, 'List_car': List_car})
            
        Res.append({"Area": nameA, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def expired_month_Country(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    # print(timezone.now().month, ' ', timezone.now().year)
   
    data_list = []
    count = 0
    List_car = []
    for val in center_list:
        
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    monthis = dat.exp_date.month
                    yearis = dat.exp_date.year
                    current_month = timezone.now().month
                    current_year = timezone.now().year
                    # if (monthis == current_month) & (yearis == current_year) :
                    #     print(monthis, ' ', yearis)
                    if (monthis == current_month) & (yearis == current_year) :
                        # print(monthis, ' ', yearis)
                        count += 1
                        List_car.append(dat.reg_id.id)

    data_list.append(
        {'count': count, 'List_car': List_car})
        
    Res.append({"Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def expired_month_center(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    
    for val in center_list:
        data_list = []
        count = 0
        List_car = []
        for dat in inspection_list:
            if val.id == dat.center_id.id:
                monthis = dat.exp_date.month
                yearis = dat.exp_date.year
                current_month = timezone.now().month
                current_year = timezone.now().year
                if (monthis == current_month) & (yearis == current_year) :
                    count += 1
                    List_car.append(dat.reg_id.id)
        data_list.append(
            {'count': count, 'List_car': List_car})
        
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def expired_month_Area(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    # print(timezone.now().month, ' ', timezone.now().year)
    for AREA in range(3):
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        data_list = []
        count = 0
        List_car = []
        for val in center_list:
            if val.region == nameA:   
                for dat in inspection_list:
                    if val.id == dat.center_id.id:
                        monthis = dat.exp_date.month
                        yearis = dat.exp_date.year
                        current_month = timezone.now().month
                        current_year = timezone.now().year
                        # if (monthis == current_month) & (yearis == current_year) :
                        #     print(monthis, ' ', yearis)
                        if (monthis == current_month) & (yearis == current_year) :
                            # print(monthis, ' ', yearis)
                            count += 1
                            List_car.append(dat.reg_id.id)

        data_list.append(
            {'count': count, 'List_car': List_car})
            
        Res.append({"Area": nameA, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def expired_month_Country(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    # print(timezone.now().month, ' ', timezone.now().year)
   
    data_list = []
    count = 0
    List_car = []
    for val in center_list:
        
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    monthis = dat.exp_date.month
                    yearis = dat.exp_date.year
                    current_month = timezone.now().month
                    current_year = timezone.now().year
                    # if (monthis == current_month) & (yearis == current_year) :
                    #     print(monthis, ' ', yearis)
                    if (monthis == current_month) & (yearis == current_year) :
                        # print(monthis, ' ', yearis)
                        count += 1
                        List_car.append(dat.reg_id.id)

    data_list.append(
        {'count': count, 'List_car': List_car})
        
    Res.append({"Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def forecast_expired_month_center(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    
    for val in center_list:
        data_list = []
        count = 0
        # List_car = []
        for dat in inspection_list:
            if val.id == dat.center_id.id:
                monthis = dat.exp_date.month
                yearis = dat.exp_date.year
                current_month = timezone.now().month
                current_year = timezone.now().year
                if (monthis <= current_month) & (yearis <= current_year) :
                    count += 1
                    # List_car.append(dat.reg_id.id)
        data_list.append(
            {'count': count } )
        
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def forecast_expired_month_Area(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    # print(timezone.now().month, ' ', timezone.now().year)
    for AREA in range(3):
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        data_list = []
        count = 0
        List_car = []
        for val in center_list:
            if val.region == nameA:   
                for dat in inspection_list:
                    if val.id == dat.center_id.id:
                        monthis = dat.exp_date.month
                        yearis = dat.exp_date.year
                        current_month = timezone.now().month
                        current_year = timezone.now().year
                        # if (monthis == current_month) & (yearis == current_year) :
                        #     print(monthis, ' ', yearis)
                        if (monthis <= current_month) & (yearis <= current_year) :
                           
                            count += 1
                            
        data_list.append(
            {'count': count})
            
        Res.append({"Area": nameA, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def forecast_expired_month_Country(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    # print(timezone.now().month, ' ', timezone.now().year)
   
    data_list = []
    count = 0
    for val in center_list:
        
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    monthis = dat.exp_date.month
                    yearis = dat.exp_date.year
                    current_month = timezone.now().month
                    current_year = timezone.now().year
                    # if (monthis == current_month) & (yearis == current_year) :
                    #     print(monthis, ' ', yearis)
                    if (monthis <= current_month) & (yearis <= current_year) :
                        # print(monthis, ' ', yearis)
                        count += 1

    data_list.append(
        {'count': count})
        
    Res.append({"Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})