favorite_language = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}
for key,value in favorite_language.items():
	print("key:"+key)
	print("value:"+value)

for key in favorite_language.keys():
	print("key:"+key)
	print("value:"+favorite_language[key])

for value in favorite_language.values():
	print("value:"+value)

for key in sorted(favorite_language.keys()):
	print("key:"+key)
	print("value:"+value)

for value in set(favorite_language.values()):
	print("value:"+value)
	