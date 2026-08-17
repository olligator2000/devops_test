from django.test import TestCase
from django.urls import reverse


class GalleryTests(TestCase):
    def test_homepage_returns_200(self):
        """Проверяем, что главная страница работает (код 200)"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        """Проверяем, что используется шаблон gallery.html"""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'gallery.html')

    def test_homepage_contains_basic_elements(self):
        """Проверяем, что на странице есть ключевые элементы"""
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Галерея')  # текст из заголовка
        self.assertContains(response, 'DEVOPS')  # текст из бегущей строки