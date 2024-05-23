import heapq

def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів у мінімальну купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Виймаємо два найменші елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість з'єднання цих двох кабелів
        cost = first + second
        
        # Додаємо цю вартість до загальної вартості
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальна вартість з'єднання кабелів:", min_cost_to_connect_cables(cables))
