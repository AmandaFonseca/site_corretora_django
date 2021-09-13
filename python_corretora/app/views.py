from django.shortcuts import render
from django.http import HttpResponse
from app.forms import ClienteForm
from django.shortcuts import redirect
from app.models import Cliente
from django.db import connection
from datetime import date
from django.core.paginator import Paginator
from string import Template

def calculate_age(dt):
    today = date.today()
    return today.year - dt.year - ((today.month, today.day) < (dt.month, st.day))

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def my_custom_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()

def paginacao(request):
    data ={}
    all = Cliente.objects.all()
    paginator = Paginator(all, 3)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return data


# Create your views here.
def home(request):
    data={}
    data['db'] = Cliente.objects.all()
    #data = paginacao(request)

    datainfo = data['db']
    t = Template('UPDATE app_cliente SET idade = $x WHERE id = $y')
    for x in datainfo.values():
        for idx, val in enumerate(x):
            if val == 'id':
                id_user = x[val]
            if val == 'data_nascimento':
                idade_user = calculateAge(x[val])
                sql = t.substitute({'x': idade_user, 'y': id_user})
                my_custom_sql(sql)
    return render(request, 'index.html',data)


def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'form.html', data)

def create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return  redirect('home')