from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import sale,Sales_Agent
from .forms import CustomUserCreationForm, SaleForm, SaleModelForm



class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm


    def get_success_url(self):
        return reverse("login")




class LandingPageView(generic.TemplateView):
    template_name = "home_page.html"


def home_page(request):
    return render(request,"home_page.html")



class SaleListView(generic.ListView):
    template_name = "sales/sale_list.html"
    queryset = sale.objects.all()
    
    



def sale_list(request):
    sales = sale.objects.all()
    context = {
        "sales": sales
    }
    return render(request, "sales/sale_list.html",context)


class SaleDetailView(generic.DetailView):
    template_name = "sales/sale_detail.html"
    queryset = sale.objects.all()
    



def sale_detail(request, pk):
    sales = sale.objects.get(id=pk)
    context = {
        "sale" : sales
    }
    return render(request, "sales/sale_detail.html", context)


class SaleCreateView(generic.CreateView):
    template_name = "sales/sale_create.html"
    form_class = SaleModelForm


    def get_success_url(self):
        return reverse("sales:sale-list")


    def form_valid(self,form):
        #send email
        send_mail(
            subject="A Sale has been created", 
            message="Visit site to view Sale Details",
            from_email = "test@test.com",
            recipient_list = ["test2@test.com"]
        )

        return super(SaleCreateView, self).form_valid(form)




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



class SaleUpdateView(generic.UpdateView):
    template_name = "sales/sale_update.html"
    queryset = sale.objects.all()
    form_class = SaleModelForm


    def get_success_url(self):
        return reverse("sales:sale-list")


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



class SaleDeleteView(generic.DeleteView):
    template_name = "sales/sale_delete.html"
    queryset = sale.objects.all()
    


    def get_success_url(self):
        return reverse("sales:sale-list")



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