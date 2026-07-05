FROM alpine:latest
RUN apk add --no-cache ffmpeg nginx
RUN mkdir -p /var/www/html /run/nginx
RUN echo 'events {} http { include mime.types; server { listen 80; location / { root /var/www/html; add_header Access-Control-Allow-Origin *; } } }' > /etc/nginx/nginx.conf
RUN echo -e '#!/bin/sh\nnginx\nffmpeg -re -i "$STREAM_URL" -c:v copy -c:a copy -f hls -hls_time 4 -hls_list_size 5 -hls_flags delete_segments /var/www/html/stream.m3u8' > /start.sh
RUN chmod +x /start.sh
EXPOSE 80
CMD ["/start.sh"]
