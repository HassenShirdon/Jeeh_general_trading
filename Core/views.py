from django.shortcuts import render, get_object_or_404, redirect
from urllib import request
from django.http import HttpResponse
from .models import Team, Product, Testominals
from django.views import generic
from .forms import ProductForm, TeamForm, TestimonialsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    teams = Team.objects.all()
    products = Product.objects.all()[:6]
    testominals = Testominals.objects.all()
    return render(request, 'Core/index.html', {'teams': teams, 'products': products, 'testominals': testominals})


def product(request):
    products = Product.objects.all()
    return render(request, 'Core/product.html', {'products': products})


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'Core/product_detail.html'


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The team has been created successfully.')
            return redirect('index')
    else:
        messages.error(request, 'Please correct the following errors:')
        form = ProductForm()

    context = {'form': form}
    return render(request, 'Core/product_form.html', context)


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        context = {'form': ProductForm(instance=product), 'id': id}
        return render(request, 'Core/product_form.html', context)

    elif request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The product has been updated successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'product_form.html', {'form': form})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}

    if request.method == 'GET':
        return render(request, 'product_confirm_delete.html', context)
    elif request.method == 'POST':
        product.delete()
        messages.success(request, 'the product has been successfully deleted')
        return redirect('index')


@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The team has been created successfully.')
            return redirect('index')
    else:
        messages.error(request, 'Please correct the following errors:')
        form = TeamForm()

    context = {'form': form}
    return render(request, 'Core/team_form.html', context)


@login_required
def create_testimonials(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TestimonialsForm()

    context = {'form': form}
    return render(request, 'Core/testimonial_form.html', context)


def about(request):
    teams = Team.objects.all()
    return render(request, 'Core/about.html', {'teams': teams})


def services(request):
    return render(request, 'Core/services.html', {})
