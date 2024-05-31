from django.contrib import admin
from .models import OtherInfo,History,Achieve
# Register your models here.
admin.site.register(OtherInfo)
admin.site.register(History)
admin.site.register(Achieve)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Alumni, UniversityBranch, Course
from .forms import AlumniForm

class AlumniAdmin(UserAdmin):
    model = Alumni
    add_form = AlumniForm
    form = AlumniForm
    list_display = ('registration_no', 'username', 'email', 'first_name', 'surname', 'branch', 'age')
    search_fields = ('registration_no', 'username', 'first_name', 'surname', 'email')
    ordering = ('registration_no', 'username')

    fieldsets = (
        (None, {'fields': ('registration_no', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'surname', 'email', 'phone',  'birthdate', 'age', 'sex', 'fiv_index', 'fvi_index')}),
        ('University info', {'fields': ('branch', 'course_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('registration_no', 'username', 'password', 'first_name', 'surname', 'email', 'phone',  'birthdate', 'age', 'sex', 'fiv_index', 'fvi_index', 'branch', 'course_name', 'is_staff', 'is_active')}
        ),
    )

    readonly_fields = ['age']

admin.site.register(Alumni, AlumniAdmin)
admin.site.register(UniversityBranch)
admin.site.register(Course)

