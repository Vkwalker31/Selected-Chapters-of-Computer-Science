"""
Тесты приложения pages.
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Article, News, FAQ, Review, PromoCode

User = get_user_model()


class HomeViewTest(TestCase):
    def test_home(self):
        r = Client().get(reverse('pages:home'))
        self.assertEqual(r.status_code, 200)

    def test_home_with_article(self):
        Article.objects.create(title='Тест', content='Текст', is_published=True)
        r = Client().get(reverse('pages:home'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Тест')


class NewsViewTest(TestCase):
    def test_news_list(self):
        r = Client().get(reverse('pages:news_list'))
        self.assertEqual(r.status_code, 200)

    def test_news_detail(self):
        n = News.objects.create(title='Новость', summary='Кратко', content='Полный текст')
        r = Client().get(reverse('pages:news_detail', args=[n.pk]))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Новость')


class FAQViewTest(TestCase):
    def test_faq_list(self):
        r = Client().get(reverse('pages:faq_list'))
        self.assertEqual(r.status_code, 200)


class ReviewsViewTest(TestCase):
    def test_reviews_list(self):
        r = Client().get(reverse('pages:reviews'))
        self.assertEqual(r.status_code, 200)

    def test_review_add_requires_login(self):
        r = Client().get(reverse('pages:review_add'))
        self.assertEqual(r.status_code, 302)

    def test_review_add_post(self):
        user = User.objects.create_user('u', 'u@t.com', 'pass')
        c = Client()
        c.login(username='u', password='pass')
        r = c.post(reverse('pages:review_add'), {'rating': 5, 'text': 'Отличный музей!'})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)


class PromoViewTest(TestCase):
    def test_promo_list(self):
        r = Client().get(reverse('pages:promo_list'))
        self.assertEqual(r.status_code, 200)


class RegisterViewTest(TestCase):
    def test_register_get(self):
        r = Client().get(reverse('pages:register'))
        self.assertEqual(r.status_code, 200)

    def test_register_post(self):
        r = Client().post(reverse('pages:register'), {
            'username': 'newuser',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
        })
        self.assertEqual(r.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
