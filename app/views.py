# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from app.models import *
from app.forms import *
from django.contrib import messages
from datetime import datetime

#@login_required(login_url="/login/")
def index(request):
    context = {'segment' : 'index'}
    cats = product_category.objects.all()
    products = product.objects.all()
    return render(request, "pages/frontend/index.html",{'cats':cats , 'products' : products}, context)

def productsFront(request):
    context = {'segment' : 'productFront'}
    cats = product_category.objects.all()
    products = product.objects.all()
    return render(request, "pages/frontend/shop.html",{'cats':cats , 'products' : products}, context)

def productsCat(request,id):
    context = {'segment' : 'productCat'}
    cats = product_category.objects.all()
    products = product.objects.filter(category=id)
    return render(request, "pages/frontend/product_by_cat.html",{'cats':cats , 'products' : products}, context)

def reviewsFront(request,id):
    type = "grid"
    reviews = review.objects.filter(product_id=id)
    return render(request, 'pages/frontend/reviews.html'
                  , {'reviews': reviews
                      , 'type': type})

@login_required(login_url="/login/")
def admin(request):
    context = {'segment' : 'index'}
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        context['segment'] = load_template

        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def products(request):
    
    type = "grid"
    products = product.objects.all()
   
    return render(request, 'pages/products.html'
                  , {'products': products
                      , 'type': type})

@login_required(login_url="/login/")
def addProduct(request):
    if request.method == "POST":
        form = productForm(request.POST, request.FILES,instance=product)
       # if form.is_valid():
        #    try:
        type = "grid"
        msg = "1"
        latest = product.objects.latest('id')
        form.fields["id"].initial = latest.id+ 1
        id = request.POST['id']
        name = request.POST['name']
        create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_uid = 1
        write_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_uid = 1
        category = request.POST['category']
        description = request.POST['description']
        price = request.POST['price']
        product_image=request.FILES['product_image']
        pro = product(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
         create_uid = create_uid, name=name, description=description, price=price, category=category,product_image=product_image)

        pro.save()
        products = product.objects.all()
        messages.success(request, f'Success, Product Saved Successfully')
        return render(request, 'pages/products.html'
                              , {'type': type, 'msg': msg, 'products': products})
         #   except:
          #      pass
        #else:
            #messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            #return redirect(addProduct)
    else:
        form = productForm()
        latest = product.objects.latest('id')
        form.fields["id"].initial = latest.id+ 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'pages/products.html', {'type': type, 'form': form})

@login_required(login_url="/login/")
def categories(request):
    type = "grid"
    cats = product_category.objects.all()
    return render(request, 'pages/categories.html'
                  , {'cats': cats
                      , 'type': type})

@login_required(login_url="/login/")
def addCategory(request):
    if request.method == "POST":
        form = categoryForm(request.POST, request.FILES)
       # if form.is_valid():
        #    try:
        type = "grid"
        msg = "1"
        latest = product_category.objects.latest('id')
        form.fields["id"].initial =  latest.id+1
        id = request.POST['id']
        name = request.POST['name']
        create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_uid = 1
        write_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_uid = 1
        parent_category = request.POST['category']
        description = request.POST['description']
        category_image = request.FILES['category_image']
        pro = product_category(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
         create_uid = create_uid, name=name, description=description,  parent_category=parent_category, category_image= category_image)

        pro.save()
        cats = product_category.objects.all()
        messages.success(request, f'Success, Product Category Saved Successfully')
        return render(request, 'pages/categories.html'
                              , {'type': type, 'msg': msg, 'cats': cats})
         #   except:
          #      pass
        #else:
            #messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            #return redirect(addProduct)
    else:
        form = categoryForm()
        latest = product_category.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'pages/categories.html', {'type': type, 'form': form})


@login_required(login_url="/login/")
def reviews(request):
    type = "grid"
    reviews = review.objects.all()
    return render(request, 'pages/reviews.html'
                  , {'reviews': reviews
                      , 'type': type})

@login_required(login_url="/login/")
def addReview(request):
    if request.method == "POST":
        form =reviewForm(request.POST)
       # if form.is_valid():
        #    try:
        type = "grid"
        msg = "1"
        latest = product.objects.latest('id')
        form.fields["id"].initial =  latest.id+ 1
        id = request.POST['id']
        reviewer_id = request.POST['reviewer_id']
        create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_uid = 1
        write_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_uid = 1
        product_id = request.POST['product_id']
        description = request.POST['description']
       
        pro = review(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
         create_uid = create_uid, reviewer_id=reviewer_id, description=description,  product_id=product_id)

        pro.save()
        reviews = review.objects.all()
                #messages.success(request, f'Success, Product Saved Successfully')
        return render(request, 'pages/reviews.html'
                              , {'type': type, 'msg': msg, 'reviews': reviews})
         #   except:
          #      pass
        #else:
            #messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            #return redirect(addProduct)
    else:
        form = reviewForm()
        latest = product.objects.latest('id')
        form.fields["id"].initial = latest.id+ 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'pages/reviews.html', {'type': type, 'form': form})

@login_required(login_url="/login/")
def users(request):
    type = "grid"
    users = user.objects.all()
    return render(request, 'pages/users.html'
                  , {'users': users
                      , 'type': type})

@login_required(login_url="/login/")
def addUser(request):
    if request.method == "POST":
        form =userForm(request.POST)
       # if form.is_valid():
        #    try:
        type = "grid"
        msg = "1"
        latest = product.objects.latest('id')
        form.fields["id"].initial =  latest.id+ 1
        id = request.POST['id']
        name = request.POST['name']
        create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_uid = 1
        write_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_uid = 1
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
       
        pro = user(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
         create_uid = create_uid, name=name, email=email,  password=password, role=role)

        pro.save()
        users = user.objects.all()
        messages.success(request, f'Success, Product Saved Successfully')
        return render(request, 'pages/users.html'
                              , {'type': type, 'msg': msg, 'users': users})
         #   except:
          #      pass
        #else:
            #messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            #return redirect(addProduct)
    else:
        form = userForm()
        latest = user.objects.latest('id')
        form.fields["id"].initial = latest.id+ 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'pages/users.html', {'type': type, 'form': form})

def deleteProduct(request, id):
    pro = product.objects.get(id=id)
    pro.delete()
    type = "grid"
    msg = "2"
    products = product.objects.all()
    if True:
       messages.warning(request, f'Success, Record Deleted Successfully')
    elif False:
       messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'pages/products.html'
                  , {'type': type, 'msg': msg, 'products': products})

def deleteCategory(request, id):
    cat = product_category.objects.get(id=id)
    cat.delete()
    type = "grid"
    msg = "2"
    cats = product_category.objects.all()
    if True:
       messages.warning(request, f'Success, Record Deleted Successfully')
    elif False:
       messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'pages/categories.html'
                  , {'type': type, 'msg': msg, 'cats': cats})

def deleteReview(request, id):
    rev = review.objects.get(id=id)
    rev.delete()
    type = "grid"
    msg = "2"
    reviews = review.objects.all()
    if True:
       messages.warning(request, f'Success, Record Deleted Successfully')
    elif False:
       messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'pages/reviews.html'
                  , {'type': type, 'msg': msg, 'reviews': reviews})
                
def deleteUser(request, id):
    user = user.objects.get(id=id)
    user.delete()
    type = "grid"
    msg = "2"
    users = user.objects.all()
    if True:
       messages.warning(request, f'Success, Record Deleted Successfully')
    elif False:
       messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'pages/users.html'
                  , {'type': type, 'msg': msg, 'users': users})

def editProduct(request, id):
    type = "edit"
    editForm = product.objects.get(id=id)
    return render(request, 'pages/products.html', {'form': editForm, 'type': type})


def updateProduct(request, id):
    type = "grid"
    pro = product.objects.get(id=id)
    id = pro.id
    name = request.POST['name']
    create_date = pro.create_date
    create_uid = pro.create_uid
    write_date = pro.write_date
    write_uid = pro.write_uid
    category = request.POST['category']
    description = request.POST['description']
    price = request.POST['price']
    product_image=request.FILES['product_image']
  
    pro = product(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, category=category, description=description,
                              price=price, product_image=product_image)
    pro.save()
    msg = "3"
    products = product.objects.all()

    if True:
        messages.success(request, f'Success, Product Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Product Update Error')

    return render(request, 'pages/products.html'
                  , {'type': type, 'msg': msg, 'products': products})



def addReviewF(request , id):
    if request.method == "POST":
        form =reviewForm(request.POST)
       # if form.is_valid():
        #    try:
        type = "grid"
        msg = "1"
        latest = review.objects.latest('id')
        form.fields["id"].initial =  latest.id+ 1
        idr = request.POST['id']
        reviewer_id = request.POST['reviewer_id']
        create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_uid = 1
        write_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_uid = 1
        product_id = request.POST['product_id']
        description = request.POST['description']
       
        pro = review(id=idr, write_date=write_date, write_uid=write_uid,create_date=create_date,
         create_uid = create_uid, reviewer_id=reviewer_id, description=description,  product_id=product_id)

        pro.save()
        reviews = review.objects.all()
                #messages.success(request, f'Success, Product Saved Successfully')
        return render(request, 'pages/frontend/reviews.html'
                              , {'type': type, 'msg': msg, 'reviews': reviews})
         #   except:
          #      pass
        #else:
            #messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            #return redirect(addProduct)
    else:
        form = reviewForm()
        latest = review.objects.latest('id')
        form.fields["id"].initial = latest.id+ 1
        form.fields["reviewer_id"].initial = id
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['reviewer_id'].widget.attrs['readonly'] = True
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'pages/frontend/reviews.html', {'type': type, 'form': form})