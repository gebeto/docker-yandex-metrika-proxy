FROM gebeto/nginx-python

MAINTAINER <slavik.nychkalo@gmail.com>

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./scripts /www/scripts
# COPY ./tag.py /www/tag.py

WORKDIR /www/static

RUN mkdir -p /www
RUN mkdir -p /www/scripts
RUN mkdir -p /www/static
# RUN python tag.py github.com
# RUN rm tag.py _tag.js


EXPOSE 9999

# ENTRYPOINT ["nginx", "-g", "daemon off;"]

ENTRYPOINT ["/www/scripts/start.sh"]

