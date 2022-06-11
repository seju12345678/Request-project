import requests
import json
import os
if os.path.isfile("courses.json"):
    with open("courses.json","r") as f:
        a=json.load(f)
else:
    res=requests.get('http://saral.navgurukul.org/api/courses')
    a=res.json()
    b=open("courses.json","w")
    c=json.dump(a,b,indent=4)
i=0
while i<len(a["availableCourses"]):
    print(i+1,":",a["availableCourses"][i]["name"],"ID:",a["availableCourses"][i]["id"])
    i+=1
print("")
course_id=int(input("enter the course no. :"))
print(course_id,":",a["availableCourses"][course_id-1]["name"])
if os.path.isfile("parents.json"):
    with open ("parents.json","r") as ras:
        d=json.load(ras)
else :
    s=a["availableCourses"][course_id-1]["id"]
    l='http://saral.navgurukul.org/api/courses/'+str(s)+'/exercises'
    res1=requests.get(l)
    d=res1.json()
    e=open("parents.json","w")
    f=json.dump(d,e,indent=4)
serial_no=0
for j in d["data"]:
    if j["childExercises"]==[]:
        print(serial_no+1,":",j["name"])
        print("     ",j["slug"])
    else:
        print(serial_no+1,":",j["name"])
        k=0
        while k<len(j["childExercises"]):
            print("     ",k+1,":",j["childExercises"][k]["name"])
            k+=1
    serial_no+=1
print("")
parent_id=int(input("enter the parent no. : "))
print(parent_id,":",d["data"][parent_id-1]["name"])
if d["data"][parent_id-1]["childExercises"]==[]:
    print(d["data"][parent_id-1]["slug"])
    pid=d["data"][parent_id-1]["id"]
    pslug=d["data"][parent_id-1]["slug"]
    if os.path.isfile("slug.json"):
        with open("slug.json","r") as k:
            m=json.load(k)
    else:
        parent_api='http://saral.navgurukul.org/api/courses/'+str(pid)+'/exercise/getBySlug?slug='+pslug
        slug_url=requests.get(parent_api)
        m=slug_url.json()
        with open("slug.json","w") as file3:
            json.dump(m,file3,indent=4)
    print(m["content"])

else:
    k=0
    while k<len(d["data"][parent_id-1]["childExercises"]):
        print("     ",k+1,":",d["data"][parent_id-1]["childExercises"][k]["name"])
        k+=1
    child_id=int(input("enter the child no.: "))
    z=d["data"][parent_id-1]["childExercises"][child_id-1]["slug"]
    r=d["data"][parent_id-1]["childExercises"][child_id-1]["id"]
    if os.path.isfile("child.json"):
        with open("child.json","r") as i:
            g=json.load(i)
    else:
        t='http://saral.navgurukul.org/api/courses/'+str(r)+'/exercise/getBySlug?slug='+z
        res2=requests.get(t)
        g=res2.json()
        h=open("child.json","w")
        i=json.dump(g,h,indent=4)
    print(g["content"])
