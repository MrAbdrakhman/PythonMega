# Фильтрация с помощью filter(). Необходимо написать функцию, и передать ее filter(),
# чтобы получить список только тех слов из текста text (см. выше “The Zen of Python”), что содержат букву ‘p’.
# Подсказка: необходимо заменить \n на пробел.

# То есть, это нужно проделать еще до фильтрации.
# Функция, которая будет передана в filter() должна возвращать True, если в слове есть буква ‘p’.
text = """The Zen of Python, by Tim PetersBeautiful is better than ugly. Explicit is better than implicit.
Simple is better than complex. Complex is better than complicated. Flat is better than nested.Sparse is better than dense.
Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
text2=list(text.split())
def f1(word_p):
    for i in range(len(word_p)):
        if word_p[i]=='p':
            return True
    return False
out_text=filter(f1,text2)
print(list(out_text))