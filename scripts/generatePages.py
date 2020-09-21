from yattag import Doc
from os import listdir

doc, tag, text, line = Doc().ttl()

with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Coming Soon')
        doc.stag('link', rel = 'stylesheet', href='css/styles.css')
    with tag('body'):
        with tag('h1'):
            text('Coming Soon')
        with tag('table', klass='rwd-table'):
            with tag('tr'):
                line('th', 'Name')
                line('th', 'Emote')
                line('th', 'Link')
            for emote in listdir('../i'):
                with tag('tr'):
                    line('td', emote.split('.')[0], data='Name')
                    with tag('td', data='Emote'):
                        doc.stag('img', src='i/' + emote)
                    line('td', 'Copy', data='Link')

with open('../index.html', 'w') as file:
    file.write(doc.getvalue())