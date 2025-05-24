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
        // Instantiate
        List<Object> someObjects = new List<Object>();
        List<string> names = new List<string> {"John", "Jane", "Jack"};
        // Add
        names.Add("Jill");
        // Count
        int numPeople = names.Count; // 4
        if(names.Contains("Jill"))
            Console.WriteLine("Jill is in the list");
        // Remove, RemoveAt, Clear
        if(names.Remove("Jill"))
            Console.WriteLine("Jill removed");
        names.RemoveAt(1);
        names.Clear();
        // Contains
        if(names.Contains("Jill"))
            Console.WriteLine("Jill is in the list");
        // Add two lists
        string[] african = new string[] { "Cairo", "Johannesburg" };
        string[] asian = new string[] { "Delhi", "Seoul" };
        List<string> citiesList = new List<string>();
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
        LINQ
        - features for writing queries on collection types
        */
        using System.Linq;
        //var
        // // Method syntax
        var custQuery2 = customers.Where(cust => cust.City == "London");
        // // Query syntax
        var custQuery =  
            from cust in customers  
            where cust.City == "London"  
            select cust;
        // Foreach
        string[] names = { "Hansel", "Gretel", "Helga", "Gus" };
        var query = names.Where(n => n.Contains("a")); // n => n.Contains is lambda expression
        foreach (var name in query)
        {
            Console.WriteLine(name);
        }
        
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

        // is operator
        if (chris is Person)
        {
            Console.WriteLine("Chris is a Person");
        }

        // Downcasting - base class to derived class
        // // with as operator 
        Child christian = chris as Child;
        if (christian != null)
        {
            Console.WriteLine("Christian is a Child");
        }
        // // typecast
        Employee myEmployee = new Employee();
        Manager myManager = (Manager)myEmployee; // throws an exception if object isnt of derived type

        // Upcasting - derived class to base class
        Child myChild = new Child();
        Person myPerson = myChild;

        // Crow inherits from Bird, which inherits from Animal, and it implements IFly:
        class Bird : Animal
        { }
        class Crow : Bird, IFly
        { }
        // All of these references are valid:
        Crow crow = new Crow();
        Bird b = crow;
        Animal a = crow;
        IFly f = crow;

        // reference type matters not value type
        Cat c = new Cat();
        Animal a = c;
        c.Meow(); // OK, 'Meow()' is defined for the type 'Cat'
        a.Meow();
        // Error! 'Meow()' is not defined for the type 'Animal'

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
Class
*/   
public class HotSauce
{
    /*
    Properties vs. Fields
    */
    /*
    - Cant access the field without a property
    - You could make it public but that would break encapsulation
    */
    private string brand; // Field
    /*
    - Properties are used to access and modify private fields
    */
    public string Brand  // Property
    {
        get { return brand; }
        set { brand = value; }
    }
    /*
    Static Members - perform a particular action that only needs to be performed once
    */
    private static string flavor;
    static HotSauce() => flavor = "spicy";

    /*
    Explicit Backing Field
    - The backing field is a private variable that stores the value of the property.
    - Title is a property with an explicitly defined backing private field, title. Title also has an explicit getter and setter for accessing and modifying the field
    */
    private string title; // FIELD
    public string Title   // PROPERTY
    { 
        get 
        {
        return title;
        }
        set 
        {
        title = value;
        }
    }
    
    /*
    Automatic Backing Field
    - Origin is an auto-implemented property. A hidden, private backing field is automatically created during runtime, which the property will use behind the scenes. Explicit getters and setters are not need. This Origin property is functionally equivalent to the preceding Title property
    */
    public string Origin
    { get; set; } = string.Empty;

    /*
    ToString()
    - Override the ToString method to return a string representation of the object
    - Called when Console.WriteLine() is used
    */
    public override string ToString()
    {
        return $"Title: {Title}, Origin: {Origin}";
    }
}

/*
Inheritance
*/
class Employee {
    /*
    Virtual Method - The parent method can be overriden
    */
    public virtual void MakeHRRequest() {
        Console.WriteLine("Employee makes an HR request.");
    }
}
class Manager : Employee {
    /*
    Override Method - Subclass overrides a parent function
    */
    public override void MakeHRRequest() {
        Console.WriteLine("Manager makes an HR request.");
    }
    /*
    Constructor Initializer - this and base
    */
    public Manager(string lname) : this(lname, "unknown"){}
    public Manager(string fname, lname): base(fname, lname)
    {}
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

/*
Abstract Class
- Implements members and defines members that must be implemented by subclass
*/
abstract class Employee {
    // Must be implemented by the derived class
    public abstract void MakeHRRequest(); 
    public void ClockIn() {
        Console.WriteLine("Employee clocks in.");
    }
}
class Manager : Employee {
    public override void MakeHRRequest() {
        Console.WriteLine("Manager makes an HR request.");
    }
}

/*
Interface
- Defines members that a class must implement
*/

// The IAccount interface has three methods to implement.
public interface IAccount  // good practice to start name with I
{
    string AccountID { get; }
    void PayInFunds ( decimal amount );
    bool WithdrawFunds ( decimal amount );
    decimal GetBalance ();
}

// This CustomerAccount class is labeled with : IAccount, which means that it will implement that interface and its members must be defined
public class CustomerAccount : IAccount
{ }


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
        // Instantiate
        List<Object> someObjects = new List<Object>();
        List<string> names = new List<string> {"John", "Jane", "Jack"};
        // Add
        names.Add("Jill");
        // Count
        int numPeople = names.Count; // 4
        if(names.Contains("Jill"))
            Console.WriteLine("Jill is in the list");
        // Remove, RemoveAt, Clear
        if(names.Remove("Jill"))
            Console.WriteLine("Jill removed");
        names.RemoveAt(1);
        names.Clear();
        // Contains
        if(names.Contains("Jill"))
            Console.WriteLine("Jill is in the list");
        // Add two lists
        string[] african = new string[] { "Cairo", "Johannesburg" };
        string[] asian = new string[] { "Delhi", "Seoul" };
        List<string> citiesList = new List<string>();
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
        LINQ
        - features for writing queries on collection types
        */
        using System.Linq;
        //var
        // // Method syntax
        var custQuery2 = customers.Where(cust => cust.City == "London");
        // // Query syntax
        var custQuery =  
            from cust in customers  
            where cust.City == "London"  
            select cust;
        // Foreach
        string[] names = { "Hansel", "Gretel", "Helga", "Gus" };
        var query = names.Where(n => n.Contains("a")); // n => n.Contains is lambda expression
        foreach (var name in query)
        {
            Console.WriteLine(name);
        }
        
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

        // is operator
        if (chris is Person)
        {
            Console.WriteLine("Chris is a Person");
        }

        // Downcasting - base class to derived class
        // // with as operator 
        Child christian = chris as Child;
        if (christian != null)
        {
            Console.WriteLine("Christian is a Child");
        }
        // // typecast
        Employee myEmployee = new Employee();
        Manager myManager = (Manager)myEmployee; // throws an exception if object isnt of derived type

        // Upcasting - derived class to base class
        Child myChild = new Child();
        Person myPerson = myChild;

        // Crow inherits from Bird, which inherits from Animal, and it implements IFly:
        class Bird : Animal
        { }
        class Crow : Bird, IFly
        { }
        // All of these references are valid:
        Crow crow = new Crow();
        Bird b = crow;
        Animal a = crow;
        IFly f = crow;

        // reference type matters not value type
        Cat c = new Cat();
        Animal a = c;
        c.Meow(); // OK, 'Meow()' is defined for the type 'Cat'
        a.Meow();
        // Error! 'Meow()' is not defined for the type 'Animal'

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
Class
*/   
public class HotSauce
{
    /*
    Properties vs. Fields
    */
    /*
    - Cant access the field without a property
    - You could make it public but that would break encapsulation
    */
    private string brand; // Field
    /*
    - Properties are used to access and modify private fields
    */
    public string Brand  // Property
    {
        get { return brand; }
        set { brand = value; }
    }
    /*
    Static Members - perform a particular action that only needs to be performed once
    */
    private static string flavor;
    static HotSauce() => flavor = "spicy";

    /*
    Explicit Backing Field
    - The backing field is a private variable that stores the value of the property.
    - Title is a property with an explicitly defined backing private field, title. Title also has an explicit getter and setter for accessing and modifying the field
    */
    private string title; // FIELD
    public string Title   // PROPERTY
    { 
        get 
        {
        return title;
        }
        set 
        {
        title = value;
        }
    }
    
    /*
    Automatic Backing Field
    - Origin is an auto-implemented property. A hidden, private backing field is automatically created during runtime, which the property will use behind the scenes. Explicit getters and setters are not need. This Origin property is functionally equivalent to the preceding Title property
    */
    public string Origin
    { get; set; } = string.Empty;

    /*
    ToString()
    - Override the ToString method to return a string representation of the object
    - Called when Console.WriteLine() is used
    */
    public override string ToString()
    {
        return $"Title: {Title}, Origin: {Origin}";
    }
}

/*
Inheritance
*/
class Employee {
    /*
    Virtual Method - The parent method can be overriden
    */
    public virtual void MakeHRRequest() {
        Console.WriteLine("Employee makes an HR request.");
    }
}
class Manager : Employee {
    /*
    Override Method - Subclass overrides a parent function
    */
    public override void MakeHRRequest() {
        Console.WriteLine("Manager makes an HR request.");
    }
    /*
    Constructor Initializer - this and base
    */
    public Manager(string lname) : this(lname, "unknown"){}
    public Manager(string fname, lname): base(fname, lname)
    {}
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

/*
Abstract Class
- Implements members and defines members that must be implemented by subclass
*/
abstract class Employee {
    // Must be implemented by the derived class
    public abstract void MakeHRRequest(); 
    public void ClockIn() {
        Console.WriteLine("Employee clocks in.");
    }
}
class Manager : Employee {
    public override void MakeHRRequest() {
        Console.WriteLine("Manager makes an HR request.");
    }
}

/*
Interface
- Defines members that a class must implement
*/

// The IAccount interface has three methods to implement.
public interface IAccount  // good practice to start name with I
{
    string AccountID { get; }
    void PayInFunds ( decimal amount );
    bool WithdrawFunds ( decimal amount );
    decimal GetBalance ();
}

// This CustomerAccount class is labeled with : IAccount, which means that it will implement that interface and its members must be defined
public class CustomerAccount : IAccount
{ }

