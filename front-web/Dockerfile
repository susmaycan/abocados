# syntax = docker/dockerfile:1

FROM node:21-slim as base

WORKDIR /app

# Build
FROM base as build

COPY --link package*.json ./
RUN npm ci

# Run
FROM base

COPY --from=build /app/node_modules /app/node_modules

CMD [ "npm", "run", "dev" ]

EXPOSE 3000
