from django.db import models

class Company(models.Model):
	logo = models.ImageField(upload_to="images/company/", verbose_name="Логотип")
	name = models.CharField(max_length=100, verbose_name="Название компании")
	position = models.CharField(max_length=100, verbose_name="Должность")
	description = models.CharField(max_length=255, verbose_name="Описание компании")
	city = models.CharField(max_length=50, null=True, verbose_name="Город", blank=True)
	hire_date = models.DateField(verbose_name="Дата приема на работу")
	day_of_dismissal = models.DateField(verbose_name="Дата увольнения", null=True, blank=True)
	link = models.CharField(max_length=255, verbose_name="Сайт компании", null=True, blank=True)

	class Meta():
		db_table = "Company"
		verbose_name_plural = "Компании"
		verbose_name = "Компания"

	def __str__(self):
		return (f"Компания: {self.name}")

class Responsibilities(models.Model):
	description = models.CharField(max_length=255, verbose_name="Описание")
	company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

	class Meta():
		db_table = "Responsibilities"
		verbose_name_plural = "Обязанности"
		verbose_name = "Обязанность"

	def __str__(self):
		return (f"#{self.id}")