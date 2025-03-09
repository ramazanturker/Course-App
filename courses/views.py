from datetime import date, datetime
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course, Category

data = {
    "programming": "course lists in the programming category",
    "web-development": "course lists in the web development category",
    "mobile": "course lists in the mobile category",
}

db = {
    "courses": [
        {
            "title": "javascript course",
            "description": "javascript course description",
            "imageUrl": "1.jpg",
            "slug": "javascript-course",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "python course",
            "description": "python course description",
            "imageUrl": "2.jpg",
            "slug": "python-course",
            "date": date(2022,9,10),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "web development course",
            "description": "web development course description",
            "imageUrl": "3.jpg",
            "slug": "web-development-course",
            "date": date(2022,8,10),
            "isActive": True,
            "isUpdated": True
        },
    ],
    "categories": [
        { "id": 1, "name": "programming", "slug": "programming" },
        { "id": 2, "name": "web development", "slug": "web-development" },
        { "id": 3, "name": "mobile applications", "slug": "mobile-applications" },
    ]
}

def index(request):
    courses = Course.objects.filter(isActive = 1)
    categories = Category.objects.all()

    # for course in db["courses"]:
    #     if course["isActive"] == True:
    #         courses.append(course)
    
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
    courses = Course.objects.filter(category__slug=slug, isActive=True)
    categories = Category.objects.all()
    
    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'selectedCategory': slug
    })