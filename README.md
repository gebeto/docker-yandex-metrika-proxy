# docker-yandex-metrika-proxy
Docker container with Yandex.Metrika nginx proxy for Ukraine, etc.


## Usage example
This command run proxy and generate `tag.js` file with metrika `http://localhost` url
```sh
 $ docker run \
 	-p 80:9999 \
 	-e "PROXY_URL=http://localhost" \
 	-v -it gebeto/yandex-metrika-proxy
```