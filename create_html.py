import os

if not os.path.exists('documents/html'):
    os.makedirs('documents/html')

path = 'documents'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.md' in file:
            files.append(os.path.join(r, file))

for f in files:
    sep1 = '.'
    c = f.split(sep1, 1)[0]
    print('path', c)
    sep2 = '/'
    d = c.split(sep2, 1)[1]
    print('output', d)
    os.system(f'pandoc --pdf-engine=wkhtmltopdf {c}.md -o documents/html/{d}.html')
    




