import json

# Read the shortcuts.json file
with open('shortcuts.json', 'r', encoding='utf-8') as file:
    shortcuts = json.load(file)

# Prepare the output structure
quick_actions = {"items": []}

# Process each category and item
for category in shortcuts:
    for item in category["items"]:
        # Only include items that should be shown
        if item.get("show", True):
            name = item["name"]
            species = item.get("species", "")
            genus = item.get("genus", "")
            type = item.get("type", "Tree")
            
            # If genus is empty, take the first word in species
            if not genus and species:
                genus = species.split()[0]
            
            # Construct the name and params
            full_name = f"{name} {species}" if species else name

            key_tag = {
                "poi_type_tag": type,
                "access": "",
                "genus": genus
            }
            if species:
                key_tag["species"] = species
            
            params = {
                "key_tag": json.dumps(key_tag),
                "dialog": "true"
            }
            
            # Add the item to the quick actions list
            quick_actions["items"].append({
                "name": full_name,
                "actionType": "osmpoi.add",
                "params": json.dumps(params)
            })

            print(f"Added {full_name}")
            print(f"  - genus   = {genus}")
            print(f"  - species = {species}")
            print(f"")



# Write the quick_actions_trees.json file
with open('quick_actions_trees.json', 'w', encoding='utf-8') as file:
    json.dump(quick_actions, file, ensure_ascii=False, indent=2)

print("quick_actions_trees.json has been created successfully.")
