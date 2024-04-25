from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from .models import Client, Product, Order
from datetime import datetime, timedelta
from .forms import AddProductForm
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    logger.info('Посетили главную...')
    return HttpResponse('''
                <h1>Самая главная страница</h1>
                <h6>С совсем немногострочным кодом...</h6>     
            ''')


def about(request):
    logger.info('Кто-то нами заинтересовался')
    return HttpResponse('''
                <h1>Коротко о нас</h1>
                <h6>Совсем коротко...</h6>
                <p>После завершения обучения у нас откроется доступ к курсу по подготовке к поиску работы от центра карьеры GeekBrains.<br><br>

                Это практический курс, на котором мы пройдем все основные этапы подготовки к поиску работы: разработаем стратегию поиска работы, составим резюме и подготовимся к интервью с рекрутером.<br><br>

                После этого мы сможем обратиться за помощью в поиске работы в центр карьеры и продолжить работать с карьерным консультантом. На последнем уроке курса будет ссылка на форму, которую необходимо заполнить для обращения в центр карьеры. </p>    
            ''')


def products(request, client_id, count_days):
    start_date = datetime.today() - timedelta(days=count_days)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer_id=client, date_ordered__gt=start_date)
    ords = set()
    for ord in orders:
        prods = ord.products.all()
        print(type(prods))
        for prod in prods:
            ords.add(prod)
    ords = list(ords)
    ords.sort(key=lambda d: d.date_add, reverse=False)
    return render(request, 'mainapp/client_orders.html', {'client': client, 'orders': ords})


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            product = Product(name=name, description=description, price=price, count=count, image=image)
            product.save()
    else:
        form = AddProductForm()
    return render(request, 'mainapp/add_product.html', {'form': form})