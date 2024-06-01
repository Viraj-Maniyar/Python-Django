from django.shortcuts import render,redirect
from  .models import*


# Uploading a Recipe

def index(request):
   if request.method == "POST":
      data = request.POST
      recipe_name = data.get('recipe_name') 
      recipe_description = data.get('recipe_description')
      recipe_image = request.FILES.get('recipe_image')
      
      recipe.objects.create(
         recipe_name = recipe_name,
         recipe_description = recipe_description,
         recipe_image = recipe_image
      )
      return redirect('index')

   
   queryset = recipe.objects.all()
   
   if request.GET.get('Search'):
      queryset = queryset.filter(recipe_name__icontains = request.GET.get('Search'))
   
   context = {'recipies': queryset}
       
   return render(request,'index.html' , context)

# Update a Recipe 

def update_recipe(request, id):
   queryset = recipe.objects.get(id = id)

   if request.method == "POST":
      data = request.POST
      recipe_name = data.get('recipe_name')
      recipe_description = data.get('recipe_description')
      recipe_image = request.FILES.get('recipe_image')

      queryset.recipe_name = recipe_name
      queryset.recipe_description = recipe_description
      
      if recipe_image:
         queryset.recipe_image = recipe_image
      queryset.save()
      return redirect('index')

   context = {'recipe' : queryset}

   return render(request,'update_recipe.html', context)

# delete a Recipe

def delete_recipe(request,id):
   queryset = recipe.objects.get(id = id)
   queryset.delete()
   return redirect('/')