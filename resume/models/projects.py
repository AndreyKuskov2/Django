from django.db import models

class Project(models.Model):
	image = models.ImageField(upload_to="images/", verbose_name="Изображение")
	name = models.CharField(max_length=100, verbose_name="Название")
	description = models.CharField(max_length=100, verbose_name="Описание")
	github_link = models.CharField(max_length=100, verbose_name="Ссылка на GitHub проекта")
	other_link = models.CharField(max_length=100, null=True, verbose_name="Ссылка на сторонний ресурс", blank=True)

	class Meta:
		db_table = "Project"
		verbose_name_plural = "Проекты"
		verbose_name = "Проект"

	def __str__(self):
		return (f"Проект: {self.name}")

class Accomplishment(models.Model):
	achievements = models.CharField(max_length=100, verbose_name="Достижение в проекте")
	project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

	class Meta:
		db_table = "Accomplishment"
		verbose_name_plural = "Достижения"
		verbose_name = "Достижение"

	def __str__(self):
		return (f"#{self.id}")