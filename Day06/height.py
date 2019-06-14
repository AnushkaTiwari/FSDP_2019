# Code Challenge : Rewrite following code using map filter and reduce
"""   people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print (average_height)
    """
    
 people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]     


                      
my_filter_list=filter(lambda x: 'height' in x,people)
print(list(my_filter_list))
    


