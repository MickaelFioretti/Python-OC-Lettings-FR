from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )

    def test_profile_creation(self):
        profile = Profile.objects.create(user=self.user, favorite_city="Paris")
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.favorite_city, "Paris")

    def test_profile_str_method(self):
        profile = Profile.objects.create(user=self.user, favorite_city="London")
        self.assertEqual(str(profile), "testuser")

    def test_profile_blank_favorite_city(self):
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.favorite_city, "")
