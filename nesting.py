nest={
    "fruits":["apple","banana","kiwi"],
    "laptop":{
        "brand":"dell",
        "ram":4,
        "storageType":"hdd"
    }
}


#accessing through nested list and dictionary

print(nest["fruits"])

# another example

capitals={
    "chhattisgarh":"raipur",
    "madhyaPradesh":"bhopal"
}

#nesting a list in dictionary.
travel_log=[
    {
        "state":"Chhattisgarh",
        "cities_visited":["bilaspur","raipur","korba"],
        "total_Visit":123
    },
    {
        "state":"maharashtra",
        "cities_visited":["mumbai","thane","pune"],
        "total_visit":23
    }
]

print(travel_log[0]["cities_visited"][1])