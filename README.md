# Учебный проект FastAPI лаготворительного фонда поддержки котиков QRKot.

## В проекте три основные сущности:

- Проекты - У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.


- Пожертвования - Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.


- Пользователи - Целевые проекты создаются администраторами сайта. Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых. Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

## Сам процесc инвестирования выглядит следующим образом:

- Если создан новый проект, а в базе были «свободные» (не распределённые по проектам) суммы пожертвований — они автоматически должны инвестироваться в новый проект, и в ответе API эти суммы должны быть учтены. То же касается и создания пожертвований: если в момент пожертвования есть открытые проекты, эти пожертвования должны автоматически зачислиться на их счета.

## Для запуска проекта:
- клонируйте репозиторий
- установите виртуальное окружение
- установите зависимости из файла requirements.txt
- команда **uvicorn main:app**
