# Restaurant Order System

Приложение для управления заказами в ресторане. Позволяет пользователям добавлять товары в корзину, выбирать стол и оформлять заказы.

Администраторы могут управлять заказами: удалять их, сохранять и изменять статусы. Также администратор может просматривать заказы, созданные пользователями, искать заказы по статусу и ID стола, а также изменять статус заказа напрямую на сайте.

Дополнительные возможности:

Процесс верификации пользователя по email — для каждого пользователя доступен только один email.
Фильтрация списка заказов по статусу.



🚀 Установка


git clone https://github.com/TOFU-tj/django-restaurant-project.git



активация виртуального окружения 
python3 -m venv .venv


1. macOS
source .venv/activate/bin

2. Windows
.venv\Scripts\activate

3. cd restaurant 


pip install -r requirements.txt

requerment.txt
pip install django
pip install Pillow


Добавление базы данных
На macOS может возникнуть ошибка env: python\r: No such file or directory

если она возникла используете эту строку 

sed -i '' -e 's/\r$//' manage.py

потом можете уже добавляйте БД

./manage.py loaddata main/fixtures/category.json   
./manage.py loaddata main/fixtures/goods.json                        
./manage.py loaddata main/fixtures/tables.json  


Создание суперпользователя !!! 

./manage.py createsuperuser

cd restaurant 


👤 Автор: [TOFU-tj](https://github.com/TOFU-tj))
