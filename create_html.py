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
    sep = '.'
    c = f.split(sep, 1)[0]
    sep = '/'
    d = c.split(sep, 1)[1]
    os.system(f'pandoc --pdf-engine=wkhtmltopdf {c}.md -o documents/html/{d}.html')
    




