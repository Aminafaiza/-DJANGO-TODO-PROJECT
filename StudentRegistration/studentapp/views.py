
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def student_list(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    students = Student.objects.all().order_by('-id')

    return render(request, 'student_list.html', {
        'form': form,
        'students': students,
        'edit_mode': False,
    })


def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    students = Student.objects.all().order_by('-id')

    return render(request, 'student_list.html', {
        'form': form,
        'students': students,
        'edit_mode': True,
        'editing_student': student,
    })


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

    return redirect('student_list')
