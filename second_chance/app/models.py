from django.db import models
import datetime


class Industry(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.name



class Employer(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    hq_address = models.CharField(max_length=255, null=True, blank=True)
    hq_in_dc = models.BooleanField(default=False)
    home_url = models.CharField(max_length=255, null=True, blank=True)
    employment_url = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    box_present = models.IntegerField(null=True, blank=True)
    crime_type_asked = models.IntegerField(null=True, blank = True) # 1 = "crime", 2="misdemeanor", 3="felony"
    years_specified_by_box = models.IntegerField(null=True, blank = True)
    industries = models.ManyToManyField(Industry, null=True, blank=True)
    # vetted = models.BooleanField(default = False)
    # day_care = models.BooleanField(default = False)
    # federal_bonding = models.BooleanField(default = False)
    # retention_programs  = models.BooleanField(default = False)
    # professional_development = models.BooleanField(default = False)
    # clean_record_on_abusive_practices = models.BooleanField(default = False)

    # def calculate_score(self):



    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.name


class Position(models.Model):
    employer = models.ForeignKey(Employer)
    title = models.CharField(max_length=40)
    phone = models.CharField(max_length=40, null=True, blank=True)
    worksite_location = models.CharField(max_length=255, null=True, blank=True)
    job_posted = models.CharField(max_length = 40, null=True, blank = True)
    collateral_sanction_applies = models.BooleanField(default=True)
    which_collateral_sanction_applies = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.title


class UserReview(models.Model):
    employer = models.ForeignKey(Employer)
    position = models.ForeignKey(Position, null=True, blank=True)
    title = models.CharField(max_length=40)
    notes = models.TextField(null=True, blank=True)
    date_of_action = models.CharField(max_length=40, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.id