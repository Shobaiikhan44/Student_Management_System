from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            print("Saved Image Path:", student.image.path)  # Debugging
            messages.success(request, 'Student registered successfully!')
            return redirect('register_student')
        else:
            messages.error(request, 'Error in form submission.')
            print("Form errors:", form.errors)  # Debugging

    else:
        form = StudentForm()

    return render(request, 'register.html', {'form': form})


def search_student(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            students = Student.objects.filter(first_name__icontains=query)  | Student.objects.filter(email__icontains=query)
            return render(request, 'search.html', {'students': students})
    return render(request, 'search.html')