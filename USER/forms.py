from django import forms


class LoginForm(forms.Form):
    registration_no = forms.CharField(max_length=50, label='Registration Number')
    password = forms.CharField(widget=forms.PasswordInput)

    
    
# forms.py
from django import forms
from .models import OtherInfo, History, Achieve

class OtherInfoForm(forms.ModelForm):
    class Meta:
        model = OtherInfo
        fields = '__all__'

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'

class AchieveForm(forms.ModelForm):
    class Meta:
        model = Achieve
        fields = '__all__'


from django import forms
from .models import Alumni, Course, UniversityBranch

from django import forms
from .models import Alumni, UniversityBranch, Course

class AlumniForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=UniversityBranch.objects.all(), required=True, widget=forms.Select(attrs={'id': 'branch'}))
    course_name = forms.ModelChoiceField(queryset=Course.objects.none(), required=True, widget=forms.Select(attrs={'id': 'course_name'}))

    class Meta:
        model = Alumni
        fields = ['surname', 'first_name', 'birthdate',  'sex', 'fiv_index', 'fvi_index', 'email', 'phone', 'branch', 'course_name', 'registration_no', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'branch' in self.data:
            try:
                branch_id = int(self.data.get('branch'))
                self.fields['course_name'].queryset = Course.objects.filter(branch_id=branch_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.branch:
            self.fields['course_name'].queryset = self.instance.branch.courses.order_by('name')


from django import forms
from .models import EducationalBackground

class EducationalBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = [
            'primary_school_name', 'primary_school_year_attended', 'primary_school_address',
            'secondary_school_name', 'secondary_school_year_attended', 'secondary_school_address',
            'veta_name', 'veta_program','veta_year_attended', 'veta_address',
            'college_name','college_program', 'college_year_attended', 'college_address',
            'university_name', 'university_course_title','university_relevant_course','university_graduation_year'
            
        ]
        widgets = {
            'primary_school_name': forms.TextInput(attrs={'placeholder': 'Primary School Name'}),
            'primary_school_year_attended': forms.TextInput(attrs={'placeholder': 'Year Attended'}),
            'primary_school_address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'secondary_school_name': forms.TextInput(attrs={'placeholder': 'Secondary School Name'}),
            'secondary_school_year_attended': forms.TextInput(attrs={'placeholder': 'Year Attended'}),
            'secondary_school_address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'veta_name': forms.TextInput(attrs={'placeholder': 'VETA Name'}),
            'veta_program': forms.TextInput(attrs={'placeholder': 'Program Attended'}),
            'veta_year_attended': forms.TextInput(attrs={'placeholder': 'Year Attended'}),
            'veta_address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'college_name': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'college_program': forms.TextInput(attrs={'placeholder': 'Program attended'}),
            'college_year_attended': forms.TextInput(attrs={'placeholder': 'Year Attended'}),
            'college_address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'university_name': forms.TextInput(attrs={'placeholder': 'university Name'}),
            'university_course_title': forms.TextInput(attrs={'placeholder': 'Bachelor/Degree of .....'}),
            'university_graduation_year': forms.TextInput(attrs={'placeholder': 'Graduation Year'}),
            'university_relevant_course': forms.Textarea(attrs={'placeholder': 'Relevant Course', 'cols': 60, 'rows': 5}),
            
        }