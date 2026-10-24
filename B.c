#include <stdio.h>

int main()
{
    float instrest;
    int rate, min_balance, age, balance;
    char account_holder;
    printf("Enter Account Holder (m/f):");
    scanf("%c", &account_holder);
    printf("Enter age :");
    scanf("%d", &age);
    printf("Enter balance :");
    scanf("%d", &balance);

    if (account_holder == 'f')
    {
        if (age >= 60)
        {
            min_balance = 0;
            rate = 12;
        }
        else if (age <= 22)
        {
            min_balance = 0;
            rate = 4;
        }
        else
        {
            min_balance = 2000;
            rate = 8;
        }
    }
    else if (account_holder == 'm')
    {

        if (age >= 60)
        {
            min_balance = 2000;
            rate = 11;
        }
        else if (age <= 22)
        {
            min_balance = 500;
            rate = 2;
        }
        else
        {
            min_balance = 5000;
            rate = 6;
        }
    }

    if (balance >= min_balance)
    {
        printf("min_balance is maintained");
    }
    else
    {
        printf("min_balance is not maintained");
    }
    instrest = balance * rate / 100;
    printf("%d", &instrest);

    return 0;
}