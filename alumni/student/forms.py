from django import forms

from .models import studinfo1

class StudinfoForm(forms.ModelForm):

	class Meta:
		model= studinfo1
		fields= ('name','lastname', 'idnumber', 'jobstatus', 'passout', 'branch', 'email', 'mobile')