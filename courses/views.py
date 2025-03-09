from datetime import date, datetime
from django.shortcuts import get_object_or_404, render
from .models import Course, Category
from django.core.paginator import Paginator


def index(request):
    courses = Course.objects.filter(isActive = 1)
    categories = Category.objects.all()
    
    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses
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
    
    return render(request, 'courses/index.html', {
        'categories': categories,
        'page_object': page_object,
        'selectedCategory': slug
    })