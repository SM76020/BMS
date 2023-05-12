from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import bank
from wsgiref.util import FileWrapper
import os
# Create your views here.

#Login Page
def Home(request):
    return render(request, "login.html")

#Registration Admin
def reg(request):
    if request.method == "POST":
        fullname=request.POST.get("fullname")
        username=request.POST.get("username")
        email=request.POST.get("email")
        phonenumber=request.POST.get("phonenumber")
        password=request.POST.get("password")
        gender=request.POST.get("gender")
        branch=request.POST.get("branch")
       # print(fullname,username,email,phonenumber,password)
        ob=Registration.objects.create(fullname=fullname,username=username,email=email,phonenumber=phonenumber,password=password,gender=gender,branch=branch)
        ob.save()
    return render(request,"registration.html")

#Admin Login
def log(request):
    a=request.POST['username']
    b=request.POST['password']
    try:
        if Registration.objects.filter(username=a,password=b):
            return render(request,"account.html")
        else:
            return render(request,"login.html")
    except Exception as e:
        return HttpResponse(e)
    
#Display Homepage  
def ds(request):
    return render(request,'account.html')

#Add Account Holder
def acc(request):
    if request.method == "POST":
        fulln=request.POST.get("fullname")
        mail=request.POST.get("email")
        accn=request.POST.get("accno")
        num=request.POST.get("number")
        addr=request.POST.get("address")
        dob=request.POST.get("dob")
        pin=request.POST.get("pin")
        typeac=request.POST.get("typeac")
        depo=request.POST.get("depo")
        typ="deposit"

        ob=Accholder.objects.create(fullname=fulln,email=mail,accno=accn,number=num,address=addr,dob=dob,pin=pin,typeac=typeac)
        ob.save()
        eb=Transaction.objects.create(account_number=accn,transaction_amount=depo,transaction_type=typ,current_balance=depo)
        eb.save()
        # return HttpResponse("Success: New account holder created.")
    
    return render(request,"holder.html")

#To see all Account Holder
def all_accounts(request):
    accounts = Accholder.objects.all()
    return render(request, 'AccHDetails.html',{'details_key':accounts})

#Edit Account Holder Details
def edit(request,idp):
    object=Accholder.objects.get(id=idp)
    return render(request,'editach.html',{'objectp':object})

#Update Account Holder Details
def update(request,idu):
    object=Accholder.objects.get(id=idu)
    form=bank(request.POST,instance=object)
    if form.is_valid:
        form.save()
        acc=Accholder.objects.all()
        return render(request,'account.html')

#Delete a Account Holder
def delete(request,idd):
    member=Accholder.objects.get(id=idd)
    member.delete()
    return render(request,'account.html')

#Deposit Amount
def deposit(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        transaction_amount = request.POST.get('transaction_amount')
        current_balance = Transaction.objects.filter(account_number=account_number).order_by('-transaction_datetime').first().current_balance
        new_balance = float(current_balance) + float(transaction_amount)
        am=Transaction.objects.create(account_number=account_number,transaction_amount=transaction_amount,transaction_type='deposit',current_balance=new_balance)
        am.save()
        return HttpResponse('deposit_success')
    return render(request, 'deposite.html')

#Withdrawal Amount
def withdrawal(request):
    try:
        if request.method == 'POST':
            account_number = request.POST.get('account_number')
            transaction_amount = request.POST.get('transaction_amount')
            current_balance = Transaction.objects.filter(account_number=account_number).order_by('-transaction_datetime').first().current_balance
            if float(transaction_amount) > float(current_balance):
                return HttpResponse(request, 'withdrawal_error')
            else:
                new_balance = float(current_balance) - float(transaction_amount)
                am=Transaction.objects.create(account_number=account_number,transaction_amount=transaction_amount,transaction_type='withdrawal',current_balance=new_balance)
                am.save()
                return HttpResponse('withdrawal_success')
    except Exception as e:
        return HttpResponse(e)

#Withdrawal Page
def wit(request):
    return render(request, 'withdrawl.html')

#To see All Transactions
def treport(request):
    transactions = Transaction.objects.all()
    return render(request, 'accreports.html', {'transactions': transactions})


# def download_pdf(request):
#     filename = 'transactions.pdf'
#     content = FileWrapper(filename)
#     response = HttpResponse(content, content_type='application/pdf')
#     response['Content-Length'] = os.path.getsize(filename)
#     response['Content-Disposition'] = 'attachment; filename=%s' % 'transaction.pdf'
#     return response