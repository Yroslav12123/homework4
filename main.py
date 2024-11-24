import poems
import sign

fullname = 'Ярослав Волков'

name3 = sign.OWNER.format(avtor='Ярослав')

print(name3)

wishes = ('З цього курсу я хочу вивчити python basics\nтакож це мені потрібно для моєї майбутньої роботи')
print(wishes)

random = "**************************************************************************"
print(random)

poem1 = poems.SHEVCHENKO_POEM.format('SHEVCHENKO_POEM1')

print(poem1)
print(random)

poem2 = poems.SHEVCHENKO_POEM2.format('SHEVCHENKO_POEM2')

print(poem2)
print(random)
