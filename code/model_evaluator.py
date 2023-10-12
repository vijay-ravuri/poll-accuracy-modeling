# Fuction used to plot a Confusion Matrix and calculate performance metrics for models
# Originally adapted (minorly) from lesson 2.14, taken directly from Vijay's Project 3


from sklearn.metrics import ConfusionMatrixDisplay, f1_score, \
    recall_score, precision_score, accuracy_score


def evaluation(X_test, y_test, model):
    ConfusionMatrixDisplay.from_estimator(model, 
                                          X_test, 
                                          y_test, 
                                          cmap='Blues', 
                                          display_labels = ['Wrong Call', 'Right Call'])
    preds = model.predict(X_test)
    
    acc = accuracy_score(y_test, preds)
    recall = recall_score(y_test, preds)
    prec = precision_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    print(f'accuracy: {acc}')
    print(f'recall: {recall}')
    print(f'precision: {prec}')
    print(f'f1 score: {f1}')

    return {
        'accuracy': acc,
        'recall': recall,
        'precision': prec,
        'f1_score': f1
    }