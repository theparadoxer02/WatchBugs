from django.shortcuts import render, redirect,get_object_or_404 as goo404
from django.http import HttpResponse
from .models import bugshare
import hashlib
from django.contrib import messages
import random
from .forms import mainform
from .models import bugshare


def home(request):
    if request.method == 'POST':
        form = mainform(request.POST)
        print("ho")
        if form.is_valid():
            name = form.cleaned_data["name"]
            url = form.cleaned_data["url"]
            code = form.cleaned_data["code"]
            bug = form.cleaned_data["bug"]
            comment = form.cleaned_data["comment"]
            a=random.randrange(0,6)
            hash_value = str(hash(code))[a:a+8]
            if bugshare.objects.filter(hash_value=hash_value).exists() == True:
                messages.error(request,"The file already exist bhai ! , try something else")
                return render(request,"shareapp/home.html")
            bugshare.objects.create(name=name,url=url,code=code,bug=bug,comment=comment,hash_value=hash_value)
            return redirect('shareapp:view_by_hash',hash_id=hash_value)
    else:
        form = mainform()
        return render(request,'shareapp/home.html',{"form":form})

def view_by_hash(request,hash_id):
    if request.method == 'GET':
        print("getting data")
        code_obj = goo404(bugshare,hash_value=hash_id)
        return render(request,'shareapp/home.html',{"modelcode":code_obj,"filename":"yes"} )
    if request.method == 'POST':
        code = request.POST.get('code')
        code_obj = goo404(bugshare,hash_value=hash_id)
        code_obj.code = code
        code_obj.save()
        return redirect("shareapp:view_by_hash",hash_id=hash_id)
