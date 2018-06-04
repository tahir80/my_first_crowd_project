from django.core.management.base import BaseCommand, CommandError
from django.urls import reverse
from django.conf import settings
from image_ann.models import Hit

import boto
import boto.mturk
import boto.mturk.connection

_mturk_connexion = None

title = 'add annotations'
Description = "Simple Task"
Keywords = None
Reward = 0.02
MaxAssignments = 1
LifetimeInSeconds = 172800
AssignmentDurationInSeconds = 600
AutoApprovalDelayInSeconds = 14400

# Keywords=[k.replace(',', '') for k in hit_type.keywords.split()]

def get_connection():
  global _mturk_connexion

  if _mturk_connexion is None:
    _mturk_connexion = boto.mturk.connection.MTurkConnection(
       aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
       aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
       debug=True,
       host=settings.AWS_HOST)

  return _mturk_connexion


def create_external_question_hit(url):
  question = boto.mturk.question.ExternalQuestion(url, 500)
  new_hit = get_connection().create_hit(
                question=question,
                title=title,
                description=Description,
                reward=0.02,
                max_assignments = MaxAssignments,
                lifetime = LifetimeInSeconds,
                duration = AssignmentDurationInSeconds,
                approval_delay = AutoApprovalDelayInSeconds,
                keywords=Keywords
                )
  return new_hit

class Command(BaseCommand):

    help = "Create new Hit"
    def handle(self, *args, **options):

        #this function will first create connection. see above
        hit = Hit(hit_id='?', title=title, description = Description)
        # keywords=[k.replace(',', '') for k in hit.keywords.split()]
        # print(type(hit.get_absolute_url()))
        new_hit = create_external_question_hit(settings.URL_ROOT + hit.get_absolute_url())
        # first grab hit_id from newly created Hit object and add it to Hit Model class
        hit.hit_id = new_hit[0].HITId
        self.stdout.write("https://workersandbox.mturk.com/mturk/preview?groupId=" +new_hit[0].HITId)
        hit.save()
