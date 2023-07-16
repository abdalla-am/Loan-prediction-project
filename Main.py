# imporing Modules
import Preprocessing
import Feature_Selection_Splitting
import Logistic_Regression
import Decision_Tree
import SVM
import Getter


#Data Cleaning & Preprocessing & Data Scaling :-
loan_Df = Preprocessing.Preprocessing()

#Feature Selection & Data Splitting :-
ReadyData = Feature_Selection_Splitting.feature_selection_and_data_Splitting(loan_Df)
print ('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
print('                                                                      -* Welcome to our Loan Predictor *-\n')

while(True):
    print('Press :')
    print('-------')
    print('     1 --> To Show Models and accuracy.')
    print('     2 --> To Predict Loan Status.\n')
    Option = input ('    Option ==> ')
    if(Option != '1' and Option != '2'):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('         Invalid !')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        continue
    else:
        break

#when user choose to view Models :-
if (Option == '1'):
    while(True):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Please Select The algorithm you want : ')
        print('---------------------------------------')
        print('     1 --> for Logistic Regression.')
        print('     2 --> for Support Vector Machine.')
        print('     3 --> for Decision Tree.')
        print('     4 --> for All Algorithms.\n')
        fOption = input('    Option ==> ')
        if(fOption != '1' and fOption != '2' and fOption != '3' and fOption != '4'):
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('         Invalid !')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            continue
        else:
            break
        
    if (fOption == '1'):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Logistic_Regression.Logistic_algorirthm(ReadyData)
    elif (fOption == '2'):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        SVM.SVM_Algorithm(ReadyData)
    elif (fOption == '3'):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Decision_Tree.Decision_Tree_Algoithm(ReadyData)
    elif (fOption == '4'):    
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Logistic_Regression.Logistic_algorirthm(ReadyData)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        SVM.SVM_Algorithm(ReadyData)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Decision_Tree.Decision_Tree_Algoithm(ReadyData)

#When User choose to predict !
elif (Option == '2'):
    features = Getter.FeaturesGetter()
    while(True):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Please Select The algorithm you want : ')
        print('---------------------------------------')
        print('     1 --> for Logistic Regression.')
        print('     2 --> for Support Vector Machine.')
        print('     3 --> for Decision Tree.')
        print('     4 --> for All Algorithms.\n')
        sOption = input('    Option ==> ')
        if(sOption != '1' and sOption != '2' and sOption != '3' and sOption != '4'):
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('         Invalid !')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            continue
        else:
            break
        
    if (sOption == '1'):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Logistic_Regression.Logistic_Predictor(ReadyData, features)
    elif (sOption == '2'):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        SVM.SVM_Predictor(ReadyData, features)
    elif (sOption == '3'):
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Decision_Tree.ID3_Predictor(ReadyData, features)
    elif (sOption == '4'):    
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Logistic_Regression.Logistic_Predictor(ReadyData, features)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        SVM.SVM_Predictor(ReadyData, features)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        Decision_Tree.ID3_Predictor(ReadyData, features)

print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')