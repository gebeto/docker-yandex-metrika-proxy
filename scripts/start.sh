#! /bin/sh

python /www/scripts/tag.py $PROXY_URL


nginx -g "daemon off;"