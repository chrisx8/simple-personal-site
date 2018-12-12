FROM nginx:alpine

RUN rm -rf /etc/nginx/conf.d && \ 
    rm -rf /usr/share/nginx

COPY conf.d /etc/nginx/conf.d
COPY nginx.conf /etc/nginx/
COPY html /usr/share/nginx

EXPOSE 80 443
