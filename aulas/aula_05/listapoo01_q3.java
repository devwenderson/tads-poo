class Conta {
    public String titular;
    public String numero;
    public double saldo;

    public Conta(String titular, String numero, double saldo) {
        this.titular = titular;
        this.numero = numero;
        this.saldo = saldo;
    }

    public void depositar(double saldo) {
        this.saldo += saldo;
    }

    public void sacar(double saldo) {
        this.saldo -= saldo;
    }
}

public class listapoo01_q3 {
    public static void main(String[] args) {
        Conta conta1 = new Conta("Wenderson", "123-X", 2000);
        System.out.println(conta1.titular + " " + conta1.numero);
    }
}