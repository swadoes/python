import os
os.system("cls")

my_text = 'ываабв лповап абвцукв алоабвабв ываываыв'
my_text = filter(lambda x: 'абв' not in x, my_text.split())
new_text = " ".join(my_text)
print(new_text)