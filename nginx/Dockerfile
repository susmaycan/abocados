FROM nginx:1.19.0-alpine

EXPOSE 80

RUN rm -rf /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d
