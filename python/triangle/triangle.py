def equilateral(sides):
    # side can't have 0 length
    if any(side == 0 for side in sides):
        return False
    
    # triangle sum of sides violation
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False

    # if all sides are equal
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False

def isosceles(sides):
    # side can't have 0 length
    if any(side == 0 for side in sides):
        return False
    
    # triangle sum of sides violation
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    
    # At least 2 sides are equal
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    return False 

def scalene(sides):
    # side can't have 0 length
    if any(side == 0 for side in sides):
        return False
    
    # triangle sum of sides violation
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    
    # At least 2 sides are equal
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True
    return False 
