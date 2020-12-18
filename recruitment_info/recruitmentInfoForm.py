from django import forms
from .models import RecruitmentInfoModel


class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = RecruitmentInfoModel
        fields = ('name', 'email', 'phoneNumber', 'fullAddress', 'nameOfUniversity', 'graduationYear', 'cgpa',
                  'experienceInMonths', 'currentWorkPlaceName', 'applyingIn', 'expectedSalary', 'fieldBuzzReference',
                  'githubProjectUrl', 'cvFile')
        labels = {
            'name': 'Name',
            'email': 'E-mail',
            'phoneNumber': 'Phone number',
            'fullAddress': 'Full-address',
            'nameOfUniversity': 'Name of university',
            'graduationYear': 'Graduation year',
            'cgpa': 'CGPA',
            'experienceInMonths': 'Experience',
            'currentWorkPlaceName': 'Current work place',
            'applyingIn': 'Applying',
            'expectedSalary': 'Expected salary',
            'fieldBuzzReference': 'Reference',
            'githubProjectUrl': 'Github project url',
            'cvFile': 'Upload CV'
        }

