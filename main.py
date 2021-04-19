import random;
import check;

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [Rock,Paper,scissors];
a = "";
while a!= "you win":
  user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors:   "));

  computer_choice = random.randint(0,2);
  if user_choice <= 3 and user_choice >= 0:
    print (list[user_choice]);
    print ("\n computer chose : \n");
    print(list[computer_choice]);

  a =check.check(user_choice, computer_choice);
  print (a);
