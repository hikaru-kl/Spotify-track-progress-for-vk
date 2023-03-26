# Spotify-track-streamer-for-vk
Небольшой скрипт для изменения статуса VK при прослушивании музыки на Spotify.

____
## Запуск
1. Необходимо полчить свой access_token VK, для этого нужно перейти на [vkhost.github.io](https://vkhost.github.io/) выбрать вкладку `Настройки` --> В настройках выбрать тип - `Пользователь`, права - `статус`.
2. Необходимо получить OAuth token Spotify, для этого нужно перейти на [developer.spotify.com](https://developer.spotify.com/console/get-users-currently-playing-track/), нажать на `GET TOKEN` и выбрать `user-read-currently-playing`.
3. Нужно создать 2 txt файла в директории со скриптом:
- spotify_token.txt
- vk_token.txt

И поместить в соответствующие файлы токены от VK и Spotify
____

По хорошему скрипт на долгое время не запускать или же выставить большие тайминги на time.sleep т. к. спустя некоторое время vk выкидывает капчу, из-за чего работа скрипта приостанавливается.
