a={'may':30,'nov':8,'des':1,'jan':14}
print("Dictionary",a)
print("ascending order using keys:",sorted(a.keys()))
print("ascending order of values:",sorted(a.values()))
print("descending order of keys:",sorted(a.keys(),reverse=True))
print("descending order of values:",sorted(a.values(),reverse=True))
print("ascending order of items:",sorted(a.items()))
print("descending order of items:",sorted(a.items(),reverse=True))