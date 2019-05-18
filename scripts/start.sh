#! /bin/sh

python /www/scripts/tag.py $PROXY_URL


exec nginx -g "daemon off;"