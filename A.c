#include <stdio.h>

int main()
{

    int marks;
    printf("Enter Marks :");

    scanf("%d", &marks);

    if (marks < 0 || marks > 100)
    {
        printf("Invalid input");
    }
    else if (marks >= 75)
    {
        printf("Distinction");
    }
    else if (marks >= 60)
    {
        printf("First Division");
    }
    else if (marks >= 45)
    {
        printf("Second Division");
    }
    else if (marks >= 33)
    {
        printf("Third Division");
    }
    else
    {
        printf("Fail");
    }

    return 0;
}