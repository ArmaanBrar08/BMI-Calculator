                   #Intorducing AI#

print("Hello, this program allows the user to calculate BMI");

print("B - Body, M - Mass, I - Index");

Answer_1 = input("Are you ready: ");
if Answer_1 == 'No':
    input("How come: ");
    print("Sorry you feel that way.");
    
if Answer_1 == 'Yes':
    print("Ok, sounds good");
    
Answer_2 = input("This calculator asks for your height and weight, is that okay: ");

if Answer_2 == 'No':
    input("How come: ");
    print('Sorry you feel that way.');
elif Answer_2 == 'Yes':
    print("Ok, sounds good");
    
print("If you would, convert your weight into Kilograms (kg)");

print("And your height in meters (m)");

                  #BMI CALCULATOR#

weight = float(input("Enter your weight in kilograms (kg): "));
height = float(input("Enter your height in meters (m): "));

bmi = weight / (height * height)

if bmi < 18.5:
    print("You are underweight, you must eat more!");
elif bmi > 25:
    print("You are overweight, you must eat less");
elif 18.25 < bmi < 25:
    print("You are healthy, keep up the good work");
    
Answer_3 = input("Would you like to see your BMI: ");

if Answer_3 == 'Yes':
    print("Your BMI is " + bmi);
elif Answer_3 == 'No':
    print("That's okay, Have a great day");