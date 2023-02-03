import json
import re
import add_redirect_entry
from jproperties import Properties

all_redirects = {}
def add_redirect(source, dest):
	newdest =re.sub(r"^(.*)/latest/en/(.*)\.html", r"/en/w/\1/\2", dest)
	newdest =re.sub(r"^(.*)/latest/ja/(.*)\.html", r"/ja/w/\1/\2", newdest)
	all_redirects[source] = newdest

learn_docs_folder = "/home/allenz/liferay/liferay-learn/site/docs"

with open(learn_docs_folder + "/redirects.json", encoding="utf-8") as redirectsfile:
	redirects = json.load(redirectsfile)

for key in redirects:
	add_redirect(key, redirects[key])


keep_redirects = Properties()

with open(learn_docs_folder + "/redirects_keep.properties", "rb") as redirectskeepfile:
	keep_redirects.load(redirectskeepfile, "utf-8")

for redirect in keep_redirects.items():
	add_redirect(redirect[0], redirect[1].data)

new_redirects = Properties()

with open(learn_docs_folder + "/redirects_new.properties", "rb") as redirectsnewfile:
	new_redirects.load(redirectsnewfile)

for redirect in new_redirects.items():
	add_redirect(redirect[0], redirect[1].data)


for key in all_redirects:
	print(key + ": " + all_redirects[key])
	add_redirect_entry.add_redirect(key, all_redirects[key])