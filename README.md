1. Надо уставновить зависимости командой
python -m pip install -r requirements.txt  (или pip install -r requirements.txt)

2. Запускаем сервер командой
python manage.py runserver

3. Заходим н сервер. Видим таблицы c постами и книгами, если не авторизованный пользователь пытается добавить запись, то она будет перехвачена и вместо этого будет добавлена запись 'bird96'(я так назвал канареечные записи у себя) и указана дата добавления, не более 2-ух штук(пердусмотрено ограничение).

4.Вы можете зарегестрироваться и тогда у вас будем возможность добавлять посты и создавать книги. Канареечные записи видеть вы не будете. Их видит только админ. Так же я скрыл их от Django ORM переопределив objects в models.py.

5.Вы можете зайти в качестве админа (логин: 'admin', пароль: 'admin') и у вас будет возможность видеть канареечные записи, все остальные записи и добавлять посты, создавать книги.

6.Все таблицы сделаны с помощью js билиотеки datatables.
