# Приложение для общения с GigaChat посредством использования GigaChat API

## Зависимости:
- python 3.8+
- python venv 
- pip

## Развертывание приложения (в *nix системах)
После загрузки репозитория, необходимо создать виртуальное окружение python в корневой папке проекта, активировать его и установить зависимости:
```
python -m venv venv
source venv/bin/activate
pip install -r requierements.txt
deactivate
```
Также необходимо скопировать конфигурационный файл и ввести свои данные:
```
cp default.config.yaml config.yaml
nano config.yaml
```

## Запуск приложения
Для запуска приложения необходимо активировать виртуальное окружения и запустить исполняемый файл:
```
source venv/bin/activate
python main.py
```

## Структура проекта:
- main.py - основной исполняемый файл
- README.md - инструкция по установке и запуску
- default.config.yaml - конфигурационный файл
- requierements.txt - файл, содержащий зависимости python
- .gitignore - файл с указанием файлов, которые не следует загружать в git