# Порівняння ефективності алгоритмів сортування: Merge Sort, Insertion Sort та Timsort

## Опис завдання

Метою дослідження було порівняння трьох алгоритмів сортування — Merge Sort, Insertion Sort та Timsort. Тестував на різних наборах даних:
1. **Повністю несортовані дані**
2. **Напівсортовані дані** (половина відсортована, половина — випадкові елементи)
3. **Майже відсортовані дані** (деякі елементи знаходяться не на своїх місцях)

Для аналізу були використані масиви розміром 10, 100 і 1000 елементів.

## Результати

### Розмір масиву: 10
| Тип даних           | Merge Sort (с) | Insertion Sort (с) | Timsort (с)  |
|---------------------|----------------|--------------------|--------------|
| Несортовані         | 0.000012       | 0.000004           | 0.000002     |
| Напівсортовані      | 0.000013       | 0.000004           | 0.000002     |
| Майже відсортовані  | 0.000011       | 0.000003           | 0.000002     |

### Розмір масиву: 100
| Тип даних           | Merge Sort (с) | Insertion Sort (с) | Timsort (с)  |
|---------------------|----------------|--------------------|--------------|
| Несортовані         | 0.000140       | 0.000174           | 0.000007     |
| Напівсортовані      | 0.000132       | 0.000143           | 0.000006     |
| Майже відсортовані  | 0.000133       | 0.000047           | 0.000006     |

### Розмір масиву: 1000
| Тип даних           | Merge Sort (с) | Insertion Sort (с) | Timsort (с)  |
|---------------------|----------------|--------------------|--------------|
| Несортовані         | 0.001650       | 0.018960           | 0.000079     |
| Напівсортовані      | 0.001549       | 0.015291           | 0.000046     |
| Майже відсортовані  | 0.001552       | 0.004284           | 0.000043     |

## Висновки

1. **Timsort** — найшвидший алгоритм сортування у всіх випадках. Навіть на великих наборах даних розміром 1000 елементів, Timsort значно перевершує інші алгоритми.

2. **Insertion Sort** показує задовільні результати на малих масивах, але швидко стає неефективним для великих даних. Алгоритм має квадратичну складність \(O(n^2)\), що особливо помітно при роботі з великими масивами. 

3. **Merge Sort** стабільний на всіх наборах даних. Показує стабільні результати незалежно від типу даних, що відповідає його складності \(O(n \log n)\). Хоча він повільніший за Timsort на малих і середніх наборах даних, він все одно є надійним алгоритмом для роботи з великими масивами.

### Рекомендації

На основі цих результатів можна зробити висновок, що використовувати вбудовані алгоритми сортування Python (Timsort) — це хороша практика, оскільки цей алгоритм демонструє високу ефективність на всіх типах даних і є універсальним рішенням для реальних застосувань. У більшості випадків немає необхідності перевинаходити велосипед та імплементувати власні алгоритми сортування, адже Timsort забезпечує як швидкість, так і стабільність.