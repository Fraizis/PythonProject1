def activity_selection(activities):
    # Sort activities by their finish times
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]  # Always select the first activity

    # Iterate through the activities and select the non-overlapping ones
    for i in range(1, len(activities)):
        print(activities[i][0], selected[-1][1])
        if activities[i][0] >= selected[-1][1]:  # Start time >= last finish time
            selected.append(activities[i])

    return selected

# Example usage
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9)]
result = activity_selection(activities)
print("Selected activities:", result)
