import csv
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.utils import timezone
from .models import center, owner, registration, inspection, account
from .forms import uploadFileForm

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


#for forms and statistics
def upload_reg_file(request):
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            reader = csv.reader(file)
            for row in reader:
                reg = registration(id=row[0], plate=row[1], reg_date=row[2], place=row[3], car_des=row[4], purpose=row[5], owner_id_id=row[6])
                reg.save()
            return render(request, '.html')
    else:
        form = uploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})

 
def get_number_of_cars_inspected_by_month(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for val in center_list:
        data_list = []
        for month in range(1, 13):
            count = 0
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    if dat.exp_date.month == month:
                        count += 1
            data_list.append({'month': month, 'count': count})
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def get_number_of_cars_inspected_by_quarter(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for val in center_list:
        data_list = []
        for quarter in range(1, 5):
            count = 0
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    if (dat.exp_date.month - 1) // 3 + 1 == quarter:
                        count += 1
            data_list.append({'quarter': quarter, 'count': count})
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def get_number_of_cars_inspected_by_year(request):
    Res = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for val in center_list:
        data_list = []
        for year in range(2010, timezone.now().year + 1):
            count = 0
            for dat in inspection_list:
                if val.id == dat.center_id.id:
                    if dat.exp_date.year == year:
                        count += 1
            data_list.append({'year': year, 'count': count})
        Res.append({"Name_center": val.name, "Ds": data_list})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})




def get_forecast(request):
    data = {}
    data['centers'] = []
    data['areas'] = []
    data['country'] = []
    data['forecast_centers'] = []
    data['forecast_areas'] = []
    data['forecast_country'] = []
    center_list = center.objects.all()
    inspection_list = inspection.objects.all()
    for val in center_list:
        center_data = {}
        center_data['name'] = val.name
        center_data['count'] = 0
        for dat in inspection_list:
            if val.id == dat.center_id.id:
                monthis = dat.exp_date.month
                yearis = dat.exp_date.year
                current_month = timezone.now().month
                current_year = timezone.now().year
                if (monthis == current_month) & (yearis == current_year) :
                    center_data['count'] += 1
        data['centers'].append(center_data)
    for AREA in range(3):
        area_data = {}
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        area_data['name'] = nameA
        area_data['count'] = 0
        for val in center_list:
            if val.region == nameA:   
                for dat in inspection_list:
                    if val.id == dat.center_id.id:
                        monthis = dat.exp_date.month
                        yearis = dat.exp_date.year
                        current_month = timezone.now().month
                        current_year = timezone.now().year
                        if (monthis == current_month) & (yearis == current_year) :
                            area_data['count'] += 1
        data['areas'].append(area_data)
    country_data = {}
    country_data['count'] = 0
    for val in center_list:
        for dat in inspection_list:
            if val.id == dat.center_id.id:
                monthis = dat.exp_date.month
                yearis = dat.exp_date.year
                current_month = timezone.now().month
                current_year = timezone.now().year
                if (monthis == current_month) & (yearis == current_year) :
                    country_data['count'] += 1
    data['country'].append(country_data)
    for val in center_list:
        center_data = {}
        center_data['name'] = val.name
        center_data['count'] = 0
        for dat in inspection_list:
            if val.id == dat.center_id.id:
                monthis = dat.exp_date.month
                yearis = dat.exp_date.year
                current_month = timezone.now().month
                current_year = timezone.now().year
                if (monthis <= current_month) & (yearis <= current_year) :
                    center_data['count'] += 1
        data['forecast_centers'].append(center_data)
    for AREA in range(3):
        area_data = {}
        if AREA == 0:
            nameA = "Miền Bắc"
        if AREA == 1:
            nameA = "Miền Trung"
        if AREA == 2:
            nameA = "Miền Nam"
        area_data['name'] = nameA
        area_data['count'] = 0
        for val in center_list:
            if val.region == nameA:   
                for dat in inspection_list:
                    if val.id == dat.center_id.id:
                        monthis = dat.exp_date.month
                        yearis = dat.exp_date.year
                        current_month = timezone.now().month
                        current_year = timezone.now().year
                        if (monthis <= current_month) & (yearis <= current_year) :
                            area_data['count'] += 1
        data['forecast_areas'].append(area_data)
    country_data = {}
    country_data['count'] = 0
    for val in center_list:
        for dat in inspection_list:
            if val.id == dat.center_id.id:
                monthis = dat.exp_date.month
                yearis = dat.exp_date.year
                current_month = timezone.now().month
                current_year = timezone.now().year
                if (monthis <= current_month) & (yearis <= current_year) :
                    country_data['count'] += 1
    data['forecast_country'].append(country_data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    
def complete_inspection(request):
    if request.method == 'POST':
        center_id = request.POST.get('center_id')
        reg_id = request.POST.get('id')
        reg = registration.objects.get(id=reg_id)
        inspection_obj = inspection(reg_id=reg, center_id=center_id, insp_date=timezone.now())
        inspection_obj.save()
        return HttpResponse('Inspection completed successfully')
    else:
        return HttpResponse('Invalid request method')

def add_center_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        acc = account(username = data['username'],password = data['password'],role = data['role'],center_id = data['center_id'])
        acc.save()
        return HttpResponse('Center added successfully')
    else:
        return HttpResponse('Invalid request method')


import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
@csrf_exempt
# def add_center_account(request):
def test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        print(request.POST.get('out'))
        return HttpResponse('Inspection completed successfully')
    else:
        return HttpResponse('Invalid request method')
def get_plate_status(request):
    key1 = request.GET.get('key1')
    key2 = request.GET.get('key2')
    f1 = inspection.objects.filter(center_id=key1, reg_id=key2)
    exp_date = f1.get().exp_date
    f2 = registration.objects.filter(id=key2)
    plate_car = f2.get().plate
    Res = []
    status = 1
    if (exp_date.month < timezone.now().month) & (exp_date.year < timezone.now().year):
        status = 0
    Res.append({'Plate' : plate_car, 'status' : status})
    data = list(Res)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
