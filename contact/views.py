from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def index(request, letter = None):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith = letter)
    else:
        contacts = Contact.objects.filter(name__icontains=request.GET.get('search', ''))
    context = {
        'contacts': contacts,
        'alphabet':alphabet,
    }
    return render(request, 'contact/index.html', context)

def view(request,id):
    contact = Contact.objects.get(id=id)   
    context = {
        'contact': contact
    }
    return render(request, 'contact/detail.html', context)

def edit(request,id):
    contact = Contact.objects.get(id=id)
    if request.method == "GET":
        form = ContactForm(instance=contact)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'contact/edit.html', context)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        context = {
            'form':form,
            'id':id
        }
        messages.success(request,'Contacto Actualizado')
        return render(request, 'contact/edit.html', context)
    
def create(request):
    if request.method == "GET":
        form = ContactForm()
        context = {
            'form':form,
        }
        return render(request, 'contact/create.html', context)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')
    
def delete(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')