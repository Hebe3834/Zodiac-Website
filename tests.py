#!/usr/bin/python
print ("Content-type: text/html\n")

import cgi
data = cgi.FieldStorage()

choice = data.getvalue('choice')

def get_template(choice):
    if choice=='chinese':
        f = open('ctemplate.html')
    else:
        f = open('wtemplate.html')
    template = f.read()
    f.close()
    return template

def fill_tag(html, tag, content):
    index = html.find('</'+tag+'>')
    ans = html[:index] + content + html[index:]
    return ans

template = get_template(choice)
html = fill_tag(template, 'title', 'Find your Sign!')
html = fill_tag(html, 'h1', "Let's find out which sign you are")
html = fill_tag(html, 'style', '''p {
background-color:LemonChiffon;
padding:50px;
font-size:30px;
border-radius: 200px;
text-align:center;
width: 30%;
}
p:hover{
box-shadow: 0px 0px 20px 20px gold;
}
''')
html = fill_tag(html, 'body', """ <p style="float:left">
      <a style="color:chocolate;" href="bday.py?choice=""" + str(choice) + '''">From your<br>Birthday</a>
    </p><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <p style="margin:auto">
       <a style="color:chocolate;" href="personality.py?choice=''' + str(choice) + '''">From your<br>Personality</a>
    </p>
    <p style="float:right">
       <a style="color:chocolate;" href="''' + str(choice) + '''_list.html">Never mind, just show me the full list</a>
       </p>''')

print(html)
