def calculate_average(numbers):
    """
    Calculate the average of integers in an array.
    
    Args:
        numbers: A list of integers
        
    Returns:
        float: The average of the numbers, or 0 if the list is empty
    """
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)
