import markovify

# with open("esenin.txt", 'r', encoding='utf-8') as f0, \
# 	open("kish.txt", 'r', encoding='utf-8') as f1, \
# 	open("kino.txt", 'r', encoding='utf-8') as f2, \
# 	open("kukr.txt", 'r', encoding='utf-8') as f3, \
# 	open("dataset.txt", 'a', encoding='utf-8') as f:
#     f.write(f0.read())
#     f.write(f1.read())
#     f.write(f2.read())
#     f.write(f3.read())

with open("dataset.txt", 'r', encoding='utf-8') as f:   
    text = f.read()
text_model = markovify.Text(text)

my_file = open("result.txt", 'a', encoding='utf-8')
for i in range(10):
    my_file.write(text_model.make_short_sentence(280))
my_file.close()