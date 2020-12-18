import re
import time
import requests
import uuid
import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from recruitment_info.recruitmentInfoForm import RecruitmentForm


def recruitment_con(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone_number = request.POST.get('phoneNumber', '')
    full_address = request.POST.get('fullAddress', '')
    name_of_university = request.POST.get('nameOfUniversity', '')
    graduation_year = request.POST.get('graduationYear', '')
    cgpa = request.POST.get('cgpa', '')
    experience_in_months = request.POST.get('experienceInMonths', '')
    current_work_place_name = request.POST.get('currentWorkPlaceName', '')
    applying_in = request.POST.get('applyingIn', '')
    expected_salary = request.POST.get('expectedSalary', '')
    field_buzz_reference = request.POST.get('fieldBuzzReference', '')
    github_project_url = request.POST.get('githubProjectUrl', '')
    cv_file = request.POST.get('cvFile', '')

    token = request.session.get('token')
    headers = {'Authorization': 'Token ' + token}

    on_spot_update_time = 0
    if on_spot_update_time == 0:
        on_spot_creation_time = int(round(time.time() * 1000))

    tsync_id = uuid.uuid1().hex
    cv_tsync_id = uuid.uuid1().hex
    on_spot_update_time = int(round(time.time() * 1000))

    payload = {"tsync_id": tsync_id,
               "name": name,
               "email": email,
               "phone": phone_number,
               "full_address": full_address,
               "name_of_university": name_of_university,
               "graduation_year": graduation_year,
               "cgpa": cgpa,
               "experience_in_months": experience_in_months,
               "current_work_place_name": current_work_place_name,
               "applying_in": applying_in,
               "expected_salary": expected_salary,
               "field_buzz_reference": field_buzz_reference,
               "github_project_url": github_project_url,
               "cv_file": {
                   "tsync_id": cv_tsync_id
               },
               "on_spot_update_time": on_spot_update_time,
               "on_spot_creation_time": on_spot_creation_time}

    response = requests.post('https://recruitment.fisdev.com/api/v0/recruiting-entities/',
                             data=json.dumps(payload),
                             headers={'Content-type': 'application/json; charset=UTF-8',
                                      'Authorization': 'Token ' + token,
                                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                                    'KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

    text = response.text
    obj = json.loads(text)

    if not obj['success']:
        temp_msg = obj['message']
        temp2 = temp_msg.split(": ")
        msg = temp2[1]
        messages.error(request, msg)
        return redirect('/recruitmentForm/')
    else:

        print("Upto 2nd API")
        print(obj['cv_file'])
        print(type(cv_file))
        file_token_id = str(obj['cv_file']['id'])
        obj['cv_file']['extension'] = 'null'
        obj['cv_file']['description'] = 'null'
        obj['cv_file']['file'] = cv_file
        url = 'https://recruitment.fisdev.com/api/file-object/' + file_token_id + '/'
        payload2 = obj['cv_file']
        response2 = requests.put(url, data=json.dumps(payload2), headers={'Content-type': 'application/json; '
                                                                                          'charset=UTF-8',
                                                                          'Authorization': 'Token ' + token,
                                                                          'User-Agent': 'Mozilla/5.0 (Windows NT '
                                                                                        '10.0; Win64; x64) '
                                                                                        'AppleWebKit/537.36 ( '
                                                                                        'KHTML, like Gecko) '
                                                                                        'Chrome/87.0.4280.88 '
                                                                                        'Safari/537.36'})

        print('-------------------------------------------------------')
        print('-------------------------------------------------------')
        print('-------------------------------------------------------')
        print(response2.status_code)
        print(response2.content)

        return HttpResponse(response2.json())
