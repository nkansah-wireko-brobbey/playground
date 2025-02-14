def distribute_items(data):
    total_items = data[0]["total"]
    bins = data[0]["bins"]
    
    # Define a custom key function for sorting
    def sort_key(bin_info):
        bin_name = list(bin_info.keys())[0]
        sk_number = int(bin_name.split("-")[1])  # Extract the SK number
        space_left = bin_info[bin_name]["space-left"]
        return (sk_number, -space_left)  # Sort by SK number, then by space-left (descending)
    
    # Sort bins using the custom key function
    sorted_bins = sorted(bins, key=sort_key)
    
    distribution = {}
    remaining_items = total_items
    
    # Distribute items into bins
    for bin_info in sorted_bins:
        bin_name = list(bin_info.keys())[0]
        space_left = bin_info[bin_name]["space-left"]
        
        if remaining_items <= 0:
            break
        
        # Assign as many items as possible to this bin
        items_to_assign = min(remaining_items, space_left)
        distribution[bin_name] = items_to_assign
        remaining_items -= items_to_assign
    
    return distribution

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
result = distribute_items(data)
print(result)