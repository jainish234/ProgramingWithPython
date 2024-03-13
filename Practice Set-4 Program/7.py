# 7) Accept the string from the user; display the count of vowels and consonants.

str=input("Please enter a string as you wish: ");
vowels=0
consonants=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;#vowel counter is incremented by 1
    else:
        consonants=consonants+1;
#consonant counter is incremented by 1
print("The number of vowels:",vowels);
print("\nThe number of consonant:",consonants);

output:=
Please enter a string as you wish: python language
The number of vowels: 5

The number of consonant: 10