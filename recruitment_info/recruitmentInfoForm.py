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
            'phoneNumber': 'Phone Number',
            'fullAddress': 'Full Address',
            'nameOfUniversity': 'Name of University',
            'graduationYear': 'Graduation Year',
            'cgpa': 'CGPA',
            'experienceInMonths': 'Experience',
            'currentWorkPlaceName': 'Current Work Place',
            'applyingIn': 'Applying',
            'expectedSalary': 'Expected Salary',
            'fieldBuzzReference': 'Reference',
            'githubProjectUrl': 'Github Project URL',
            'cvFile': 'Upload CV'
        }

