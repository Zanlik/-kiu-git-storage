def warn_the_sheep(queue):
    if queue[-1]=='wolf':
        return 'Pls go away and stop eating my sheep'
    a=queue[::-1]
    for i in range(len(queue)):
        if a[i]=='wolf':
            return 'Oi! Sheep number'+' '+str(i) +'! You are about to be eaten by a wolf!'