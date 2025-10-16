# Тестирование торговой стратегии на двух скользящих средних

**Источник:** [OsEngine](https://github.com/AlexWan/OsEngine)  
**Стратегия:** Lesson3Bot3.cs

## Параметры тестирования

- **Инструмент:** SBER (Сбербанк)
- **Период данных:** 01.01.2024 - 10.10.2025
- **Объем торговли:** 1 контракт
- **SMA1:** 15 периодов
- **SMA2:** 91 период
- **Тип анализа:** Один полный проход по историческим данным
- **Время выполнения:** 4.26 сек

## Проблемы при тестировании

1. **Проблема с запуском на чистой Windows10:**
   - При попытке запустить OsEngine.exe со скачанного репозитория на чистой установке Windows10 произошла ошибка при инициализации (см. Capture.PNG)

2. **Решение:**
   - Найдена машина с предварительно установленной VS2022
   - На этой машине OsEngine.exe успешно запустилась
   - Все последующие тесты проведены на этой конфигурации

## Скриншоты ошибок

- Capture.PNG - Ошибка при запуске на чистой Windows10 (c установленной .NET 9.0 )
![Ошибка запуска](https://raw.githubusercontent.com/Alex-Shur/algo_trading_csharp_ws_Python/refs/heads/main/OsEngine_cs/Capture.PNG)

- Результаты тестирования
![1](https://raw.githubusercontent.com/Alex-Shur/algo_trading_csharp_ws_Python/refs/heads/main/OsEngine_cs/Capture1.PNG)

![2](https://raw.githubusercontent.com/Alex-Shur/algo_trading_csharp_ws_Python/refs/heads/main/OsEngine_cs/Capture2.PNG)

![3](https://raw.githubusercontent.com/Alex-Shur/algo_trading_csharp_ws_Python/refs/heads/main/OsEngine_cs/Capture3.PNG)

![4](https://raw.githubusercontent.com/Alex-Shur/algo_trading_csharp_ws_Python/refs/heads/main/OsEngine_cs/Capture4.PNG)
