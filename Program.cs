using System;

namespace BetterCalculator
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is a calculator. What calculation do you want to perform?");
            Console.WriteLine("1. Addition, 2.Subtraction, 3.Multiplication, 4.Division, 5.Modulus");
            int choice = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Input the first number");
            int x = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Input the second number");
            int y = Convert.ToInt32(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        Console.WriteLine("{0} added by {1} equals {2}", x, y, x + y);
                        break;
                    case 2:
                        Console.WriteLine("{0} subtracted by {1} equals {2}", x, y, x - y);
                        break;
                    case 3:
                        Console.WriteLine("{0} multiplied by {1} equals {2}", x, y, x * y);
                        break;
                    case 4:
                        Console.WriteLine("{0} divided by {1} equals {2}", x, y, x / y);
                        break;
                    case 5:
                        Console.WriteLine("{0} fits in {1} {2} times.", y, x, x / y);
                        Console.WriteLine("The remainder of {0} and {1} is {2}", x, y, x % y);
                        break;
                    default:
                        Console.WriteLine("Invalid input. Make sure you've typed in one of the options at the start.");
                        break;
                }
        }
    }
}
