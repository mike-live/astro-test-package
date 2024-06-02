### Astro test package

### Markdown
.md : m = mark, d = down

Rendering of markdown file `Shift-Ctrl-V`

### How to make python packages
https://packaging.python.org/tutorials/packaging-projects/

1. Список всех уставновленных пакетов на вашем компьютере
```cmd
pip list
```

2. Установка нашей библиотеки из папки:
  - Перейти в папку (cd = change directory):
    ```cmd
    cd astro-test-package
    ```
  - Уставновка пакета из текущей папки (-e = editable = редактируемый):
    ```cmd
    pip install -e .
    ```

### Установка git
Скачать git scm for windows.
При установке указать название основной ветки main (должно быть по умолчанию)

### How to use git

1. Создать папку для репозитория
2. Инициализировать репозиторий (это делается только один раз при его создании)
```cmd
git init
```
3. Проверить текущий статус репозитория и ветку
```cmd
git status
```
4. Добавить изменения в репозиторий (в состояние staged)
```cmd
git add <имя файла>
```
5. Сделать commit (закоммитить изменения)
```cmd
git commit -m "Commit message"
```
6. Показать историю коммитов (для текущей ветки)
  ```cmd
  git log
  ```


### How to use github

1. Зарегистрироваться на github.com
2. Настроить двухфакторную аутентификацию
3. Установить ssh-клиент на ваш компьютер
[https://github.com/PowerShell/Win32-OpenSSH/releases](https://github.com/PowerShell/Win32-OpenSSH/releases)
Используйте файл `OpenSSH-Win64-v9.5.0.msi`
4. Создать ssh-ключ для доступа к Github. (Подробная инструкция тут [https://docs.github.com/en/authentication/connecting-to-github-with-ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh))
- Для этого выполнить команду в терминале, в котором доступен ssh-keygen. Например, в VSCode Terminal:
```cmd
ssh-keygen -t ed25519 -C "your_email@example.com"
``` 
- Он предложит указать путь для сохранения вашего ssh-ключа. Если хотите оставить путь по умолчанию, то запомните путь, который он написал и нажмите enter.
```cmd
> Enter file in which to save the key (c:\Users\User\.ssh\id_ALGORITHM)
```
- Затем он предложит ввести passphrase. Это пароль, который защищает ваш ключ локально от прямого копирования. (Не используйте пустые пароли). Парольную фразу он спросит дважды. Если они совпали, то он создаст ключ, иначе запросит ещё раз.
```cmd
> Enter passphrase (empty for no passphrase): [Type a passphrase]
```
5. После создания ключа у вас будет 2 файла: 
- приватный ключ (Например с названием id_ed25519)
- публичный ключ (Например с названием id_ed25519.pub)
6. Публичный ключ необходимо скопировать и разместить на github. 
- Для этого в настройках (Profile->Settings) на github, найдите в панели SSH and GPG keys.
- Нажмите Add SSH key
- Напишите название вашего ключа
- Скопируйте текст файла с публичным ключом (не перепутайте =)) в поле на github
- Сохраните ключ

Отлично, мы настроили SSH ключ. Теперь необходимо его добавить в ssh-agent, чтобы git знал где его искать.

1. Далее необходимо настроить `ssh-agent`
- По идее он должен по умолчанию работать, но если нет, то выполните от имени администратора в powershell:
```powershell
Start-Service ssh-agent
```
2. Добавить ключ в ssh-agent
```cmd
ssh-add <путь к файлу с приватным ключом>
```
Например:
```cmd
ssh-add c:\Users\User\.ssh\id_ed25519
```

#### Настройка пользователя
Теперь конфигурируем настройки пользователя, который будет отправлять изменения на github. (Укажите себя и email как на github)
```cmd
git config --global user.name "Ivanov Ivan"
git config --global user.email "ivanov@example.com"
```

#### Связка локального репозитория и на github
Так как мы уже создали локальный репозиторий, то нужно указать URL, по которому git будет отправлять изменения. Чтобы узнать URL для вашего репозитория нужно на gihub открыть ваш репозиторий, нажать зеленую кнопку Code, выбрать SSH, скопировать URL. 
Затем в терминале VSCode с помощью `cd` перейти в папку с репозиторием и выполнить в ней команду (вместо URL подставить скопированный):
```cmd
git remote add origin <URL>
```

Например, для добавления этого репозитория команда выглядит так:
```cmd
git remote add origin git@github.com:mike-live/astro-test-package.git
```

### Отправляем изменения на github
В папке с репозиторием после того как сделали нужные коммиты и хотите их выгрузить на github, необходимо выполнить команду:
```cmd
git push origin
```

# Как выгрузить package на PyPI
Подробно по ссылке: [https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

PyPI: [https://pypi.org](https://pypi.org)

#### Опечатки, пожелания
Если увидели опечатки или что-то не работает, то вы можете создать Issue к этому репозиторию.