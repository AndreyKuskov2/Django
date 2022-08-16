from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import projects as pj, skills as sk, experience as ex

from django.views.generic import TemplateView
from django.core.cache import cache

class HomePage(TemplateView):
	template_name = "resume/base.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['projects'] = pj.Project.objects.all()
		context['accomplishment'] = pj.Accomplishment.objects.all().select_related('project_id')

		skills_technologies = cache.get_many(['skills', 'technologies'])
		if (not skills_technologies):
			skills = sk.Group.objects.all()
			technologies = sk.Technology.objects.all().select_related('group_id')
			cache.set_many({'skills': skills, 'technologies': technologies}, 60)
		else:
			skills = skills_technologies['skills']
			technologies = skills_technologies['technologies']
	
		context['skills'] = skills
		context['technologies'] = technologies
		context['companies'] = ex.Company.objects.all()
		context['responsibilities'] = ex.Responsibilities.objects.all().select_related('company_id')
		return context
