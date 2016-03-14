from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.core.context_processors import csrf

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
    account_id = request.session.get('account_id')
    if account_id:
        return render_to_response('accounts/menu.html',{'account_id':account_id})
    else:
        return HttpResponse("ascacs")