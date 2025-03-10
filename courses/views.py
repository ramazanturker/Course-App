from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Category
from django.core.paginator import Paginator


def index(request):
    courses = Course.objects.filter(isActive = 1, isHome=1)
    categories = Category.objects.all()
    
    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses
    })
    
def create_course(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        slug = request.POST["slug"]
        isActive = request.POST.get("isActive", False)
        isHome = request.POST.get("isHome", False)
        
        if isActive == "on":
            isActive = True
            
        if isHome == "on":
            isHome = True
        
        error = False
        message = ""
        
        if title == "":
            error = True
            message += "title is a required field"
        
        if len(title) < 5:
            error = True
            message += "you must enter at least five characters"
        
        if error:
            return render(request, 'courses/create-course.html', { "error": True, "message": message })
             
        course = Course(title = title, description = description, imageUrl = imageUrl, slug = slug, isActive = isActive, isHome = isHome)
        course.save()
        return redirect("/courses")
        
    return render(request, 'courses/create-course.html')
    
def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        courses = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        categories = Category.objects.all()
    else:
        return redirect("/courses")
    
    return render(request, 'courses/search.html', {
        'categories': categories,
        'courses': courses,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    
    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    courses = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    categories = Category.objects.all()
    
    paginator = Paginator(courses, 3)
    page = request.GET.get('page', 1)
    page_object = paginator.page(page)
    
    return render(request, 'courses/list.html', {
        'categories': categories,
        'page_object': page_object,
        'selectedCategory': slug
    })