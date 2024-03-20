# AFO

### Начало работы

Сборка контейнера ``` docker-compose up ```

Основной URL: ``` 127.0.0.1:5000 ```

Докер настроен на путь ``` 0.0.0.0 ```, что значит поиск всех доступных адрессов 
в случае не работы основного URL посмотрите доступные пути в консоли(после запуска докера)

### Конечные точки
- ``` /auth/registration ``` - регестрация пользователя (принимает email, login, password)
- ``` /auth/login ``` - получение jwt-токена (принимает email, password)
- ``` /new ``` - добавление нового реквезита (принимает bank, bik, rs, ks) [требует jwt]
- ``` /get ``` - получение списка всех реквезитов текущего пользователя (ничего не принимает) [требует jwt]
- ``` /edit ``` - изменение реквезитов (принимает id, и 4 необезательных аргумента bank, bik, rs, ks) [требует jwt]
- ``` /remove ``` - удаление реквезита (принимает id) [требует jwt]
- ``` /activity ``` - выбор активного реквезита (принимает id) [требует jwt]

[требует jwt] - требует заголовка ``` Autorization: bearer <jwt> ```, значение которого можно получить по ``` /auth/login ```
Все конечные точки требующие jwt позволяют работать только с реквезитами того пользовотеля кому пренадлежит jwt

### Глобальные переменые для доступа к БД
- HOST - ``` localhost ```
- PORT - ``` 5432 ```
- PASSWORD - ``` postgres ```
- USER - ``` postgres ```
- NAME - ``` afo ```

URL для поключения к бд - ``` postgresql://postgres:postgres@localhost:5432/afo ```

URL для подключения к бд через Dbeaver - ``` jdbc:postgresql://postgres:postgres@localhost:5432/afo ```
