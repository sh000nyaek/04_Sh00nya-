from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sales_Agent, sale
from .forms import SaleForm, SaleModelForm


def home_page(request):
    return render(request,"home_page.html")



def sale_list(request):
    sales = sale.objects.all()
    context = {
        "sales": sales
    }
    return render(request, "sales/sale_list.html",context)



def sale_detail(request, pk):
    sales = sale.objects.get(id=pk)
    context = {
        "sale" : sales
    }
    return render(request, "sales/sale_detail.html", context)


def sale_create(request):
    form = SaleModelForm()
    if request.method == "POST":
        form = SaleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sales")

    context = {
        "form":SaleModelForm()
    }
    return render(request, "sales/sale_create.html",context)


def sale_update(request, pk):
    sales = sale.objects.get(id=pk)
    form = SaleModelForm(instance=sales)
    if request.method == "POST":
        form = SaleModelForm(request.POST, instance=sales)
        if form.is_valid():
            form.save()
            return redirect("/sales")
    context = {
        "form":form,
        "sale": sales
    }
    return render(request, "sales/sale_update.html",context)


def sale_delete(request, pk):
    sales = sale.objects.get(id=pk)
    sales.delete()
    return redirect("/sales")



# def sale_update(request, pk):
#     sales = sale.objects.get(id=pk)
#     form = SaleForm()
#     if request.method == "POST":
#         form = SaleForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             sales.first_name = first_name
#             sales.last_name = last_name
#             sales.age = age
#             sales.save()
#             return redirect("/sales")
    # context = {
    #     "form":form,
    #     "sale": sales
    # }
#     return render(request, "sale_update.html",context)