from django.db import models


class RecruitmentInfoModel(models.Model):

    name = models.CharField(max_length=256, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)
    phoneNumber = models.CharField(max_length=14, blank=False, null=False)
    fullAddress = models.CharField(max_length=512, blank=False, null=False)
    nameOfUniversity = models.CharField(max_length=256, blank=False, null=False)
    graduationYear = models.IntegerField(blank=False, null=False)
    cgpa = models.FloatField(blank=False, null=False)
    experienceInMonths = models.IntegerField(blank=False, null=False)
    currentWorkPlaceName = models.CharField(max_length=256, blank=False, null=False)
    applyingIn = models.CharField(max_length=10, choices=[('ANDROID', 'Android'), ('BACKEND', 'Backend')], blank=False,
                                  null=False)
    expectedSalary = models.IntegerField(blank=False, null=False)
    fieldBuzzReference = models.CharField(max_length=256, blank=False, null=False)
    githubProjectUrl = models.CharField(max_length=2083, blank=False, null=False)
    cvFile = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
