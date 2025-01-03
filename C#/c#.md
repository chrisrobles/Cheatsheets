# C\#
```c#
/*
 * C# Cheat Sheet
 *
 * C# is a general-purpose, strongly-typed, object-oriented multi-paradigm 
   programming language developed by Microsoft that runs on the .NET framework.
 * .NET is a open source, Microsoft supported, cross-platform platform for building applications.
 
 * Tools:
   Desktop Applications: WPF & Console Applications
   Web Applications: ASP.NET
   Access Data: ADO.NET & LINQ
   Cloud Apps: Windows Azure
 * Documentation: https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/
 * Tutorials: 
   https://www.codecademy.com/learn/learn-c-sharp/modules/learn-c-polymorphism/cheatsheet
   https://csharp-station.com/Tutorial/CSharp/SmartConsoleSetup.aspx
 * 
 */

using System;

class Program
{
    static void Main(string[] args)
    {
        /*
        Output
        */
        Console.WriteLine("Hello, World!\n");

        /*
        Input
        */
        string userInput = Console.ReadLine();

        /* 
        Math Library
        */
        double absValue = Math.Abs(x); // 80
        double sqRoot = Math.Sqrt(absValue); // 8.94427190999916
        double floored = Math.Floor(sqRoot); // 8
        double smaller = Math.Min(x, floored); // -80

        /*
        String Manipulation
        */
        string customGreeting = $"Lowercase version of your input, {userInput.ToLower()}!";
        userInput = "Hello, World!";
        userInput.ToUpper(); // "HELLO, WORLD!"
        userInput.IndexOf('o'); // 4
        string firstLetter = userInput[0]; // "H"
        string length = userInput.Length; // 13
        string subString = userInput.Substring(0, 5); // "Hello"
        string concat = "Hello, " + "World!"; // "Hello, World!"

        /*
        Conditional Statements
        */
        if(false) {}
        else if (false) {}
        else {}
        
        /*
        Arrays
        */
        int[] numbers = {3, 14, 59}; // skipping the `new int[]` only possible on initialization
        string[] people = new string[] { "Alice", "Bob", "Charlie" };
        int numPeople = people.Length;
        char[] letters = new char[26];

        /*
        Loops
        */
        for (int i = 0; i < 10; i++) {}
        foreach (string person in people) {}
        while (false) {}
        do {} while (false);

        /*
        Lists 
        - dynamic array
        */
        List<Object> someObjects = new List<Object>();
        List<string> names = new List<string> {"John", "Jane", "Jack"};
        names.Add("Jill");
        int numPeople = names.Count; // 4
        if(names.Contains("Jill"))
            Console.WriteLine("Jill is in the list");

        if(names.Remove("Jill"))
            Console.WriteLine("Jill removed");
        names.RemoveAt(1);
        names.Clear();

        string[] african = new string[] { "Cairo", "Johannesburg" };
        string[] asian = new string[] { "Delhi", "Seoul" };
        List<string> citiesList = new List<string>();
        // Add two lists
        citiesList.AddRange(african); // List: "Cairo", "Johannesburg"

        // Add two lists at index
        citiesList.InsertRange(0, asian); // List: "Delhi", "Seoul", "Cairo", "Johannesburg"

        // Remove multiple elements from list
        citiesList.RemoveRange(1, 2); // List: "Delhi", "Johannesburg"

        /*
        Dictionaries 
        - dynamic associative array
        */
        Dictionary<string,int> scores = new Dictionary<string, int>();

        /*
        Positional And Named Arguments
        */
        static void Print<T>(T value, string label = "")
        {
            Console.WriteLine($"{label}{value}");
        }
        // Positional arguments must come before named arguments
        Print(5, label: "Value: ");

        /*
        Out parameter 
        - return more than one value
        */
        static void GetFavoriteFoods(out string f1, out string f2, out string f3)
        {
            f1 = "Sushi";
            f2 = "Pizza";
            f3 = "Hamburgers";
        }
        string food1;
        string food2;
        string food3;
        GetFavoriteFoods(out food1, out food2, out food3);
        
        /*
        Objects
        */
        Person chris = new Person("Chris", "Robles");
        chris.Age = "26";

        /*
        Generics
        */
        MyGeneric<int> myInt = new MyGeneric<int>();
        myInt.value = 0;
    }
}
public class MyGeneric<T> {
     
    // private data members
    private T data;
    // using properties
    public T value
    {
        // using accessors
        get
        {
            return this.data;
        }
        set
        {
            this.data = value;
        }
    }
}

/*
Classes
*/
public class Person
{
    /*
    Explicit Backing Field
    */
    private string age; // FIELD
    public string Age // PROPERTY
    {
        get { return age; }
        set { age = value; }
    }

    /*
    Automatic Backing Field
    */
    // { get; set; } is a shorthand for defining a property with a hidden backing field.
    // The backing field is a private variable that stores the value of the property.
    public string LastName { get; set; } = string.Empty; // ""
    public string FirstName { get; set; } // null

    private static string species;
    public Person(string lastName, string firstName)
    {
        this.lastName = lastName;
        this.firstName = firstName;
    }
    public Person(string lname) : this(lname, "unknown") // constructor initializer
    
    /*
    Static Constructor
    - A static constructor is used to initialize any static data, 
    - or to perform a particular action that needs to be performed once only.
    */
    static Person()
    {
        species = "Homo sapien";
    }
    /*
    Virtual Method - Override methods in subclass
    - The parent method must be labeled as `virtual`

    */
    public virtual void CanDrink()
    {
        Console.WriteLine("Depends on the age");
    }
    public override string ToString() => $"{firstName} {lastName}".Trim();
}
/*
Inheritance
*/
public class Child: Person
{
    private static int maximumAge;
    // Call the parent constructor / super()
    public Child(string lastName, string firstName) : base(lastName, firstName)
    {}
    static Child() => maximumAge = 18;

    /*
    Override Method - override methods in subclass
    - When a subclass overrides a parent class's function it must be labeled as `override`
    */
    public override void CanDrink()
    {
        Console.WriteLine("Absolutely Not!");
    }
}
/*
Static Class
- Useful to provide set of tools
- Useful when you dont need to maintain any internal data
*/
public static class HumanPopulation
{
    private static long totalPopulation = 8000000000;
    
    public static long GetTotalPopulation()
    {
        return totalPopulation;
    }
    
    public static void UpdatePopulation(long newPopulation)
    {
        if (newPopulation > 0)
        {
            totalPopulation = newPopulation;
        }
    }
}

```