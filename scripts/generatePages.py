from yattag import Doc
from os import listdir, walk, path

def get_size(start_path = '../i'):
    total_size = 0
    for dirpath, dirnames, files in walk(start_path):
        for f in files:
            fp = path.join(dirpath, f)
            if not path.islink(fp):
                total_size += path.getsize(fp)
    return total_size

doc, tag, text, line = Doc().ttl()

with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Fast Emote Database')
        doc.stag('link', rel = 'stylesheet', href='css/styles.css')
    with tag('body'):
        with tag('h1'):
            text('Fast Emote Database')
        with tag('p'):
            text(f'{get_size()//1000} KB DB Size')
        doc.stag('input', id='input', type='text')
        with tag('h2'):
            text('Discord')
        with tag('table', klass='rwd-table'):
            with tag('tr'):
                line('th', 'Name')
                line('th', 'Emote')
                line('th', 'Link')
            for emote in listdir('../i'):
                with tag('tr', onclick='copy(\'https://gg.egid.tech/i/' + emote + '\')'):
                    line('td', emote.split('.')[0], data='Name')
                    with tag('td', data='Emote'):
                        doc.stag('img', src='i/' + emote)
                    line('td', 'Copy', data='Link')
        with tag('h2'):
            text('Android')
        with tag('table', klass='rwd-table'):
            with tag('tr'):
                line('th', 'Name')
                line('th', 'Emote')
                line('th', 'Link')
            for emote in listdir('../android'):
                with tag('tr', onclick='copy(\'https://gg.egid.tech/android/' + emote + '\')'):
                    line('td', emote.split('.')[0], data='Name')
                    with tag('td', data='Emote'):
                        doc.stag('img', src='android/' + emote)
                    line('td', 'Copy', data='Link')
        with tag('h2'):
            text('iOS')
        with tag('table', klass='rwd-table'):
            with tag('tr'):
                line('th', 'Name')
                line('th', 'Emote')
                line('th', 'Link')
            for emote in listdir('../ios'):
                with tag('tr', onclick='copy(\'https://gg.egid.tech/ios/' + emote + '\')'):
                    line('td', emote.split('.')[0], data='Name')
                    with tag('td', data='Emote'):
                        doc.stag('img', src='ios/' + emote)
                    line('td', 'Copy', data='Link')
        with tag('script'):
            text(
            '''
            function copy(data) {
                let text = document.querySelector('#input');
                document.getElementById('input').setAttribute('value', data);
                text.select();
                document.execCommand('copy');
            }
            ''')

with open('../index.html', 'w') as file:
    file.write(doc.getvalue())