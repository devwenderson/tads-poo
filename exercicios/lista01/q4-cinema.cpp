#include <iostream>
using namespace std;

class Ingresso {
    public:
    string dia;
    short hora;

    Ingresso(string dia_arg, short hora_arg) {
        dia = dia_arg;
        hora = hora_arg;
    }

    short calcula_ingresso() {
        if (dia == "seg" || dia == "ter" || dia == "qui") {
            short valor = 16;
            if (hora == 0 || hora >= 17) {
                valor = valor * 1.5;
            }

            return valor;
        } 
        else if (dia == "qua") {
            short valor = 8;
            return valor;
        }
        else if (dia == "sex" || dia == "sab" || dia == "dom") {
            short valor = 20;
            if (hora == 0 || hora >= 17) {
                valor = valor * 1.5;
            }
            return valor;
        }
    }
};

class UI {
    public:
    string cabecalho;

    UI() {
        cabecalho = "========= Bem-vindo(a) ao seletor de ingressos =========";
    }

    void main() {
        cout << cabecalho << endl;
        int op = 0;
        while (op != 2) {
            op = this->menu();
            if (op == 1) {
                this->ingresso();
            };
        };
        cout << "========= Até a próxima =========" << endl;
    }

    int menu() {
        int op;
        short ARRAY_LENGTH = 2;
        string opcoes[ARRAY_LENGTH] = {"1 - Ingressos", "2 - Sair"};

        for (int i=0; i < ARRAY_LENGTH; ++i) {
            cout << opcoes[i] << endl;
        };

        cout << "Escolha um valor:" << endl;
        cin >> op;
        return op;
    }

    void ingresso() {
        cout << "Ingresso" << endl;
    }
};

int main() {
    UI ui;
    ui.main();
    return 0;
}