FROM node:22-alpine AS build-stage

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем переменную для пропуска установки Cypress
ENV CYPRESS_INSTALL_BINARY=0

# Копируем зависимости
COPY package.json package-lock.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код
COPY . .

# Собираем приложение
RUN npm run build

# Stage 2: Production Stage
FROM nginx:alpine AS production-stage

# Копируем собранные файлы в Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Открываем порт 80
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
