import heapq

def distribute_items(data):
    total_items = data[0]["total"]
    bins = data[0]["bins"]
    
    # Extract bin information into a list of tuples: (distance, space_left, bin_name)
    bin_info = []
    for bin_dict in bins:
        bin_name = list(bin_dict.keys())[0]
        space_left = bin_dict[bin_name]["space-left"]
        distance = int(bin_name.split("-")[1])  # Extract the SK number
        bin_info.append((distance, space_left, bin_name))
    
    # Sort bins by distance (ascending) and space_left (descending)
    bin_info.sort(key=lambda x: (x[0], -x[1]))
    
    # Use a max-heap to prioritize bins with the most space_left at the same distance
    distribution = {}
    remaining_items = total_items
    total_distance = 0
    
    for distance, space_left, bin_name in bin_info:
        if remaining_items <= 0:
            break
        
        # Assign as many items as possible to this bin
        items_to_assign = min(remaining_items, space_left)
        distribution[bin_name] = items_to_assign
        remaining_items -= items_to_assign
        total_distance += distance
    
    return distribution, total_distance

# Example dataset
data = [
    {
        "total": 14,
        "bins": [
            {"SK-1": {"capacity": 23, "space-left": 4}},
            {"SK-2": {"capacity": 30, "space-left": 4}},
            {"SK-3": {"capacity": 20, "space-left": 8}},
            {"SK-4": {"capacity": 23, "space-left": 4}},
            {"SK-5": {"capacity": 30, "space-left": 14}},
            {"SK-7": {"capacity": 20, "space-left": 16}}
        ]
    }
]

# Get the distribution
result, total_distance = distribute_items(data)
print("Distribution:", result)
print("Total Distance:", total_distance)