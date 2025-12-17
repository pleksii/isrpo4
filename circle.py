"""
Модуль для работы с кругами.
Содержит функции для вычисления площади и длины окружности.
"""

import math
import unittest


def area(radius):
    """
    Вычисляет площадь круга.
    
    Args:
        radius (float): Радиус круга
    
    Returns:
        float: Площадь круга
    
    Raises:
        ValueError: Если радиус отрицательный
    """
    if radius < 0:
        raise ValueError("Радиус должен быть неотрицательным")
    return math.pi * radius ** 2


def circumference(radius):
    """
    Вычисляет длину окружности.
    
    Args:
        radius (float): Радиус круга
    
    Returns:
        float: Длина окружности
    
    Raises:
        ValueError: Если радиус отрицательный
    """
    if radius < 0:
        raise ValueError("Радиус должен быть неотрицательным")
    return 2 * math.pi * radius


class CircleTestCase(unittest.TestCase):
    """Класс для тестирования функций работы с кругом"""
    
    # Тесты для функции area()
    def test_zero_area(self):
        """Тест: площадь круга с радиусом 0"""
        result = area(0)
        self.assertEqual(result, 0)
    
    def test_unit_circle_area(self):
        """Тест: площадь единичного круга"""
        result = area(1)
        self.assertAlmostEqual(result, math.pi, places=5)
    
    def test_circle_area(self):
        """Тест: площадь круга с радиусом 5"""
        result = area(5)
        self.assertAlmostEqual(result, 78.53981633974483, places=5)
    
    def test_area_with_float(self):
        """Тест: площадь круга с дробным радиусом"""
        result = area(2.5)
        self.assertAlmostEqual(result, 19.634954084936208, places=5)
    
    def test_area_negative_radius(self):
        """Тест: отрицательный радиус должен вызывать исключение"""
        with self.assertRaises(ValueError):
            area(-5)
    
    # Тесты для функции circumference()
    def test_zero_circumference(self):
        """Тест: длина окружности с радиусом 0"""
        result = circumference(0)
        self.assertEqual(result, 0)
    
    def test_unit_circle_circumference(self):
        """Тест: длина единичной окружности"""
        result = circumference(1)
        self.assertAlmostEqual(result, 2 * math.pi, places=5)
    
    def test_circle_circumference(self):
        """Тест: длина окружности с радиусом 5"""
        result = circumference(5)
        self.assertAlmostEqual(result, 31.41592653589793, places=5)
    
    def test_circumference_with_float(self):
        """Тест: длина окружности с дробным радиусом"""
        result = circumference(3.5)
        self.assertAlmostEqual(result, 21.991148575128552, places=5)
    
    def test_circumference_negative_radius(self):
        """Тест: отрицательный радиус должен вызывать исключение"""
        with self.assertRaises(ValueError):
            circumference(-5)


if __name__ == '__main__':
    unittest.main()

