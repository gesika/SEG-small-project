"""Tests of the sign up view."""
from django.test import TestCase
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from clubs.forms import SignUpForm
from clubs.models import Member

class SignUpViewTestCase(TestCase):
    """Tests of the sign up view."""
    
    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': 'janedoe',
            'email': 'janedoe@example.org',
            'bio': 'This is my bio',
            'experience_level': 6,
            'personal_statement': 'This is my personal_statement',
            'new_password': 'Password123',
            'password_confirmation': 'Password123',
        }
    
    def test_sign_up_url(self):
        self.assertEqual(self.url,'/sign_up/')
    
    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertFalse(form.is_bound)
    
    def test_unsuccessful_sign_up(self):
        self.form_input['username'] = 'BAD_USERNAME'
        before_count = Member.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = Member.objects.count()
        self.assertEqual(after_count, before_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)
        #self.assertFalse(self._is_logged_in())
    
    def test_successful_sign_up(self):
        before_count = Member.objects.count()
        response = self.client.post(self.url, self.form_input, follow=True)
        after_count = Member.objects.count()
        self.assertEqual(after_count, before_count+1)
        response_url = reverse('feed')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'feed.html')
        user = Member.objects.get(username='janedoe')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'janedoe@example.org')
        self.assertEqual(user.bio, 'This is my bio')
        self.assertEqual(user.experience_level, 6)
        self.assertEqual(user.personal_statement, 'This is my personal_statement')
        is_password_correct = check_password('Password123', user.password)
        self.assertTrue(is_password_correct)
        #self.assertTrue(self._is_logged_in())"""