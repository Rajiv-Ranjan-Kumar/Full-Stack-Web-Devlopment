"""
Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
"""
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
for e in sample_dict:
    if sample_dict[e] == min(sample_dict.values()):
        print(e)
