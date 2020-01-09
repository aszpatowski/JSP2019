import xml.etree.ElementTree as ET

Name = []
Converter = []
Code = []
Course = []
mytree = ET.parse('a004z200108.xml')
myroot = mytree.getroot()
for x in myroot:
    if x.tag =='pozycja':
        Name.append(x[0].text)
        Converter.append(x[1].text)
        Code.append(x[2].text)
        Course.append(x[3].text)


print(Name)
print(Converter)
print(Code)
print(Course)