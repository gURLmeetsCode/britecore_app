# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Risk(models.Model):
    risk_type = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField(default=0)
    zipCode = models.IntegerField(default=0)
    prize_amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name
