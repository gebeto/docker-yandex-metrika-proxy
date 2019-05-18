import os
import sys

# print os.environ

script_path = os.path.realpath(__file__)
dir_path, script = os.path.split(script_path)

args = sys.argv
if len(args) == 2:
	DOMAIN = args[1]
else:
	DOMAIN = "http://DOMAIN.COM"

print("Generating tag.js for domain: %s" % DOMAIN)

tag_template = open(os.path.join(dir_path, "_tag.js")).read()


# tag = tag.replace("mc.yandex.ru", "192.168.8.111:9999")
# tag = tag.replace("mc.yandex", "google")

is_https = True if len(DOMAIN.split("https://")) == 2 else False

# 
# Replace with your server IP or Domain
# 
tag_template = tag_template.replace("mc.yandex.ru", DOMAIN)
if not is_https:
	tag_template = tag_template.replace('"https://"', '"http://"')
	tag_template = tag_template.replace('"https:"', '"http:"')
	tag_template = tag_template.replace('"https"', '"http"')
	tag_template = tag_template.replace('https', 'http')


open("tag.js", "w").write(tag_template)