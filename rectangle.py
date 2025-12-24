"""
Модуль для работы с прямоугольниками.
Содержит функции для вычисления площади и периметра.
"""

import unittest


def area(length, width):
    """
    Вычисляет площадь прямоугольника.
    
    Args:
        length (float): Длина прямоугольника
        width (float): Ширина прямоугольника
    
    Returns:
        float: Площадь прямоугольника
    
    Raises:
        ValueError: Если длина или ширина отрицательные
    """
    if length < 0 or width < 0:
        raise ValueError("Длина и ширина должны быть неотрицательными")
    return length * width


def perimeter(length, width):
    """
    Вычисляет периметр прямоугольника.
    
    Args:
        length (float): Длина прямоугольника
        width (float): Ширина прямоугольника
    
    Returns:
        float: Периметр прямоугольника
    
    Raises:
        ValueError: Если длина или ширина отрицательные
    """
    if length < 0 or width < 0:
        raise ValueError("Длина и ширина должны быть неотрицательными")
    return 2 * (length + width)


class RectangleTestCase(unittest.TestCase):
    """Класс для тестирования функций работы с прямоугольником"""
    
    # Тесты для функции area()
    def test_zero_area(self):
        """Тест: площадь при одной нулевой стороне должна быть 0"""
        result = area(10, 0)
        self.assertEqual(result, 0)
    
    def test_square_area(self):
        """Тест: площадь квадрата 10x10"""
        result = area(10, 10)
        self.assertEqual(result, 100)
    
    def test_rectangle_area(self):
        """Тест: площадь прямоугольника 5x3"""
        result = area(5, 3)
        self.assertEqual(result, 15)
    
    def test_area_with_float(self):
        """Тест: площадь с дробными числами"""
        result = area(2.5, 4.0)
        self.assertEqual(result, 10.0)
    
    def test_area_negative_length(self):
        """Тест: отрицательная длина должна вызывать исключение"""
        with self.assertRaises(ValueError):
            area(-5, 10)
    
    def test_area_negative_width(self):
        """Тест: отрицательная ширина должна вызывать исключение"""
        with self.assertRaises(ValueError):
            area(10, -5)
    
    # Тесты для функции perimeter()
    def test_zero_perimeter(self):
        """Тест: периметр при нулевых сторонах"""
        result = perimeter(0, 0)
        self.assertEqual(result, 0)
    
    def test_square_perimeter(self):
        """Тест: периметр квадрата 10x10"""
        result = perimeter(10, 10)
        self.assertEqual(result, 40)
    
    def test_rectangle_perimeter(self):
        """Тест: периметр прямоугольника 5x3"""
        result = perimeter(5, 3)
        self.assertEqual(result, 16)
    
    def test_perimeter_with_float(self):
        """Тест: периметр с дробными числами"""
        result = perimeter(2.5, 3.5)
        self.assertEqual(result, 12.0)
    
    def test_perimeter_negative_length(self):
        """Тест: отрицательная длина должна вызывать исключение"""
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
    
    def test_perimeter_negative_width(self):
        """Тест: отрицательная ширина должна вызывать исключение"""
        with self.assertRaises(ValueError):
            perimeter(10, -5)


if __name__ == '__main__':
    unittest.main()


