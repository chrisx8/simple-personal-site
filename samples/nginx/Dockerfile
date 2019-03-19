FROM nginx:alpine

RUN rm -rf /etc/nginx/conf.d && \ 
	rm -rf /usr/share/nginx

COPY conf.d /etc/nginx/conf.d

EXPOSE 80 443
