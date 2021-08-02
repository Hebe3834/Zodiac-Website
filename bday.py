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
html = fill_tag(template, 'title', 'Enter Your Birthday')
html = fill_tag(html, 'h1', 'What is your birthday?')
html = fill_tag(html, 'body', '''<br><br>
<p>
<form action="''' + choice) 
html = fill_tag(html, 'body', '''_result.py" method="GET" style="color:white">
Month:
     <select name="month">
	<option value="1">January</option>
	<option value="2">February</option>
        <option value="3">March</option>
        <option value="4">April</option>
        <option value="5">May</option>
        <option value="6">June</option>
        <option value="7">July</option>
        <option value="8">August</option>
        <option value="9">September</option>
        <option value="10">October</option>
        <option value="11">November</option>
        <option value="12">December</option>
     </select>
<br><br>Day: 
 <input type=text name='day'>
<br><br>Year:
 <input type=text name='year'>
<br><br>
<input type="checkbox" name="consent" value=True>
<label for="consent">Use my result for data purposes</label>
<br><br>
 <input type="submit">
</form>
<br><br><br>
</p>
<p style="color:azure">
(Please enter a valid birthday and a year from 1900 to 2020)
</p>''')

print(html)
