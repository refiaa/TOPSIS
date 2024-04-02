from Normalization import *

def Normalize_Decision_Matrix(Decision_Matrix, Attribute_Type, Normal_Method):
    Decision_Matrix = Decision_Matrix.astype(float)
    
    for i in range(0, len(Attribute_Type)):
        if Attribute_Type[i] == 1:
            Type = "profit"
        elif Attribute_Type[i] == 0:
            Type = "cost"
        else:
            print("Please, fill the correct attribute type")
        
        normalized_values = Normal_Method(Decision_Matrix.iloc[:, i], Type)
        Decision_Matrix.iloc[:, i] = normalized_values

    return Decision_Matrix
