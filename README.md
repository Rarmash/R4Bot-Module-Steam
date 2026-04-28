# R4Bot-Module-Steam

Внешний Steam-модуль для [R4Bot](https://github.com/Rarmash/R4Bot).

## Что делает
- добавляет `/steam price`
- добавляет `/steam profile`
- добавляет `/steam connect`
- привязывает Steam-профиль к Discord-учётной записи
- показывает цену игр и данные Steam-профиля
- если установлен модуль `profile`, добавляет в него поле Steam-профиля
- поддерживает vanity username и fallback через Steam Community
- использует runtime services из `bot.r4_services`

## Интеграции
- модуль может зарегистрировать profile-provider для `/profile`
- если `profile` не установлен, это не считается ошибкой и Steam-модуль продолжает работать сам по себе

## Секреты
API-ключ Steam хранится в:

```json
{
  "api_key": "YOUR_STEAM_WEB_API_KEY"
}
```

Файл должен лежать в:

```txt
config/secrets/steam.json
```

## Требования
- R4Bot `>= 2.0`
- runtime context с `bot.r4_services`
- сервисы `config`, `firebase`, `secrets`
- установленные пакеты `requests`

## Структура
- `module.json` — метаданные модуля
- `cog.py` — команды Steam и основное поведение модуля
- `service.py` — регистрация Steam-поля для модуля профиля
- `steam.secrets.example.json` — пример файла секретов
- `requirements.txt` — зависимости для IDE и локальной проверки

## Установка в R4Bot
```powershell
python manage_modules.py install github:Rarmash/R4Bot-Module-Steam@master --enable
```

## Разработка
Для нормальной подсветки импортов в IDE и локальной проверки модуля рекомендуется установить зависимости:

```powershell
python -m pip install -r requirements.txt
```
