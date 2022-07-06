//I will make a calculator that with different calculations like +, -, * and /


Console.WriteLine("This program is a simple calculator. Which one of these following calculations do you want to make?");
Console.WriteLine("Please type in a number.");

int use = 0;

while (true)
{
    Console.WriteLine("1. Addition, 2.Subtraction, 3.Division, 4.Multiplication, 5.Exit");
    double choice = Convert.ToDouble(Console.ReadLine());

    if (choice == 1)
    {
        Console.WriteLine("Please type in a number.");
        double x1 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Type in the second number.");
        double y1 = Convert.ToDouble(Console.ReadLine());
        double sum1 = x1 + y1;
        Console.WriteLine("The answer is {0}", sum1);
        use++;
    }
    else if (choice == 2)
    {
        Console.WriteLine("Please type in a number.");
        double x2 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Type in the second number.");
        double y2 = Convert.ToDouble(Console.ReadLine());
        double sum2 = x2 - y2;
        Console.WriteLine("The answer is {0}", sum2);
        use++;
    }
    else if (choice == 3)
    {
        Console.WriteLine("Please type in a number.");
        double x3 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Type in the second number.");
        double y3 = Convert.ToDouble(Console.ReadLine());
        double sum3 = x3 / y3;
        Console.WriteLine("The answer is {0}", sum3);
        use++;
    }
    else if (choice == 4)
    {
        Console.WriteLine("Please type in a number.");
        double x4 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Type in the second number.");
        double y4 = Convert.ToDouble(Console.ReadLine());
        double sum4 = x4 * y4;
        Console.WriteLine("The answer is {0}", sum4);
        use++;
    }
    else if (choice == 5)
    {
        if (use > 1)
        {
            Console.WriteLine("Thank you for using this program. You've used this program {0} times", use);
        }
        else
            Console.WriteLine("Thank you for using this program.");
        break;
    }
    else
        Console.WriteLine("Invalid input.");
}
