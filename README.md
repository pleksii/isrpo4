# Лабораторная работа №4: Unit-тестирование

## Описание

Проект демонстрирует применение unit-тестирования для проверки функций геометрических расчётов. Реализованы модули для работы с прямоугольниками и кругами с автоматизированными тестами на основе `unittest`.

**Файлы:**
- `rectangle.py` - модуль для прямоугольников (12 тестов)
- `circle.py` - модуль для кругов (10 тестов)

## Функциональность

### rectangle.py
- `area(length, width)` - площадь прямоугольника
- `perimeter(length, width)` - периметр прямоугольника

### circle.py
- `area(radius)` - площадь круга
- `circumference(radius)` - длина окружности

## Запуск тестов

```bash
# Все тесты
python -m unittest rectangle.py circle.py

# С подробным выводом
python -m unittest -v rectangle.py circle.py
```

## Пример использования

```python
from rectangle import area, perimeter
from circle import area as circle_area, circumference

area(5, 3)           # 15
perimeter(5, 3)      # 16
circle_area(5)       # 78.54
circumference(5)     # 31.42
```

## Результаты тестирования

- **Всего тестов:** 22
- **Пройдено:** 22 (100%)
- **Покрытие кода:** 100%
- **Время выполнения:** < 0.01 сек

```
$ python -m unittest rectangle.py circle.py
......................
----------------------------------------------------------------------
Ran 22 tests in 0.000s

OK
```

## Типы тестов

- Позитивные тесты (корректные вычисления)
- Граничные тесты (нулевые значения)
- Тесты с дробными числами
- Негативные тесты (обработка ошибок)

## GitHub Actions

Настроено автоматическое тестирование при каждом push:
- **OS:** Ubuntu & Windows
- **Workflow:** `.github/workflows/main.yml`
- Подробности в [GITHUB_ACTIONS.md](GITHUB_ACTIONS.md)

---

**Статус проекта:** Все тесты пройдены успешно
