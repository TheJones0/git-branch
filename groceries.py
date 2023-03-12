my_dict = {"warzywniak" : ["pomidor", "ogórek", "ziemniaki"],
          "piekarnia" : ["bułki", "chleb", "pączek"]}
new_dict = {k.capitalize() : [s.capitalize() for s in v] for k, v in my_dict.items()}
total = 0
for k, v in new_dict.items():
    print(f"ide do {k}, kupuje nastepujace rzeczy {', '.join(v)}")
    total += len(v)
print(f"w sumie kupiłem {total} rzeczy")
print("koniec zadania")
print("Jednak nie koniec, bo zapomniałem o pozdrowieniach :D")