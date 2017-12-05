# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Risk
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):

    """This class defines the test suite for the risk model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.risk_object_name = "Write world class code"
        self.risk_object = Risk(risk_type=self.risk_object_name)

    def test_model_can_create_a_risk_object(self):
        """Test the risk model can create a risk object."""
        old_count = Risk.objects.count()
        self.risk_object.save()
        new_count = Risk.objects.count()
        self.assertNotEqual(old_count, new_count)



class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.risk_data = {'first_name': 'Foo'}
        self.response = self.client.post(
            reverse('home'),
            self.risk_data,
            format="json")

    def test_api_can_create_a_risk(self):
        """Test the api has risk creation capability."""
        self.assertTrue(status.is_success(self.response.status_code))

    def test_api_can_post_a_risk_field(self):
        """Test the api can post a given field to risk model."""
        client = APIClient()
        response = self.client.post('/', {'title': 'new idea'}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
