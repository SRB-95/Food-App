from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
# class based view
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# user permission
from django.contrib.auth.decorators import login_required

# Create your views here.

# def index (request):
#     item_list = Item.objects.all()
#     context ={
#         'item_list' : item_list,
#     }
#     return render(request,'food/index.html',context)

class IndexClassView(ListView):
    # food_search = request.GET.get('search_btn')
    model = Item
    template_name ='food/index.html'
    context_object_name = 'item_list'
    # Pagination
    paginate_by = 3
    paginate_orphans = 1

# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context={
#         'item' : item,  
#     }
#     return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name ='food/detail.html'

# def create_item (request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request,'food/item-form.html',{'form':form})

# This is a class beased view for create item
class CreateItem (CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

@login_required
def update_item (request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form,'item':item})

@login_required
def delete_item (request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',{'item':item})

# Search Functionality
def searchFunctionality(request):
    query = request.GET.get('s_form', None)
    # all_food_item = Item.objects.all()
    all_food_item = Item.objects.filter(item_name__icontains=query)
    return render(request, 'food/search.html', {'all_food_item':all_food_item})