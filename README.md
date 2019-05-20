# docker-yandex-metrika-proxy
Docker container with Yandex.Metrika nginx proxy for Ukraine, etc.

Based on [nginx:alpine](https://hub.docker.com/_/nginx/) with additionally installed python [gebeto/nginx-python](https://cloud.docker.com/repository/docker/gebeto/nginx-python) with `apk add python`


## Usage example
This command run proxy and generate `tag.js` file with metrika `http://localhost` url
```sh
 $ docker run \
 	-p 80:9999 \
 	-e "PROXY_URL=http://localhost" \
 	-v -it gebeto/yandex-metrika-proxy
```

## Purpose
I am from Ukraine and Yandex are blocked in this country. Yandex's solution (Alternative CDN) are not help me to fix my problem, because this solution send metrika data to `mc.yandex.ru` but it is blocked😅. So I create this proxy with `nginx` (`proxy_pass`) to setup it on your host and send all metrika data to it, additionally I create script on `python` that replace `mc.yandex.ru` host to host of your server.

Old metrika logic was:
 > USER -> YANDEX_METRIKA

New is:
 > USER -> YOUR_HOST -> YANDEX_METRIKA
