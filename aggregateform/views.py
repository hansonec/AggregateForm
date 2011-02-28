# Create your views here.

from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.forms.formsets import formset_factory
from django.core.context_processors import csrf

class AggregateForm():
	def __init__(self, *args):
		self.forms = []
		for form in args:
			self.forms.append(form)
	def add_form(self, form):
		self.forms.append(form)
	def __iter__(self):
		return self.forms.__iter__()

class Form1(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField()

class Form2(forms.Form):
	 junk = forms.CharField(max_length=100)
	 not_junk = forms.EmailField()

def index(request):
	if request.method == 'POST':
		aggform = Form1(request.POST)
		if aggform.is_valid():
			return HttpResponse('Success!')
	else:
		aggform = AggregateForm(Form1(), Form2())

	return render_to_response('test_form1.html', {'aggform': aggform,})

