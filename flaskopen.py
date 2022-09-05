import requests

a = requests.get("http://192.168.0.130:8080/jsfs.html")

for i in a:
    print(i)

func = open("image.html","w")
for i in a:
    func.write(str(i))
func.close()