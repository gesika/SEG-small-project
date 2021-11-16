from django.core.exceptions import ValidationError
from django.test import TestCase
from clubs.models import Member

# Create your tests here.
class MemberModelTestCase(TestCase):
    def setUp(self):
        self.member = Member.objects.create_user(
            username = 'johndoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@example.org',
            bio = 'This is my bio',
            experience_level = 6,
            personal_statement = 'This is my personal statement'
        )

    def test_valid_member(self):
        self._assert_member_is_valid()
    
    def test_username_cannot_be_blank(self):
        self.member.username = ''
        self._assert_member_is_invalid()
    
    def test_username_can_be_30_characters_long(self):
        self.member.username = 'x' * 30
        self._assert_member_is_valid()
    
    def test_username_cannot_be_over_30_characters_long(self):
        self.member.username = 'x' * 31
        self._assert_member_is_invalid()
    
    def _assert_member_is_valid(self):
        try:
            self.member.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')
    
    
    def test_first_name_must_not_be_blank(self):
        self.member.first_name = ''
        self._assert_member_is_invalid()
    
    
    def test_first_name_may_contain_50_characters(self):
        self.member.first_name ='x' * 50
        self._assert_member_is_valid()
        
    def test_first_name_may_not_contain_50_characters(self):
        self.member.first_name = 'x' * 51
        self._assert_member_is_invalid()
    
    def test_last_name_must_not_be_blank(self):
        self.member.last_name = ''
        self._assert_member_is_invalid()
    
    def test_last_name_may_contain_50_characters(self):
        self.member.last_name ='x' * 50
        self._assert_member_is_valid()

    def test_last_name_may_not_contain_50_characters(self):
        self.member.last_name = 'x' * 51
        self._assert_member_is_invalid()
    
    def test_email_must_not_be_blank(self):
        self.member.email = ''
        self._assert_member_is_invalid()
    
    def test_email_must_contain_username(self):
        self.member.email = '@example.org'
        self._assert_member_is_invalid()

    def test_email_must_contain_at_symbol(self):
        self.member.email = 'johndoe.example.org'
        self._assert_member_is_invalid()

    def test_email_must_contain_domain_name(self):
        self.member.email = 'johndoe@.org'
        self._assert_member_is_invalid()

    def test_email_must_contain_domain(self):
        self.member.email = 'johndoe@example'
        self._assert_member_is_invalid()

    def test_email_must_not_contain_more_than_one_at(self):
        self.member.email = 'johndoe@@example.org'
        self._assert_member_is_invalid()
    
    def test_bio_may_be_blank(self):
        self.member.bio = ''
        self._assert_member_is_valid()
    
    def test_bio_may_contain_520_characters(self):
        self.member.bio = 'x' * 520
        self._assert_member_is_valid()

    def test_bio_must_not_contain_more_than_520_characters(self):
        self.member.bio = 'x' * 521
        self._assert_member_is_invalid()

    
    def _assert_member_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.member.full_clean()
