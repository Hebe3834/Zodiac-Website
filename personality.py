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
html = fill_tag(template, 'title', "What's your Personality?")
html = fill_tag(html, 'h1', "Check all that apply")

if choice=='chinese':
    traits = ["optimistic","energetic","clever","resourceful","imaginative","hardworking","generous","just","stable","responsible","ambitious","courageous","smart","gentle","patient","elegant","considerate","dedicated","initiative","talented","inspiring","quick-witted","sympathetic","easy-going","calm","determined","endurance","warm-hearted","social","brave","independent","creative","competitive","enthusiastic","innovative","versatile","efficient","confident","loyal","honest","cheerful","trustful","timid","suspicious","short-sighted","not persistent","stubborn","hesitant","struggles to adapt","moody","impulsive","arrogant","aloof","hasty","conservative","peacockish","intolerant","tactless","unrealistic","sly","narrow-minded","jealous","pessimistic","lacks calm","indecisive","vain","emotional","undisciplined","selfish","cunning","critical","impatient","sensitive","reckless","sluggish","naive"]
    form = ''
    for i in traits:
        form += '<input type="checkbox" name="'
        form += i
        form += '"value=True>\n<label for="' + i + '">' + i + "</label>\n<br>"
    html = fill_tag(html, 'body', '''<p style="color:gold; font-size:20px">My strongest qualities and weaknesses are:</p>
    <form action="chinese_result.py" style="color:azure">''' + form + '<input type="submit"><input type="reset"></form>')
else:
    traits = ["adventurous","independent","brave","honest","passionate","stubborn","reckless","aggressive","short-tempered","dependable","hardworking","dedicated","smart","patient","lazy","possessive","uncompromising","adaptable","outgoing","curious","gentle","loves to learn","indecisive","unreliable","nosy","nervous","protective","intuitive","caring","persuasive","sensitive","moody","pessimistic","insecure","generous","confident","cheerful","leader","arrogant","self-centered","kind","creative","shy","worrying","critical","uptight","fair","idealistic","diplomatic","clever","cooperative","self-pitying","non-confrontational","resourceful","jealous","secretive","violent","distrustful","compassionate","impatient","tactless","unrealistic","disciplined","responsible","ambitious","good self-control","condescending","unforgiving","workaholic","visionary","unbiased","aloof","unpredictable","artistic","wise","overly trusting","closed off"]
    form = ''
    for i in traits:
        form += '<input type="checkbox" name="'
        form += i
        form += '"value=True>\n<label for="' + i + '">' + i + "</label>\n<br>"
    html = fill_tag(html, 'body', '''<p style="color:silver; font-size:20px">My strongest qualities and weaknesses are:</p>
    <form action="western_result.py" style="color:white">''' + form + '<input type="submit"><input type="reset"></form>')

print(html)
