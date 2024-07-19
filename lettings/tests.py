from django.core.exceptions import ValidationError
from django.test import TestCase
from lettings.models import Address, Letting
from django.urls import reverse

# --- addresses ---


class AddressTest(TestCase):
    def test_address_creation(self):
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="ST",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.assertEqual(address.number, 123)
        self.assertEqual(address.street, "Main St")
        self.assertEqual(address.city, "City")
        self.assertEqual(address.state, "ST")
        self.assertEqual(address.zip_code, 12345)
        self.assertEqual(address.country_iso_code, "USA")

    def test_address_validation(self):
        address = Address(
            number=10000,
            street="Main St",
            city="City",
            state="ST",
            zip_code=12345,
            country_iso_code="USA",
        )
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_address_state_validation(self):
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="S",
            zip_code=12345,
            country_iso_code="USA",
        )

        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_address_zip_code_validation(self):
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="ST",
            zip_code=100000,
            country_iso_code="USA",
        )
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_address_country_iso_code_validation(self):
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="ST",
            zip_code=12345,
            country_iso_code="US",
        )
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_address_str_method(self):
        address = Address(
            number=123,
            street="Main St",
            city="City",
            state="ST",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.assertEqual(str(address), "123 Main St")


# --- lettings ---


class LettingTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="ST",
            zip_code=12345,
            country_iso_code="USA",
        )

    def test_letting_creation(self):
        letting = Letting.objects.create(
            title="Beautiful Apartment",
            address=self.address,
        )
        self.assertEqual(letting.title, "Beautiful Apartment")
        self.assertEqual(letting.address, self.address)

    def test_letting_str_method(self):
        letting = Letting(
            title="Beautiful Apartment",
            address=self.address,
        )
        self.assertEqual(str(letting), "Beautiful Apartment")

    def test_letting_required_fields(self):
        # Test for required fields
        with self.assertRaises(ValidationError):
            Letting.objects.create(address=self.address).full_clean()

    def test_letting_index_view(self):
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings_index.html")
