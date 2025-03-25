from django.shortcuts import render
from .models import Customers, Transfer
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# def home(request):
#     return HttpResponse("Hello, Django!")

def home(request):
    return render(
        request,
        'moneyBank/home.html',
        {'nbar': 'home'}
    )

def about(request):
    return render(request,'moneyBank/about.html',{'nbar': 'about'})

def contact(request):
    return render(request,'moneyBank/contact.html',{'nbar': 'contact'})

def view_all_customers(request):
    all_customers = Customers.objects.all()
    context={
        'all_customers': all_customers,
        'nbar': 'view_all_customers'
    }
    return render(request,'moneyBank/view_all_customer.html',context)

def view_customer(request,user2):
    o_cust=Customers.objects.get(user_email=user2)
    context={
        'id':o_cust.id,
        'user_email':o_cust.user_email,
        'first_name':o_cust.first_name,
        'last_name':o_cust.last_name,
        'current_balance':o_cust.current_balance,
    }
    return render(request,'moneyBank/view_customer.html',context)

def make_transaction_filled(request,user2):
    o_cust=Customers.objects.get(user_email=user2)
    context={
        'user_email':o_cust.user_email,
        'first_name':o_cust.first_name,
        'last_name':o_cust.last_name,
        'account_no':o_cust.id,
        'flag':0,
    }
    return render(request,'moneyBank/make_transaction_field.html',context)

def transfer(request):
    if request.method == "POST":
        sender_email=request.POST.get("sender_email")
        sender_password=request.POST.get("sender_password")
        sender_account_no=request.POST.get("sender_account_no")
        receiver_email=request.POST.get("receiver_email")
        try:
            o_cust=Customers.objects.get(user_email=receiver_email)
            sender=Customers.objects.get(user_email=sender_email)
            amount=float(request.POST.get("amount"))
            if(sender_email == receiver_email or int(sender_account_no) == o_cust.id or int(sender_account_no) != sender.id):
                context={
                    'user_email':o_cust.user_email,
                    'first_name':o_cust.first_name,
                    'last_name':o_cust.last_name,
                    'flag':1,
                }
                return render(request,'moneyBank/make_transaction_field.html',context)
            receiver=Customers.objects.get(user_email=receiver_email)        
            if(sender_password != sender.password):
                context={
                    'user_email':o_cust.user_email,
                    'first_name':o_cust.first_name,
                    'last_name':o_cust.last_name,
                    'flag':2,
                }
                return render(request,'moneyBank/make_transaction_field.html',context)
            if(amount>=sender.current_balance):
                return HttpResponse("Not Enough Balance. Please Go Back.")
            sender.current_balance=sender.current_balance-amount
            receiver.current_balance=receiver.current_balance+amount
            tx=Transfer(tx_from = sender,tx_to=o_cust,amount=amount)
            tx.save()
            receiver.save()
            sender.save()
            return HttpResponseRedirect('/moneyBank/view_all_customers/')
        except:
            return HttpResponse("No Account Found. Enter Valid Account Details. Please Go Back.")
    return HttpResponseRedirect('moneyBank/view_all_customers/')

def view_your_account_details_page(request):
    return render(request,'moneyBank/view_your_account_details.html')

def view_your_account_details(request):
    if request.method == "POST":
        user_email=request.POST.get("user_email")
        password=request.POST.get("password")
        try:
            cust=Customers.objects.get(user_email=user_email)
            if(password != cust.password):
                return HttpResponse('INVALID PASSWORD.')
            context={
                'flag':0,
                'user_email':cust.user_email,
                'current_balance':cust.current_balance,
                'first_name':cust.first_name,
                'last_name':cust.last_name,
                'account_no':cust.id,
            }
            return render(request,'moneyBank/view_your_account_details.html',context)
        except:
            return HttpResponse("No Account Found. Enter Valid Account Details. Please Go Back.")

def view_transactions_page(request):
    return render(request,'moneyBank/view_transactions.html')

def view_transactions(request):
    user_email=request.POST.get("user_email")
    password=request.POST.get("password")
    print(user_email)
    print(password)
    try:
        cust=Customers.objects.get(user_email=user_email)
        if(password != cust.password):
            return HttpResponse('INVALID PASSWORD.')
                
        tx=Transfer.objects.filter(Q(tx_from=cust.id) | Q(tx_to=cust.id))
        print(tx)
        context={
            'flag':0,
            'user_email':cust.user_email,
            'current_balance':cust.current_balance,
            'first_name':cust.first_name,
            'last_name':cust.last_name,
            'account_no':cust.id,
            'tx':tx,
            'nbar': 'view_transactions_page',
        }
        return render(request,'moneybank/view_transactions.html',context)
    except:
        return HttpResponse("No Account Found. Enter Valid Account Details. Please Go Back.")