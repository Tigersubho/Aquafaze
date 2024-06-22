import joblib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Profile, Image1, Activity
import cv2
from django.shortcuts import render, redirect
import requests as r
import json
from django.conf import settings
import random
import smtplib
# views.py
import base64
import numpy as np
from django.http import JsonResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import joblib
from deepface import DeepFace

from django.core.mail import send_mail

from joblib import load
import sklearn


# Create your views here.
def AquaFaze(request):
    return render(request, 'app/AquaFaze.html')


def blogs(request):
    return render(request, 'app/blogs.html')


def activity_section(request):
    return render(request, 'app/activito.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/AquaFaze')
        else:
            return redirect('/login')
    return render(request, 'app/login.html')


def UserLoggedIn(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    return username


def logout_view(request):
    username = UserLoggedIn(request)
    if username is not None:
        logout(request)
        return redirect('/AquaFaze')
    else:
        return HttpResponse("you must login first to logout")


def signuppage(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        lastname = request.POST.get("lastname")
        firstname = request.POST.get("firstname")
        phone = request.POST.get("phone")
        try:
            if User.objects.get(username=username):
                error_message = 'Username is already taken.'
                return render(request, 'app/signup.html', {'error_message': error_message})
        except User.DoesNotExist:
            # if otp == request.session['otp']:
            if password == cpassword:
                my_user = User.objects.create_user(username, email, password, first_name=firstname,
                                                   last_name=lastname)
                my_user.save()
                return redirect('/login')
            else:
                error_messag = 'Passwords did not match.'
                return render(request, 'app/signup.html', {'error_messag': error_messag})
        # else:
        #     erro_message = 'OTP did not match'
        #     return render(request, 'app/signup.html', {'erro_message': erro_message})
    return render(request, 'app/signup.html')


def aboutus(request):
    return render(request, 'app/aboutus.html')


def quick(request):
    return render(request, 'app/quick.html')


def error(request):
    return render(request, 'app/error.html')


@login_required
def my_account(request):
    firstname = request.user.first_name
    lastname = request.user.last_name
    user_id = request.user.id
    name = firstname + " " + lastname
    email = request.user.email
    data = Profile.objects.get(user_id=user_id)
    data1 = Activity.objects.get(user_id=user_id)
    hydration1 = float(data1.Hydration)
    time = data1.work_time
    weight = float(data.Weight)
    height = float(data.Height)
    date = data.date
    date1 = data1.date
    hydration = float(data.Hydration)
    activity = int(data1.activity)
    if activity == 1:
        Activito = 'Bicycle'
    elif activity == 2:
        Activito = 'Bike Riding'
    elif activity == 3:
        Activito = 'Cricket'
    elif activity == 4:
        Activito = 'Football'
    elif activity == 5:
        Activito = 'Outdoor Games'
    elif activity == 6:
        Activito = 'Desk Job'
    elif activity == 7:
        Activito = 'Treking'
    elif activity == 8:
        Activito = 'Labourous job'

    return render(request, 'app/my_account.html',
                  {'name': name, 'email': email, 'weight': weight, 'height': height, 'date': date,
                   'hydration': hydration, 'hydration1': hydration1, 'Activity': Activito, 'time': time,
                   'date1': date1})


@login_required()
def activito(request):
    return render(request, 'app/activito.html')


def error404(request):
    return render(request, 'app/error404.html')


def buisness(request):
    return render(request, 'app/buisness.html')


@login_required(login_url='/error')
def detailed(request):
    return render(request, 'app/detailed.html')


souvik1 = 0


def profile(request):
    if request.method == 'POST':
        post = Profile()
        post.UserName = request.user.username
        post.first_name = request.user.first_name
        post.last_name = request.user.last_name
        post.user_id = request.user.id
        post.date = request.user.date_joined
        post.Age = request.POST.get('age')
        post.Height = request.POST.get('height')
        post.Weight = request.POST.get('weight')
        post.Gender = request.POST.get('gender')
        post.Ethnicity = request.POST.get('ethnicity')
        user_id = post.user_id
        try:
            firstname = request.user.first_name
            lastname = request.user.last_name
            user_id = request.user.id
            name = firstname + " " + lastname
            email = request.user.email
            data = Profile.objects.get(user_id=user_id)
            Age = int(data.Age)
            weight = float(data.Weight)
            height = float(data.Height)
            date = data.date
            hydration = data.Hydration
            error_message = 'You have already submitted details , you can just check it here and update it as per ' \
                            'your changes. '
            return render(request, 'app/my_account.html',
                          {'name': name, 'email': email, 'weight': weight, 'height': height, 'date': date,
                           'hydration': hydration, 'Age': Age,
                           'error_message': error_message})
        except ObjectDoesNotExist:
            post.save()
        Gender = int(post.Gender)
        Ethnicity = int(post.Ethnicity)
        Height = float(post.Height)
        Age = float(post.Age)
        key = "c7898f318b33426194a120118230205"
        lat = 82.48637
        lon = 135.31313
        resp = r.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lon}&aqi=no")
        re = json.loads(resp.text)
        city = re['location']['name']
        temp = re['current']['temp_c']
        sky = random.randint(0, 2)
        humidity = re['current']['humidity']
        rel_temp_c = re['current']['feelslike_c']
        weather = re['current']['condition']['text']
        if weather == "mist":
            weather = 3
        elif weather == "fog":
            weather = 1
        else:
            weather = 2
        state = re['location']['region']
        nation = re['location']['country']
        model = joblib.load('app/models/location_fetch.joblib')
        predict = [[weather, sky, humidity, temp, rel_temp_c]]
        location = model.predict(predict)
        print(location)
        Weight = float(post.Weight)
        BMI = int(Weight / (Height ** 2))
        finalmodel = joblib.load('app/models/mainHydration_final_dt.joblib')
        parameters = [[Ethnicity, Gender, Age, BMI]]
        Hydra = finalmodel.predict(parameters)
        Hydration = Hydra + location
        global souvik1
        souvik1 = float(Hydration)
        souvik1 = round(souvik1, 2)

        if souvik1:
            post.Hydration = souvik1
            post.save()
        return render(request, 'app/detailed.html', {'output': souvik1})


souvik = 0

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        image_data_url = request.POST.get('image_data')
        image_data = base64.b64decode(image_data_url.split(',')[1])
        key = "c7898f318b33426194a120118230205"
        lat = 22.48637
        lon = 88.31313
        resp = r.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lon}&aqi=no")
        re = json.loads(resp.text)
        # print(re)
        city = re['location']['name']
        temp = re['current']['temp_c']
        sky = random.randint(0, 2)
        humidity = re['current']['humidity']
        rel_temp_c = re['current']['feelslike_c']
        weather = re['current']['condition']['text']
        state = re['location']['region']
        nation = re['location']['country']

        if image_data_url:
            image11 = Image1(image_data=image_data_url)
            image11.save()
        model3 = load_model('app/models/Gener_detect.h5')
        model = load_model('app/models/model2.h5')
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((200, 200))
        image = img_to_array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        image = np.expand_dims(image, axis=0)
        image = image / 255.0
        prediction = model.predict(image)
        gender = int(model3.predict(image))
        age = int(prediction * 0.7)
        model1 = joblib.load('app/models/ageVsheight.joblib')
        ethnicity = 4
        input_data = [[age, gender, ethnicity]]
        prediction1 = float(model1.predict(input_data))
        height = prediction1 / 30.48
        model2 = joblib.load('app/models/weight_decisiontree.joblib')
        input_data1 = [[gender, ethnicity, height]]
        weight = float(model2.predict(input_data1))
        BMI = weight / (height ** 2)
        model4 = joblib.load('app/models/location_fetch.joblib')
        if weather == "mist":
            weather = 3
        elif weather == "fog":
            weather = 1
        else:
            weather = 2
        predict = [[weather, sky, humidity, temp, rel_temp_c]]
        location = model4.predict(predict)
        finalmodel = joblib.load('app/models/mainHydration_final_dt.joblib')
        parameters = [[ethnicity, gender, age, BMI]]
        Hydra = finalmodel.predict(parameters)
        Hydration = Hydra + location
        print(height)
        print(weight)
        print(age)
        print(gender)

        global souvik
        souvik = float(Hydration)
        souvik = round(souvik, 2)

        return render(request, 'app/quick.html')


def show_result(request):
    if request.method == 'POST':
        return render(request, 'app/quick.html', {'souvik': souvik})


def update(request):
    user_id = request.user.id
    instance = get_object_or_404(Profile, user_id=user_id)

    if request.method == 'POST':
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        age = request.POST.get('age')
        instance.Age = age
        instance.Height = height
        instance.Weight = weight
        instance.save()
        firstname = request.user.first_name
        lastname = request.user.last_name
        name = firstname + " " + lastname
        email = request.user.email
        key = "c7898f318b33426194a120118230205"
        lat = 82.48637
        lon = 135.31313
        resp = r.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lon}&aqi=no")
        re = json.loads(resp.text)
        city = re['location']['name']
        temp = re['current']['temp_c']
        sky = random.randint(0, 2)
        humidity = re['current']['humidity']
        rel_temp_c = re['current']['feelslike_c']
        weather = re['current']['condition']['text']
        if weather == "mist":
            weather = 3
        elif weather == "fog":
            weather = 1
        else:
            weather = 2
        state = re['location']['region']
        nation = re['location']['country']
        model = joblib.load('app/models/location_fetch.joblib')
        predict = [[weather, sky, humidity, temp, rel_temp_c]]
        location = model.predict(predict)
        data = Profile.objects.get(user_id=user_id)
        weight = float(data.Weight)
        height = float(data.Height)
        Ethnicity = 4
        date = data.date
        Gender = int(data.Gender)
        Age = float(data.Age)
        BMI = int(weight / (height ** 2))
        finalmodel = joblib.load('app/models/mainHydration_final_dt.joblib')
        parameters = [[Ethnicity, Gender, Age, BMI]]
        Hydra = finalmodel.predict(parameters)
        Hydration = float(Hydra + location)
        Hydra = round(Hydration, 2)

    return render(request, 'app/my_account.html',
                  {'instance': instance, 'name': name, 'email': email, 'hydration': Hydra, 'date': date})


def feedback(request):
    return render(request, 'app/feedback.html')


from datetime import datetime


def activity(request):
    if request.method == "POST":
        post = Activity()
        post.user_id = request.user.id
        user_id = post.user_id
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        post.UserName = request.user.username
        post.activity = request.POST.get('activity1')
        post.work_time = request.POST.get('activity')
        post.date = current_datetime
        activity = post.activity
        data = Profile.objects.get(user_id=user_id)
        hydration = float(data.Hydration)
        time = int(post.work_time)
        if time > 4:
            hydration = hydration + 1
        model = joblib.load('app/models/activito_decisiontree.joblib')
        para = [[activity, hydration, time]]
        value = model.predict(para)
        value1 = float(value + hydration)
        value2 = round(value1, 2)
        if value1:
            post.Hydration = value1
            post.save()
        return render(request, 'app/activito.html', {'value': value2})
