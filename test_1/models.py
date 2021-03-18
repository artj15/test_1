from django.db import models
from django.urls import reverse
# Create your models here.
class Menu(models.Model):
    logo = models.FileField(upload_to= 'test_1/static/')
    menu_text_1 = models.TextField()
    menu_text_2 = models.TextField()
    menu_text_3 = models.TextField()
    menu_text_4 = models.TextField()
    text_lk = models.TextField()
    def __str__(self):
        return f'{self.logo}, {self.menu_text_1}, {self.menu_text_2}, {self.menu_text_3}, {self.menu_text_4}, {self.text_lk}'
    '''def get_absolute_url(self):
        return reverse('index')'''
class About(models.Model):
    header = models.TextField()
    img = models.FileField(upload_to= 'test_1/static/')
    main_h = models.TextField()
    main_p_1 = models.FileField(upload_to= 'test_1/static/')
    main_p_2 = models.FileField(upload_to= 'test_1/static/')
    main_p_3 = models.FileField(upload_to= 'test_1/static/')
    footer = models.TextField()
    def __str__(self):
        return f'{self.header}, {self.img}, {self.main_h}, {self.main_p_1}, {self.main_p_2}, {self.main_p_3}, {self.footer}'
    '''def get_absolute_url(self):
        return reverse('index')'''
    
class MainIndex(models.Model):
    index_h1 = models.TextField()
    index_h2 = models.TextField()
    index_a_1 = models.TextField()
    index_a_2 = models.TextField()
    index_img = models.FileField(upload_to= 'test_1/static/')
  
class Forwhom(models.Model):
    forwhom_h1 = models.TextField()
    forwhom_h2 = models.TextField()
    forwhom_td_1_img = models.FileField(upload_to= 'test_1/static/')
    forwhom_td_1 = models.TextField()
    forwhom_td_2_img = models.FileField(upload_to= 'test_1/static/')
    forwhom_td_2 = models.TextField()
    forwhom_td_3_img = models.FileField(upload_to= 'test_1/static/')
    forwhom_td_3_img_byce = models.FileField(upload_to= 'test_1/static/')
    forwhom_td_3 = models.TextField()
    forwhom_td_4_img = models.FileField(upload_to= 'test_1/static/')
    forwhom_td_4 = models.TextField()
    
class Freeles(models.Model):
    first_name = models.TextField()
    email = models.TextField()
    message = models.TextField()
    text_left_1 = models.TextField()
    text_left_2 = models.TextField()
    text_left_3 = models.TextField()
    def __str__(self):
        return f'{self.first_name} {self.email} {self.message}'




'''  
class Format(models.Model):
    pass

class Authors(models.Model):
    pass
'''
