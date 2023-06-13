from django.db.models.functions import TruncYear, TruncQuarter, TruncMonth
from django.db.models import Count
from .models import inspection

def get_inspection_statistics():
    year_statistics = inspection.objects.annotate(year=TruncYear('date')).values('year').annotate(count=Count('id'))
    quarter_statistics = inspection.objects.annotate(quarter=TruncQuarter('date')).values('quarter').annotate(count=Count('id'))
    month_statistics = inspection.objects.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id'))
    return {'year_statistics': year_statistics, 'quarter_statistics': quarter_statistics, 'month_statistics': month_statistics}


