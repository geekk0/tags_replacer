import csv
import codecs

f = open('default_hashtag.txt', 'r', encoding='utf8')
default_template = f.read()
f.close()

new_page = ''

with open('codes.csv', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        new_block = default_template

        tag_description = row[0]
        tag_name = row[1]
        image_path = row[2]

        new_block = new_block.replace('element_name', tag_name).replace('element_description', tag_description).replace('element_qr_path', image_path)

        new_page += '\n'+new_block

f = open('Простыня.txt', 'w', encoding='utf8')
f.write(new_page)
f.close()





