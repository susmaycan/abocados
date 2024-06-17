# syntax = docker/dockerfile:1

FROM node:21-slim as base

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

RUN npm run build

CMD [ "npm", "run", "start" ]
