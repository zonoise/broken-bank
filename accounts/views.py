from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.template.context_processors import csrf

from datetime import datetime

from models import UserTotal
from forms import AddMoneyForm

# Create your views here.
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/index.html',c)

def login(request):
    account_id = request.POST.get('account-id')
    if account_id :
        request.session['account_id'] = account_id
        return redirect('menu')
    else:
        return redirect('index')

def menu(request):
    accountid = request.session.get('account_id')
    if accountid:
        user_total, status = UserTotal.objects.get_or_create(
            account_id = accountid,
            defaults = {'account_id': accountid,'value': 0,'created_at':datetime.now()}
            )
        c = {'account_id':accountid,'user_total_money':user_total.value,'form':AddMoneyForm()}
        c.update(csrf(request))
        return render_to_response('accounts/menu.html',c)
    else:
        return HttpResponse("ascacs")

from operations import add_money
def add(request):
    f = AddMoneyForm(request.POST)
    if f.is_valid():
        account_id = request.session.get('account_id')
        value = f.cleaned_data['value']
        
        add_money(account_id,value)
        return redirect('menu')
        #return HttpResponse("valid")
    else:
        return HttpResponse("no valid")
    
    
    