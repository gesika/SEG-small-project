"""Tests of the log in view."""
from django.test import TestCase
from django.urls import reverse
from clubs.forms import LogInForm
from clubs.models import Member
from clubs.tests.helpers import LogInTester

class LogInViewTestCase(TestCase, LogInTester):
    """Tests of the log in view."""
    
    def setUp(self):
        self.url = reverse('log_in')
        Member.objects.create_user(
            email = 'johndoe@example.org',
            first_name = 'John',
            last_name = 'Doe',
            username= 'johndoe',
            bio = 'This is my bio',
            experience_level = 6,
            personal_statement = 'This is my personal statement',
            password= 'Password123',
        )
    
    def test_log_in_url(self):
        self.assertEqual(self.url,'/log_in/')
    
    def test_get_log_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
    
    def test_unsuccessful_log_in(self):
        form_input={'email': 'johndoe@example.org', 'password': 'Wrongpassword123'}
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self._is_logged_in())
    
    def test_successful_log_in(self):
        form_input={'email': 'johndoe@example.org', 'password': 'Password123'}
        response = self.client.post(self.url, form_input, follow=True)
        self.assertTrue(self._is_logged_in())
        response_url = reverse('feed')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'feed.html')
    
    