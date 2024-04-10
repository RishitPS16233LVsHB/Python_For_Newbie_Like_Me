stateCapital = {"AndhraPradesh": "Hyderabad", "Bihar": "Patna", "Maharashtra": "Mumbai", "Rajasthan": "Jaipur"}

print(stateCapital.get("Bihar"))  # i. Output: Patna
print(stateCapital.keys())         # ii. Output: dict_keys(['AndhraPradesh', 'Bihar', 'Maharashtra', 'Rajasthan'])
print(stateCapital.values())       # iii. Output: dict_values(['Hyderabad', 'Patna', 'Mumbai', 'Jaipur'])
print(stateCapital.items())        # iv. Output: dict_items([('AndhraPradesh', 'Hyderabad'), ('Bihar', 'Patna'), ('Maharashtra', 'Mumbai'), ('Rajasthan', 'Jaipur')])
print(len(stateCapital))           # v. Output: 4
print("Maharashtra" in stateCapital) # vi. Output: True
print(stateCapital.get("Assam"))   # vii. Output: None
del stateCapital["Rajasthan"]
print(stateCapital)                # viii. Output: {'AndhraPradesh': 'Hyderabad', 'Bihar': 'Patna', 'Maharashtra': 'Mumbai'}
