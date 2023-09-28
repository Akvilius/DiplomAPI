﻿## Проект включает 2 блока: автоматизацию и запросы к БД
### Автоматизация сценария, который подготовили коллеги-тестировщики:
- Клиент создает заказ.
- Проверяется, что по треку заказа можно получить данные о заказе.

### Особенности запуска тестов
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest -v в командной строке
- При первом запуске __необходимо__ изменить значение переменной __URL_SERVICE__ в файле __configuration.py__ 
на новый адтес тестового стенда

### Работа с базой данных

В файле __НАЗВАНИЕ__ хранятся SQL-запросы для решения следующих задач:
1. Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

2. Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

Технические примечания:

Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.
