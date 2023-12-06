from django.db import models

class articles(models.Model):
    title = models.CharField('Название', max_length=50) #Создаём поле с названием 'Название' и ограничиваем в 50 символов
    anons = models.CharField('Анонс', max_length=250) #Создаём поле с названием 'Анонс' и ограничиваем в 50 символов
    full_text = models.TextField('Статья') #Создаём поле с названием 'Статья' её кол-во символов может достигать до 20к
    date = models.DateTimeField('Дата публикации') #Создаём поле с названием 'Дата публикации'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'



    class Meta:
        verbose_name = 'Новость' #Имя таблички в единственном числе
        verbose_name_plural = 'Новости' #Имя таблички в множественном числе