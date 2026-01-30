from django.db import models


class StartupApplication(models.Model):
    # BASIC INFO
    startup_name = models.CharField(max_length=255)
    incorporation_status = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=50)
    incorporation_date = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255)
    address = models.TextField()
    sector = models.CharField(max_length=100)

    # FOUNDERS
    founders = models.CharField(max_length=255)
    designations = models.CharField(max_length=255)
    full_time = models.CharField(max_length=10)
    linkedin = models.TextField(blank=True)
    experience = models.TextField(blank=True)

    # CONTACT
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # BUSINESS STAGE
    stage = models.CharField(max_length=50)
    bootstrapped = models.CharField(max_length=10)
    capital = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    burn = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    traction = models.TextField(blank=True)

    # FUNDING
    raise_amount = models.DecimalField(max_digits=15, decimal_places=2)
    funding_stage = models.CharField(max_length=50)
    purpose = models.TextField()
    pitch_deck = models.FileField(upload_to="pitch_decks/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.startup_name


class InvestorApplication(models.Model):
    # INVESTOR INFO
    full_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    entity = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    experience = models.CharField(max_length=50)

    # CONTACT
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)

    # INVESTMENT MANDATE
    stages = models.JSONField(default=list)
    sectors = models.JSONField(default=list)
    geography = models.CharField(max_length=50)

    # TICKET SIZE
    ticket = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    deployment = models.CharField(max_length=50)

    # EXPERIENCE
    previous = models.CharField(max_length=10)
    count = models.CharField(max_length=50, blank=True)
    portfolio = models.TextField(blank=True)

    # ENGAGEMENT
    engagement = models.JSONField(default=list)
    involvement = models.CharField(max_length=50)

    # MOTIVATION
    motivation = models.JSONField(default=list)
    esg = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    i_am_a = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"