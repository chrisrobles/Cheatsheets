# C++

## foreach

```c++
int myNumbers[5] = {10, 20, 30, 40, 50};
for (int i : myNumbers) {
  cout << i << "\n";
}
// reference the data without creating a copy
for (auto &i : myNumbers) {
    cout << i << "\n";
}
```

## structs

like an object with only properties

```c++
struct car {
  string brand;
  string model;
  int year;
} volvo;
volvo.myNum = 5;
car bmw; // declare another car
```

## enums

custom data types with custom values

```c++
enum Level {
  LOW,
  MEDIUM,
  HIGH
};
```

## References

Refer to the same variable

```c++
string food = "Pizza";
string &meal = food;

cout << food;  // Outputs Pizza
cout << meal;  // Outputs Pizza
cout << &food; // Outputs 0x6dfed64
```

## Pointers

Save the memory address of the variable

```c++
int x = 5;
int* y = &x;
cout << *x; // 5
cout << x; // address 0x5
cout << y; // address 0x5
*x = 10;
cout << *y; // 10

```