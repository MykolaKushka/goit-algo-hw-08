Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.

Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

Ця задача є класичною задачею Хаффмана, яка може бути розв'язана за допомогою купи (heap). Вона передбачає використання мінімальної купи для мінімізації загальних витрат на з'єднання кабелів.
Пояснення алгоритму:

    Створити мінімальну купу зі всіх довжин кабелів.
    Поки в купі більше одного елемента:
        Вийняти два найменші елементи (кабелі) з купи.
        З'єднати їх, що дає новий кабель із довжиною, яка дорівнює сумі довжин двох з'єднаних кабелів.
        Витрати на це з'єднання додаються до загальних витрат.
        Вставити новий кабель назад у купу.
    Повторювати кроки 2-3 до тих пір, поки в купі не залишиться один елемент.
