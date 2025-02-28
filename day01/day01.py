'''
System Procedure:
1. Read the file data
2. Parse the file's data into two lists. 
3. Sort the two lists.
4. Compare the difference between each complimentary item in the lists.
5. Find the sum of the differences.
6. Print the difference to the screen.
'''

'''
READ FILE
Reads a .txt file to return two lists
Input:      'filename' - the name of the file to be read.
Output:     'data' - a list of numeric strings.
'''
def read_file(file_name):
    # Try to read the file
    try:
        with open(file_name, 'r') as file:
            # Get each line from the file.
            lines = file.readlines()
            data = []

            # Remove \n from the list
            for line in lines:
                data.append(line.replace('\n', ''))
            print(data)
            return data
    except:
        print(f"File '{file_name}' could not be read.")
        return []


'''
PARSE DATA
Takes a list of strings and splits the items into two lists.
Input:      'data' - a list of numeric strings
Output:     'lists' - a list containing the two lists.
'''
def parse_data(data):
    lists = [[],[]]
    for line in data:
        numbers = line.split()
        lists[0].append(int(numbers[0]))
        lists[1].append(int(numbers[1]))
    return lists

'''
GET SIMILARITY SCORE
(added in Part 2)
Takes two lists and counts how often each number in the first list appears in
the second list. Similarity score is the sum of the products of each value and
the number of times it appears in the second list (for example, if the number
3 appeared 4 times in the list, similarity would increase by 12 (3 * 4).) 
Input:      'list1' - The first list to be compared
            'list2' - The second list to be compared
OUTPUT:     'sum_similarity' - The total of the products of the number and 
                        their occurances.
'''
def get_similarity_score(list1, list2):
    # If both lists are empty, there's noting to sum.
    if (len(list1) == len(list2) == 0):
        return 0
    sum_similarity = 0
    value_catalogue = {}

    # Get all the values in the first list
    for i in range(len(list1)):

        # Add new values in the first list to the catalogue.
        if (value_catalogue.get(int(list1[i])) == None):
            value_catalogue[int(list1[i])] = 0

    # Find overlaps in the second list.
    for i in range(len(list2)):
        if int(list2[i]) in value_catalogue:
            value_catalogue.update({int(list2[i]): value_catalogue[int(list2[i])] + 1})
    
    for i in range(len(list1)):
        sum_similarity += (int(list1[i]) * value_catalogue[int(list1[i])])

    return sum_similarity


'''
GET TOTAL DIFFERENCE
Takes two lists and returns the sum difference of each item in the lists.
Input:      'list1' - The first list to be compared
            'list2' - The second list to be compared
Output:     'difference' - The total difference between the two lists.
'''
def get_total_difference(list1, list2):
    # If both lists are empty, return no difference.
    if (len(list1) == len(list2) == 0):
        return 0
    sum_difference = 0

    # Continue for as long as the longest list is.
    length = (len(list1) if len(list1) > len(list2) else len(list2))
    for i in range(length):

        # If a list ran out, count it as 0
        val1 = (list1[i] if list1[i] else 0)
        val2 = (list2[i] if list2[i] else 0)

        # Get the difference
        difference = abs(val1 - val2)
        sum_difference += difference
    return sum_difference

def main():
    # Read the file data
    file_name = input("Enter the file's name: ")
    raw_data = read_file(file_name)

    # Parse the file data
    data = parse_data(raw_data)
    list1 = data[0]
    list2 = data[1]

    # Sort the data
    list1.sort()
    list2.sort()

    # Get similarity rating
    similarity = get_similarity_score(list1, list2)
    print(f"Similarity Score: {similarity}.")

    # Compare the lists and find the sum of the differences
    difference = get_total_difference(list1, list2)

    # Print to the screen
    print(f"The difference is: {difference}.")

if __name__ == "__main__":
    main()