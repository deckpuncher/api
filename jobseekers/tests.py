import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Jobseeker

# Create your tests here.
class JobseekerTests(TestCase):
    earliestDob = (timezone.now() - datetime.timedelta(weeks=728)).date()

    def test_jobseeker_is_14_years_old_can_clean(self):
        """
        new jobseekers must be 14 years or older
        """
        under_test = Jobseeker()
        under_test.JobseekerId = 12345678
        under_test.DOB = self.earliestDob

        try:
            under_test.clean()
        except:
            self.fail("Valid Date of Birth not accepted")

    def test_jobseeker_is_less_than_14_years_old_cannot_clean(self):
        """
        new jobseekers must be 14 years or older
        """
        invalidDob = self.earliestDob + datetime.timedelta(days=1)

        under_test = Jobseeker()
        under_test.JobseekerId = 12345678
        under_test.DOB = invalidDob

        self.assertRaises(ValidationError, under_test.clean)
