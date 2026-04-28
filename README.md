## Model Used
distilbert-base-uncased-finetuned-sst-2-english

## Sample Output
(See output.png)

## Analysis of Incorrect Predictions

"I have a pen."  
- Predicted: Negative  
- Issue: Sentence is neutral, but model assigns sentiment unnecessarily.

"She went to the store."  
- Predicted: Negative  
- Issue: Model fails to recognize neutral factual statements.

## Conclusion
- Model works well for clear sentiment  
- Struggles with neutral sentences  
- Confidence score helps identify uncertainty