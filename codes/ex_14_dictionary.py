Country = {
    "China":"Beijing",
    "Russia":"Moscow",
    "UK":"Unknow"
}

print("Capital of Russia is",Country["Russia"])

Country["Cuba"] = "Havana"
country = "Cuba"
print("Capital of",country,"is",Country[country])

country = "UK"
print("Capital of",country,"is",Country[country])

Country[country] = "London"
print("Capital of",country,"is",Country[country])
