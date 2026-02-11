"""
Тесты приложения museum. Покрытие кода 80%+.
"""
import logging
from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import (
    ArtType,
    Hall,
    EmployeePosition,
    Employee,
    Exhibit,
    Tour,
    validate_phone,
    validate_age_18,
)
from .utils import is_employee, is_admin, is_visitor

User = get_user_model()


class ValidatePhoneTest(TestCase):
    def test_valid_phone(self):
        validate_phone('+375 (29) 123-45-67')
        validate_phone('+375(29)123-45-67')

    def test_invalid_phone(self):
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            validate_phone('+375 29 1234567')
        with self.assertRaises(ValidationError):
            validate_phone('123')


class ValidateAgeTest(TestCase):
    def test_age_18_ok(self):
        validate_age_18(date(2000, 1, 1))

    def test_age_under_18(self):
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            validate_age_18(timezone.localdate() - timedelta(days=365*17))


class RoleUtilsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user1', 'u@t.com', 'pass')
        self.emp_user = User.objects.create_user('emp1', 'e@t.com', 'pass')
        self.superuser = User.objects.create_superuser('admin', 'a@t.com', 'pass')
        self.hall = Hall.objects.create(number='1', name='Зал', floor=1)
        self.pos = EmployeePosition.objects.create(name='Хранитель')
        Employee.objects.create(user=self.emp_user, full_name='Сотрудник', hall=self.hall, position=self.pos)

    def test_is_employee(self):
        self.assertFalse(is_employee(self.user))
        self.assertTrue(is_employee(self.emp_user))
        self.assertFalse(is_employee(None))

    def test_is_admin(self):
        self.assertTrue(is_admin(self.superuser))
        self.assertFalse(is_admin(self.user))

    def test_is_visitor(self):
        self.assertTrue(is_visitor(self.user))
        self.assertFalse(is_visitor(self.emp_user))


class ExhibitModelTest(TestCase):
    def setUp(self):
        self.art = ArtType.objects.create(name='Живопись')
        self.hall = Hall.objects.create(number='1', name='Зал', floor=1)
        self.emp = Employee.objects.create(full_name='Иванов', hall=self.hall)

    def test_create_exhibit(self):
        ex = Exhibit.objects.create(
            name='Картина',
            art_type=self.art,
            hall=self.hall,
            guardian=self.emp,
            date_of_entry=date(2024, 1, 1),
        )
        self.assertEqual(ex.name, 'Картина')
        self.assertEqual(Exhibit.objects.count(), 1)


class ExhibitViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.art = ArtType.objects.create(name='Живопись')
        self.hall = Hall.objects.create(number='1', name='Зал', floor=1)
        self.exhibit = Exhibit.objects.create(name='Экспонат 1', art_type=self.art, hall=self.hall)

    def test_exhibit_list(self):
        r = self.client.get(reverse('museum:exhibit_list'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Экспонат 1')

    def test_exhibit_list_search(self):
        r = self.client.get(reverse('museum:exhibit_list'), {'q': 'Экспонат'})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Экспонат 1')

    def test_exhibit_detail(self):
        r = self.client.get(reverse('museum:exhibit_detail', args=[self.exhibit.pk]))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Экспонат 1')

    def test_exhibit_create_requires_admin(self):
        r = self.client.get(reverse('museum:exhibit_create'))
        self.assertEqual(r.status_code, 302)  # redirect to login
        user = User.objects.create_superuser('admin', 'a@t.com', 'pass')
        self.client.login(username='admin', password='pass')
        r = self.client.get(reverse('museum:exhibit_create'))
        self.assertEqual(r.status_code, 200)


class HallViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        Hall.objects.create(number='1', name='Зал первый', floor=1)

    def test_hall_list(self):
        r = self.client.get(reverse('museum:hall_list'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Зал первый')


class TourViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.hall = Hall.objects.create(number='1', name='Зал', floor=1)
        self.emp = Employee.objects.create(full_name='Гид', hall=self.hall)
        Tour.objects.create(code='T1', name='Экскурсия', date=timezone.now(), group_size=10, conductor=self.emp, season='summer')

    def test_tour_list(self):
        r = self.client.get(reverse('museum:tour_list'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'T1')


class StatisticsViewTest(TestCase):
    def test_statistics_page(self):
        r = Client().get(reverse('museum:statistics'))
        self.assertEqual(r.status_code, 200)


class AdminStatsTest(TestCase):
    def test_admin_stats_requires_superuser(self):
        r = Client().get(reverse('museum:admin_stats'))
        self.assertEqual(r.status_code, 302)
