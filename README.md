# Игры для Разума

Добро пожаловать в "Игры для Разума"! Это коллекция небольших игр, разработанных для стимуляции вашего ума. Каждая игра проверяет различные аспекты ваших когнитивных способностей. В коллекцию входят следующие игры:

- **Brain-Even**: Определите, является ли число четным.
[![asciicast](https://asciinema.org/a/sDYZdQKqXPm6pR6jZLBD494Nd.svg)](https://asciinema.org/a/sDYZdQKqXPm6pR6jZLBD494Nd)
- **Brain-Calc**: Выполняйте базовые арифметические вычисления.
[![asciicast](https://asciinema.org/a/sD5erV2XKSQkz0mwtCpVZlHKi.svg)](https://asciinema.org/a/sD5erV2XKSQkz0mwtCpVZlHKi)
- **Brain-GCD**: Найдите наибольший общий делитель двух чисел.
[![asciicast](https://asciinema.org/a/OaeiqwbRxwS7LdFGjkyYvvfyq.svg)](https://asciinema.org/a/OaeiqwbRxwS7LdFGjkyYvvfyq)
- **Brain-Progression**: Определите недостающее число в арифметической прогрессии.
[![asciicast](https://asciinema.org/a/t6E5WIvqbJTTH8nm2ZbbxAkuD.svg)](https://asciinema.org/a/t6E5WIvqbJTTH8nm2ZbbxAkuD)
- **Brain-Prime**: Определите, является ли число простым.
[![asciicast](https://asciinema.org/a/pRONbJyGGYe543ftODQhh1ep6.svg)](https://asciinema.org/a/pRONbJyGGYe543ftODQhh1ep6)

## Установка и использование

Для управления проектом используется Makefile. Ниже представлены основные команды, доступные через `make`.

### Установка зависимостей

Чтобы установить все необходимые зависимости для проекта, выполните:

```sh 
make install 
```


Каждую игру можно запустить с помощью соответствующей команды:

Brain Games:
```sh
make brain-games
```
Brain Even:


```sh
make brain-even
```
Brain Calc:
 https://asciinema.org/connect/8d4fa807-14e3-46c8-97ca-19631eb2b3fb
```sh
make brain-calc
```
Brain GCD:
https://asciinema.org/connect/8d4fa807-14e3-46c8-97ca-19631eb2b3fb
```sh
make brain-gcd
```
Brain Progression:
  https://asciinema.org/connect/8d4fa807-14e3-46c8-97ca-19631eb2b3fb
```sh
make brain-progression
```

Brain Prime:
https://asciinema.org/connect/8d4fa807-14e3-46c8-97ca-19631eb2b3fb
```sh
make brain-prime
```

## Сборка и публикация

Чтобы собрать пакет и подготовить его к публикации, используйте следующие команды:

###  Сборка пакета:

```sh
make build
```

Публикация пакета (с предварительным тестированием):

```sh
make publish
```
Установка и переустановка пакета
Для установки собранного пакета:

```sh
make package-install
```
Для переустановки пакета:

```sh
make package-reinstall
```
Линтинг

Чтобы проверить код на наличие проблем с линтингом, выполните:

```sh
make lint
```


## Запуск игр
После установки пакета вы можете запускать каждую игру напрямую из командной строки:

Brain Games:

```sh
brain-games
```
Brain Even:

```sh
brain-even
```
Brain Calc:

```sh
brain-calc
```
Brain GCD:

```sh
brain-gcd
```
Brain Progression:

```sh
brain-progression
```
Brain Prime:

```sh
brain-prime
```



### Hexlet tests and linter status:
[![Actions Status](https://github.com/Minnebaevilnaz/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Minnebaevilnaz/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e89f68c85cc716f3aa23/maintainability)](https://codeclimate.com/github/Minnebaevilnaz/python-project-49/maintainability)