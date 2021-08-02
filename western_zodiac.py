#!/usr/bin/python
print ("Content-type: text/html\n")

import cgi
data = cgi.FieldStorage()

def fill_tag(html, tag, content):
    index = html.find('</'+tag+'>')
    ans = html[:index] + content + html[index:]
    return ans

template = '''<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="icon" href="icon.jpg">
    <style>
      h1 {
      text-align: center;
      color: azure;
      font-size: 35px
      }
    </style>
  </head>

  <body>
    <a href="home.html" style="float:left; color:powderblue"><< Home</a> <br><br>
    <a href="tests.py?choice=western" style="float:left; color:powderblue">< Tests</a>
  </body>
</html>'''

f = open('zodiacs_info.csv')
info = f.read()
f.close()
info = info.split('\n')[12:]
i = 0
while i<len(info):
    info[i] = info[i].split(',')
    i+=1
sign = data.getvalue('sign')
for line in info:
    if sign==line[0]:
        sign_info = line

html = fill_tag(template, 'title', sign)
html = fill_tag(html, 'style', '''body {
      background-image: url("''' + sign_info[16] + '''");
      font-family: "Lucida Console";
      color: ''' +  sign_info[17] +''';
      background-size: cover;
      background-color: rgba(255,255,255,0.2);
      background-blend-mode: lighten;
      padding: 100px;
      text-align: center;
      }''')
html = fill_tag(html, 'body', '<h1 style="font-size:70px; font-family:Comic Sans MS; color:' + sign_info[11] + '">' + sign + '''</h1>
<p style="font-size:20px;color:azure">''' + sign_info[1] + '</p>' +
'<p style="font-size:30px; background-color:rgba(255,255,255,0.3); padding:20px; border-radius:200px">' +
'Ruling Planet:<br>' + sign_info[12] +
'<br><br>Strengths:<br>' + sign_info[2] + ', ' + sign_info[3] + ', ' + sign_info[4] + ', ' + sign_info[5] + ', ' + sign_info[6] +
'<br><br>Weaknesses:<br>' + sign_info[7] + ', ' + sign_info[8] + ', ' + sign_info[9] + ', ' + sign_info[10] +
'<br><br>Famous people:<br>' + sign_info[14] + ', ' + sign_info[15] +
'<br><br>Color:<br>' + sign_info[11] + 
'<br><br>Chinese equivalant: <a href="chinese_zodiac.py?sign=' + sign_info[13] + '">' + sign_info[13] + '</a>' +
'</p>')

print(html)
