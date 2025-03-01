# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

- Скачайте код
- Установите зависимости для работы с проектом

```bash
pip install -r requirements.txt
```

## Запуск

- Запустите сайт используя файл с продукцией по умолчанию `table_sample.xlsx`

```bash
python main.py
```

- Запустите сайт используя свой файл с продукцией `example.xlsx`

```bash
python main.py -f example.xlsx

```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Настройка

- Сформируйте свой файл с продукцией `example.xlsx`, используя файл по умолчанию `table_sample.xlsx`
- Файл должен иметь расширение `xlsx` или `xls`
- Изображение продукции размещаются в папке `images`
- Пример структуры файла:

| Категория | Название | Сорт | Цена | Картинка | Акция
| --------- | -------- | ---- | ---- | -------- | -----
| Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение
| Напитки | Коньяк классический |  | 350 | konyak_klassicheskyi.png |
| Белые вина | Ркацители | Ркацители | 499 | rkaciteli.png |
| Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png |
| Красные вина | Хванчкара | Александраули | 550 | hvanchkara.png |
| Белые вина | Кокур | Кокур | 450 | kokur.png |
| Красные вина | Киндзмараули | Саперави | 550 | kindzmarauli.png |
| Напитки | Чача |  | 299 | chacha.png | Выгодное предложение
| Напитки | Коньяк кизиловый |  | 350 | konyak_kizilovyi.png |

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
