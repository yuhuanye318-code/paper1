temperature = {"name1":37.5,
               "name2":37.6,
               "name3":37.7,
               "name4":39,}
print(temperature)

for temperature_id,temperature_number in temperature.items():
    if temperature_number >= 38:
        print(temperature_id)
        print("以上这些人发烧了")