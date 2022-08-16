from django.db import models

class Group(models.Model):
	name = models.CharField(max_length=100, verbose_name="Название")

	class Meta():
		db_table = "Group"
		verbose_name_plural = "Группы"
		verbose_name = "Группа"
		ordering = ['-id']

	def __str__(self):
		return (f"Группа: {self.name}")

class Technology(models.Model):
	image = models.ImageField(upload_to="images/skills/", verbose_name="Изображение к навыку")
	name = models.CharField(max_length=100, verbose_name="Название")
	group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

	class Meta():
		db_table = "Technology"
		verbose_name_plural = "Технологии"
		verbose_name = "Технология"

	def __str__(self):
		return (f"#{self.id}")