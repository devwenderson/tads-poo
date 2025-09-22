#include <iostream>
using namespace std;

class Conta {
    public:
    string titular;
    string numero;
    double saldo;

    Conta(string titular, string numero, double saldo) {
        this->titular = titular;
        this->numero = numero;
        this->saldo = saldo;
    }

    void depositar(double valor) {
        saldo += valor;
    }

    void sacar(double valor) {
        saldo -= valor;
    }
    
};

int main() {
    Conta x("Wenderson", "123-X", 2938); // É uma instância | A instância possui o construtor da 
    // Conta& y = x; // y É uma referência para x
    // Conta* z = new Conta("Wenderson"); // z é um ponteiro para uma instância


    cout << "Titular: " << x.titular << endl;
    cout << "Numero: " << x.numero << endl;
    cout << "Saldo: " << x.saldo << endl;
    return 0;
}