using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AgeGroup

{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter your age.");
            int age = Convert.ToInt32(Console.ReadLine());
            if (age <= 1)
            {
                Console.WriteLine("You are {0} years old, which makes you an infant.", age);
            }
            else if (age <= 4)
            {
                Console.WriteLine("You are {0} years old, which makes you a toddler.", age);
            }
            else if (age <= 12)
            {
                Console.WriteLine("You are {0} years old, which makes you a child.", age);
            }
            else if (age <= 17)
            {
                Console.WriteLine("You are {0} years old, which makes you a teenager.", age);
            }
            else if (age <= 19)
            {
                Console.Write("You are {0} years old, which makes you a teenager. You are also a young adult.", age);
            }
            else if (age <= 39)
            {
                Console.WriteLine("You are {0} years old, which makes you an adult.", age);
            }
            else if (age <= 59)
            {
                Console.WriteLine("You are {0} years old, which makes you a middle aged adult.", age);
            }
            else if (age <= 110)
            {
                Console.WriteLine("You are {0} years old, which makes you a senior.", age);
            }
            else if (age > 110)
            {
                Console.WriteLine("You are {0} years old... Which isn't possible for humans.", age);
            }

        }
    }
}
