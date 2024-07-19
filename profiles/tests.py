from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse


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

    def test_profile_index_view(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles_index.html")
