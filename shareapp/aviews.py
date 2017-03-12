from django.shortcuts import render, redirect,get_object_or_404 as goo404
from django.http import HttpResponse
from .models import bugshare
import hashlib
from django.contrib import messages
import random

def home(request):
    if request.method == 'GET':
        return render(request,'shareapp/homepage.html')
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        url = request.POST.get('url')
        bug = request.POST.get('bug')
        comment = request.POST.get('comment')
        print("%s %s %s %s"%(code,name,url,bug))
        a=random.randrange(0,6)
        hash_value = str(hash(code))[a:a+8]
        if bugshare.objects.filter(name=name).exists() == True and name != '':
            messages.error(request,'Awww!! An error. Probably we might have a file with same name. Damn those folks.')
            return render(request, 'shareapp/homepage.html',{})
        bugshare.objects.create(code=code,
                                hash_value=hash_value,
                                url=url,
                                bug=bug,
                                comment=comment)
        return redirect('shareapp:view_by_hash',hash_id=hash_value)


def view_by_hash(request,hash_id):
    if request.method=='GET':
        code = Bugshare.objects.get(hash_value=hash_id)
        return render(request,'shareapp/homepage.html',{'code':code})
    if request.method=='POST':
        code = request.POST.get('code')
        code_object = goo404(bugshare,hash_value=hash_id)
        code_object = code
        code_object.save()
        return render('shareapp:view_by_hash',hash_id=hash_id)


def view_by_name(request,name):
    if request.method=='GET':
        code = request.objects.get(name=name)
        return render(request,'shareapp/homepage.html',{'code':code})
    if request.method=='POST':
        code = request.POST.get('code')
        code_object = goo404(bugshare,name=name)
        code_object = code
        code_object.save()
        return render('shareapp:view_by_name',name=name)
