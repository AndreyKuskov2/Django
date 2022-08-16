from operator import mod
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import projects, skills, experience

class AccomplishmentsInLine(admin.StackedInline):
	model = projects.Accomplishment

@admin.register(projects.Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("name", "description", "github_link_url", "other_link_url",)
	search_fields = ("name",)
	search_help_text = "Поиск по имени"
	inlines = [AccomplishmentsInLine,]

	def github_link_url(self, obj):
		return format_html("<a href='{url}'>{url}</a>", url=obj.github_link)

	def other_link_url(self, obj):
		if (obj.other_link):
			return format_html("<a href='{url}'>{url}</a>", url=obj.other_link)

	github_link_url.short_description = "Ссылка на GitHub проекта"
	other_link_url.short_description = "Ссылка на сторонний ресурс"



class TechnologyInLine(admin.StackedInline):
	model = skills.Technology

@admin.register(skills.Group)
class GroupAdmin(admin.ModelAdmin):
	inlines = [TechnologyInLine,]



class ResponsibilitiesInLine(admin.StackedInline):
	model = experience.Responsibilities

@admin.register(experience.Company)
class CompanyAdmin(admin.ModelAdmin):
	inlines = [ResponsibilitiesInLine,]
