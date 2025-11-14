# Hitalent-test-task

# Запуск
1. Устанавливаем докер.
2. Клонируем репозиторий на копмьютер.
3. Запускаем проект с помощью команды "docker compose up --build".
4. Переходим по адресу "http://127.0.0.1:8000/docs".

# Работа системы
При запуске скачаются все необходимые зависимости. 
И далее уже можно тестировать работу системы. 

# Questions

- GET/api/v1/questions/ - Получение списка вопросов без ответов.
- POST/api/v1/questions/ - Создание нового вопроса.
- GET/api/v1/questions/{question_id} - Получение вопроса по id со всеми ответами на него.
- DELETE/api/v1/questions/{question_id} - Каскадное удаление вопроса по id.
  
# Answers

- POST/api/v1/answers/question/{question_id} - Создание ответа для вопроса по id вопроса.
- GET/api/v1/answers/{answer_id} - Получение вопроса по id.
- DELETE/api/v1/answers/{answer_id} - Удаление вопроса по id.
