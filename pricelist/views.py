from django.shortcuts import render
from .models import Production, Service, ProductCategory, ServiceCategory
from django.conf import settings
# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['berteiusdeveloper@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def index(request):
    return render(request, 'pricelist/index.html', {})

def production_price_list(request):
    price = Production.objects.all()
    #price2 = Production.objects.raw('''SELECT * FROM production a,
    #                       WHERE a.id = (select max(id) from production
    #                                     WHERE theme_id = a.theme_id) GROUP BY theme_id''')
    p_categories = ProductCategory.objects.all()
    context = {'price' : price, 'categories' : p_categories}
    return render(request, 'pricelist/production_price_list.html', context)

def service_price_list(request):
    price = Service.objects.all()
    s_categories = ServiceCategory.objects.all()
    context = {'price' : price, 'categories' : s_categories}
    return render(request, 'pricelist/service_price_list.html', context)
