#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <memory>

// Entry point of the program
int main() {

    // Print
    std::cout << "Hello, World!" << std::endl;

    // Input
    int input;
    std::cout << "Enter a number: ";
    std::cin >> input;

    // Variables and Data Types
    int a = 10;
    double b = 20.5;
    char c = 'A';
    int arr[] = {1, 2, 3, 4, 5};

    // Vectors (dynamic arrays)
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.push_back(6); // Add element to the end
    vec.pop_back(); // Remove element from the end
    vec.insert(vec.begin() + 2, 10); // Insert element at index 2
    vec.erase(vec.begin() + 3); // Remove element at index 3
    vec.clear(); // Remove all elements
    vec.resize(10, 0); // Resize the vector and fill with 0

    // foreach
    for (int i : vec) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // Functions
    auto add = [](int x, int y) -> int {
        return x + y;
    };
    std::cout << "Sum: " << add(3, 4) << std::endl;

    // Loops
    for (int i = 0; i < 5; ++i) {
        std::cout << "i: " << i << std::endl;
    }

    // Standard Library Containers
    std::map<std::string, int> myMap;
    myMap["one"] = 1;
    myMap["two"] = 2;

    for (const auto& pair : myMap) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    std::set<int> mySet = {1, 2, 3, 4, 5};
    mySet.insert(6);

    for (int elem : mySet) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // Algorithms
    std::sort(vec.begin(), vec.end());
    for (int i : vec) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // Pointers
    int* ptr = &a;
    std::cout << "Pointer value: " << *ptr << std::endl;

    // References
    int& ref = a;
    ref = 20;
    std::cout << "Reference value: " << a << std::endl;

    // Classes and Objects
    class Person {
    public:
        std::string name;
        int age;

        Person(std::string n, int a) : name(n), age(a) {}

        void display() const {
            std::cout << "Name: " << name << ", Age: " << age << std::endl;
        }
    };

    Person person("John", 30);
    person.display();

    // Inheritance
    class Employee : public Person {
    public:
        int employeeId;

        Employee(std::string n, int a, int id) : Person(n, a), employeeId(id) {}

        void display() const {
            Person::display();
            std::cout << "Employee ID: " << employeeId << std::endl;
        }
    };

    Employee employee("Alice", 28, 12345);
    employee.display();

    // Exception Handling
    try {
        if (b == 0) {
            throw std::runtime_error("Division by zero error");
        }
        std::cout << "Result: " << a / b << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Exception caught: " << e.what() << std::endl;
    }

    // Lambda Functions with Capture
    int x = 10;
    int y = 20;
    auto multiply = [x, y]() -> int {
        return x * y;
    };
    std::cout << "Product: " << multiply() << std::endl;

    // Smart Pointers
    std::unique_ptr<int> uniquePtr = std::make_unique<int>(42);
    std::cout << "Unique Pointer value: " << *uniquePtr << std::endl;

    std::shared_ptr<int> sharedPtr1 = std::make_shared<int>(100);
    std::shared_ptr<int> sharedPtr2 = sharedPtr1;
    std::cout << "Shared Pointer value: " << *sharedPtr1 << ", use count: " << sharedPtr1.use_count() << std::endl;

    return 0;
}