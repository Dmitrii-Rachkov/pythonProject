# Фикстура — это ресурс или объект, который можно рассматривать как набор условий
# или предопределенное состояние, необходимое тесту для правильного выполнения,
# зачастую фикстуры создаются, чтобы генерировать какие-то данные еще до теста и
# возвращать их для использования в тесте или перед тестом: подключение к базе, драйвер, авторизация и т.д.
# Мы можем пометить функцию @pytest.fixture и затем передать эту функцию в качастве аргумента в тест.
# Если вы планируете использовать фикстуру в нескольких тестах, то можно объявить ее в файле conftest.py
# Можно использовать yield которая разделяет что будет сделано до начала теста и после.
#
# @pytest.mark.run(order=5) - позволяет нам определить очередность выполнения тестов
# @pytest.fixture(scope="module") - функция вызывается для тестового модуля
# Возможными значениями параметра scope являются function, class, module, package или session.
#
# Можно параметризировать фикстуры:
# @pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
#
# @pytest.mark.usefixtures("cleandir") - здесь мы указываем какую фикстуру использовать
#
#
