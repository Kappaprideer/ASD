# Domino
# Mamy pewien układ klocków domino. Otrzymujmey go w postaci listy par [a,b]. 
# Jeżeli przewrócimy klocek a, to klocek b też się przewróci. Chcemy znaleźć minimalną 
# liczbę klocków , które trzeba przewrócić ręczeni, aby wszystkie domina były przewrócone.
# -----------------------------------------------------------------------------------------
# Rozwiązanie: 
# Graf jest skierowany, reprezentowany listą krawędzi, szukamy wierzchołków z których
# krawędzie tylko wychodzą a żadne nie wchodzą, lub takie które nie mają w ogóle krawędzi. 
# 