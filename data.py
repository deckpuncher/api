from jobseeker.models import Jobseeker
from django.utils import timezone

jsk = Jobseeker()
jsk.FirstName = "Joe"
jsk.LastName = "Bloggs"
jsk.dob = timezone.now().date()
jsk.Email = "fake@fake.com"

jsk.save()
