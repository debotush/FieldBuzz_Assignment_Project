from django.shortcuts import render

from recruitment_info.models import RecruitmentInfoModel
from recruitment_info.recruitmentInfoForm import RecruitmentForm
from recruitment_info.recruitmentController import recruitment_con


def recruitment_index(request):

    if request.method == 'GET':
        form = RecruitmentForm()
    else:
        form = RecruitmentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print("Valid")
            print(request.FILES['cvFile'])
            file = request.FILES['cvFile']
            form.save()
            return recruitment_con(request)

    return render(request, 'recruitmentForm.html', {'form': form})
