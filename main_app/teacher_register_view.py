from .models import *
import json
import requests
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                             get_object_or_404, redirect, render)
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from .forms import *
from .models import *




def teacherregister(request):


    form = CustomUserForm2(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Teacher'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            # address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password1')
            confirm_password = form.cleaned_data.get('password2')
            # course = form.cleaned_data.get('course')
            # passport = request.FILES.get('profile_pic')
            # fs = FileSystemStorage()
            # filename = fs.save(passport.name, passport)
            # passport_url = fs.url(filename)
            try:
                user = CustomUser.objects.create_user(
                    email=email, password=password, user_type=2, first_name=first_name, last_name=last_name)
                user.gender = gender
                # user.address = address
                # user.staff.course = course
                user.save()
                messages.success(request, " Teacher Successfully Added")
                return redirect(reverse('login_page'))

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'main_app/registration.html', context)



    