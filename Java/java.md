# Java

<https://www.codecademy.com/resources/docs/java>

## Boilerplate

```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello World!");
  }
}
```

## Print

`System.out.println("Hello World!");`

## JVM

- Allows java to run on different os and platforms
  - "write once, run everywhere"
- Java program -> Compiler -> java bytecode -> JVM -> Machine Code (assembly)

## HashMap vs HashTable
[More Info](https://www.geeksforgeeks.org/differences-between-hashmap-and-hashtable-in-java/)
- HashMap preferred if thread synchronization is not needed
- HashMap allows one null key and multiple null values. Hashtable doesnt allow any null key or value.