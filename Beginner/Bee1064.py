#Read 6 values that can be floating point numbers. 
# After, print how many of them were positive. 
# In the next line, print the average of all positive values typed, with one digit after the decimal point.
values = []
positiveValues = []
for i in range(6):
    values.append(float(input("")))
    
    
for value in values:
    if value > 0:
        positiveValues.append(value)

avg = sum(positiveValues)/len(positiveValues)
print(f'{len(positiveValues)} valores positivos')
print(f'{avg:.1f}')