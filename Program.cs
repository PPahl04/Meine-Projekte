using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OddEven
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //This program will tell you if the number you've entered is odd or even.

            Console.WriteLine("Please put in a number (not 0).");
            Console.WriteLine("Type in exit in to end the loop.");
            int use = 0;
            while (true)
            {
                string input = Console.ReadLine();
                if (input == "exit")
                {
                    Console.WriteLine("Thank you for using this program. You've used this program {0} times.", use);
                    break;
                }
                else
                {
                    ++use;
                    int number = Convert.ToInt32(input);

                    if (number == 0)
                    {
                        Console.WriteLine("Please put in a number that is not 0.");
                    }
                    else if (number % 2 == 0)
                    {
                        Console.WriteLine("The number {0} is even.", number);
                    }
                    else
                    {
                        Console.WriteLine("The number {0} is odd", number);
                    }
                }
            }
                   
        }
    }
}
