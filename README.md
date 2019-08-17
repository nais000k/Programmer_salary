# Developers salaries
Проект предназначен для получения наглядной информации о зарплатах разработчиков наиболее популярных языков программирования.

### Как использовать
Для работы скрипта необходим установленный интерпретатор Python3. Затем загрузите зависимости с помощью "pip" (либо "pip3", в случае конфликтов с Python2):  

    pip install -r requirements.txt

Проект основан на использовании:  

1) [HeadHunter API](https://api.hh.ru/)  
2) [Superjob API](https://api.superjob.ru/)  

Также проект разделен на 2 соответствующих скрипта:  

1) `head_hunter.py` - предоставляет статистику зарплат разработчиков топовых языков программирования из HeadHunter API. 

2) `superjob.py` - предоставляет статистику зарплат разработчиков топовых языков программирования из SuperJob API.  Скрипт использует параметр окружения SUPERJOB_TOKEN. Храните эти чувствительные данные в файле `.env`. Получить токен можно зарегистрировавшись на [SuperJob](https://api.superjob.ru/register).

### Пример использования

    python head_hunter.py

Результат:

    +HeadHunter Moscow--------------+---------------------+------------------+
    | Язык       | Вакансий найдено | Вакансий обработано | Средняя зарплата |
    +------------+------------------+---------------------+------------------+
    | Javascript | 2599             | 1019                | 130726           |
    | Java       | 1836             | 495                 | 163279           |
    | Python     | 1451             | 532                 | 142411           |
    | Ruby       | 210              | 84                  | 152880           |
    | PHP        | 1154             | 628                 | 117289           |
    | C++        | 1016             | 319                 | 149045           |
    | C#         | 1107             | 340                 | 146035           |
    | C          | 1915             | 1986                | 85402            |
    | Go         | 408              | 167                 | 136170           |
    | Scala      | 203              | 41                  | 186792           |
    +------------+------------------+---------------------+------------------+

Или:

    python superjob.py

Результат:

    +SuperJob Moscow----------------+---------------------+------------------+
    | Язык       | Вакансий найдено | Вакансий обработано | Средняя зарплата |
    +------------+------------------+---------------------+------------------+
    | Javascript | 34               | 12                  | 99600            |
    | Java       | 11               | 7                   | 143857           |
    | Python     | 15               | 7                   | 87028            |
    | Ruby       | 0                | 0                   | 0                |
    | PHP        | 30               | 12                  | 101266           |
    | C++        | 11               | 7                   | 107714           |
    | C#         | 14               | 10                  | 120400           |
    | C          | 7                | 3                   | 125333           |
    | Go         | 0                | 0                   | 0                |
    | Scala      | 0                | 0                   | 0                |
    +------------+------------------+---------------------+------------------+
    
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org)
