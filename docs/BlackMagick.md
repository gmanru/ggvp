### Кoротко о фичах в питоне

## генераторы
вы отлично знаете что такая вот конструкция удобна

```
for k, v in d.items():
    ...
```

этj мо;но занятно применять в генераторах

```
tlst = [for id, name, weight in Town.objects.filter(...).values_list('id', 'name', 'population') ]
```

есть вариант замены OrderedDict если нам нужно немного иначе
```
sort(tlst , key = lmbbda (item): item.weight )
```

## Замыкания
в питоне есть замыкания. но многие не знают, что декоратор уже замыкание.

а ещё функция это же объект... есть простор для фантазии

например можно передать функцию в азмыкании.
тут думаю вопросы будут... все просто. надо обернуть в другой объект с состоянием.
например в функцию!

яркий пример... тут скорее ФП но я хочу зафиксировать переменную
```
def outer(arg, earg):
    title = 'Warrgh!'
    return Inner(arg, title)
```

 а вот замыкание
 
 ```
def outer(arg, earg):
    title = 'Warrgh!'
    return Inner
```
Inner знает title