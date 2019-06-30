from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns Flase for questions 
        whose pub_date is in the future.
        """