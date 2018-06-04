from django.db import models
from django.urls import reverse
# from image_ann.views import hit
# Create your models here.

class Hit(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='')
    body = models.CharField(max_length= 400, default='ADD ANNOTATIONS HERE')
    keywords = models.CharField(max_length=200, null=True, blank=True)
    max_assignments = models.IntegerField(default=1, null=True, blank=True)
    payment = models.FloatField(default=0.05, null=True, blank=True)
    duration = models.IntegerField(default=30, null=True, blank=True)
    approval_delay = models.IntegerField(default=60*3, null=True, blank=True)
    lifetime = models.IntegerField(default=60*24, null=True, blank=True)
    # image = models.ForeignKey(Image, related_name = 'hit', on_delete=models.CASCADE)
    # the HIT ID on MTurk
    hit_id= models.CharField(max_length = 50, db_index = True, unique = True)


    def get_absolute_url(self):
        return reverse('hit')
    # def get_absolute_url(self):
    #     # return reverse("hit")
    #     return reverse('hit')
    def __str__(self):
        return self.hit_id


# class Result(models.Model):
#   # the image on which this result applies
#   # image = models.ForeignKey(Image, related_name = 'results', on_delete=models.CASCADE)
#
#   # the content of the response
#   content = models.TextField(max_length = 2048, blank = False, null = False)
#
#   # Amazon related stuff
#   assignment_id = models.CharField(max_length = 50, db_index = True, unique = True)
#   # the associated hit, if already processed
#   hit   = models.ForeignKey(Hit, null = False, on_delete=models.CASCADE)
#
#   def __str__(self):
#       return self.content
