# Курси, які хочу пройти

Збираємо все сюди. План складемо, коли список буде повний.

## Python (база)

| # | Курс | Посилання | Обсяг | Про що |
|---|---|---|---|---|
| 1 | «Поколение Python»: курс для начинающих | https://stepik.org/course/58852 | 500+ задач з автоперевіркою | Змінні, умови, цикли, рядки, списки: база алгоритмів |
| 2 | «Поколение Python»: курс для продвинутых | https://stepik.org/course/68343 | 700+ задач | Вкладені списки й матриці, кортежі, множини, словники, функції, модулі (random, string, decimal), робота з файлами |

Обидва курси безкоштовні (Stepik), мова: російська. Проходимо по черзі: спочатку для начинающих, потім для продвинутых.

## Git та GitHub

| # | Курс | Посилання | Про що |
|---|---|---|---|
| 1 | 10 Days of Git and GitHub (Asabeneh) | https://github.com/asabeneh/10-days-of-git-and-github | Безкоштовний покроковий репозиторій: від основ терміналу до гілок, пушу, пул-реквестів, forking, .gitignore |

Версія для читання прямо в браузері (без GitHub): https://asabeneh.github.io/10-days-of-git-and-github/

Той самий автор веде серію «30 Days Of ...» (JavaScript, Python, React) — поки не додаю окремо, бо Python уже покривають курси вище, але можна повернутись пізніше.

## AI / ML (з відео @magerdev1)

| # | Курс | Посилання | Обсяг | Про що |
|---|---|---|---|---|
| 1 | AI For Beginners (Microsoft) | https://github.com/microsoft/AI-For-Beginners | 12 тижнів, 24 уроки | Основи AI: нейромережі, Computer Vision (OpenCV, CNN), NLP, PyTorch / TensorFlow |
| 2 | Generative AI for Beginners (Microsoft) | https://github.com/microsoft/generative-ai-for-beginners | 21 урок | Генеративний AI: LLM, промпти, RAG і векторні БД, open-source моделі та Hugging Face, AI-агенти |
| 3 | AI Agents for Beginners (Microsoft) | https://github.com/microsoft/ai-agents-for-beginners | 18 уроків | AI-агенти: патерни Planning, Multi-Agent, Metacognition, агенти в продакшені |

Примітка: усі три курси використовують Python, тому база Python потрібна перед ними.

## Кібербезпека (з відео @magerdev1)

| # | Курс | Посилання | Обсяг | Про що |
|---|---|---|---|---|
| 1 | pwn.college (Arizona State University) | https://pwn.college | Розділи-«доджо», по кожному модулі й задачі | Практична кібербезпека й хакінг прямо в браузері, безкоштовно |

Матеріал треба проходити по порядку:

1. **Getting Started (основи):** Start Here, Linux Luminarium (Linux і термінал), Computing 101, Playing With Programs.
2. **Core Material (пояси, як у бойових мистецтвах):** Intro to Cybersecurity, Program Security, System Security, Software Exploitation.
3. **Community Material (бейджі):** додаткові доджо, наприклад Web Security, Cryptographic Exploitation, x86 Exploitation, CTF-архіви.

Примітка: знадобляться Linux-термінал і Python (для скриптів-експлойтів), а пізніше трохи C та асемблер.

## OSINT (інструменти та ресурси)

Open Source Intelligence — розвідка за відкритими даними. Частина кібербезпеки, входить у стадію recon пентесту. Легальне застосування: пошук своїх слідів в інтернеті, перевірка витоків власних даних, журналістські розслідування, bug bounty recon. Межа: шукати можна тільки свої дані або те, на що є дозвіл — не чужі приватні акаунти без згоди.

| # | Інструмент | Посилання | Що робить |
|---|---|---|---|
| 1 | theHarvester | https://github.com/laramies/theHarvester | Збирає імена, email, IP, субдомени й URL домену з публічних джерел |
| 2 | Maigret | https://github.com/soxoj/maigret | Шукає акаунти людини на багатьох сайтах за нікнеймом (без API-ключів) |
| 3 | DNSDumpster | https://dnsdumpster.com | DNS-розвідка домену: знаходить хости, повʼязані з доменом |
| 4 | EXIFdata | https://www.exifdata.com | Перегляд і редагування EXIF-метаданих фото (геолокація знімку тощо) |
| 5 | Intelligence X | https://intelx.io | Пошук у витоках даних і архівах — передусім щоб перевірити власну експозицію (аналог Have I Been Pwned) |
| 6 | Dorks collections list | https://github.com/cyb-detective/dorks-collections-list | Добірка пошукових дорків для Google, Shodan, Censys, GitHub та інших |
| 7 | OSINT Framework | https://osintframework.com | Інтерактивна карта OSINT-інструментів за категоріями: Username, Email, Domain, Dark Web, Images тощо — зручна відправна точка |
| 8 | Sherlock | https://github.com/sherlock-project/sherlock | Шукає акаунти за нікнеймом у 400+ соцмережах (Python CLI) |

## Роадмапи / маршрути

| # | Ресурс | Посилання | Про що |
|---|---|---|---|
| 1 | roadmap.sh | https://roadmap.sh | Community-роадмапи «що вчити за чим»: ролі (AI Engineer, Frontend, Backend, Cyber Security) і теми, з безкоштовними матеріалами |

Корисні маршрути: [AI Engineer](https://roadmap.sh/ai-engineer), [Inference Engineering](https://roadmap.sh/inference-engineering).

## Цікаві GitHub-проєкти (з відео @github_radar)

Не курси, а готові відкриті інструменти — подивитись, як влаштовані, і за потреби використати.

| # | Проєкт | Посилання | Що робить |
|---|---|---|---|
| 1 | blackbird | https://github.com/p1ngul1n0/blackbird | OSINT: шукає акаунти за нікнеймом на багатьох сайтах (схоже на Sherlock/Maigret) |
| 2 | android-sms-gateway | https://github.com/capcom6/android-sms-gateway | Перетворює Android-телефон на SMS-шлюз з API: надсилання/приймання SMS, вебхуки, шифрування |
| 3 | voicetypr | https://github.com/moinulmoin/voicetypr | Розпізнавання голосу в текст, локально; можна викликати з CLI чи своїх скриптів |
| 4 | openfaas/faas | https://github.com/openfaas/faas | Self-hosted платформа для serverless-функцій і мікросервісів на Kubernetes |
| 5 | websocketd | https://github.com/joewalnes/websocketd | Перетворює будь-яку програму (що читає stdin/пише stdout) на WebSocket-сервер — на будь-якій мові |

## Інші

_(додаватиму сюди)_
