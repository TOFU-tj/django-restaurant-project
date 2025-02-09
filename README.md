# Restaurant Order System

Приложение для управления заказами в ресторане. Позволяет пользователям добавлять товары в корзину, выбирать стол и оформлять заказы.

Администраторы могут управлять заказами: удалять их, сохранять и изменять статусы. Также администратор может просматривать заказы, созданные пользователями, искать заказы по статусу и ID стола, а также изменять статус заказа напрямую на сайте.

Дополнительные возможности:

Процесс верификации пользователя по email — для каждого пользователя доступен только один email.
Фильтрация списка заказов по статусу.



🚀 Установка


активация виртуального окружения 
python3 -m venv .venv


1. macOS
source .venv/activate/bin

2. Windows
.venv\Scripts\activate


pip install -r requirements.txt

requerment.txt
pip install django
pip install Pillow


Добавление базы данных

./manage.py loaddata main/fixtures/category.json   
./manage.py loaddata main/fixtures/goods.json                        
./manage.py loaddata main/fixtures/tables.json  


Создание суперпользователя !!! 

./manage.py createsuperuser



git clone https://github.com/твоя-ссылка-на-репо.git
cd restaurant 


👤 Автор: [Твой Никнейм](https://github.com/твой-гит)
