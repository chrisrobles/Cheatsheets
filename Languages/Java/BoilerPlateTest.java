public class BoilerPlateTest {
    public int a = 3;

    public int f(int b) {
        return 3 + b + a;
    }
    public int g(int a ) {
        return f(a);
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
        BoilerPlateTest testing = new BoilerPlateTest();
        System.out.println(testing.f(7));
        System.out.println("TEST");
    }
}