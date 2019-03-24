#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <sstream>
#include <ctime>
#include <typeinfo>

using namespace std;

string Angabe;
class Matrix {
    private:
        int werteanz;
        int spaltenanz;
        int zeilenanz;

    public:
        int getWerteanz() {
            return werteanz;
        }
        int getSpaltenanz() {
            return spaltenanz;
        }
        int getZeilenanz() {
            return zeilenanz;
        }

        void setZeilenanz(int za) {
            zeilenanz = za;
        }

        void setSpaltenanz(int sa) {
            spaltenanz = sa;
        }
        void setWerteanz(int wa) {
            werteanz = wa;
        }

};

void read_in() { // string read_in(string filename) {
        ifstream input_file ("rmHV_10_12"); //  ifstream input_file (filename);
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        Angabe = buffer.str();  // return buffer.str();
       
}



Matrix gibmireins(string Angabe) {

    //hier werden zeilenanz etc berechnet....
    
    Matrix m;
    m.setSpaltenanz(1);
    m.setSpaltenanz(1);

    return m;
}



int main() {
    


    Matrix m;
    m.setSpaltenanz(1);
    m.getSpaltenanz();
    

    cout << "Spaltenanz: " << gibmireins("blah!").getZeilenanz();




    // string eingabe;
    // cin >> eingabe;
    // string Angabe;
    read_in(); // Angabe = read_in(eingabe);
    // groesse rausfinden
    
    int number_values_matrix1 = 0;
    int number_rows_matrix1 = 0;
        
    for (int k = 0; k < Angabe.length(); k++) {  // 45 = -, 46 = .
        if (Angabe[k] == 46) {
            number_values_matrix1 += 1;
        } 
        if (Angabe[k] == '\n') {
            number_rows_matrix1 += 1;
        }
        if (Angabe[k] == '-') {
            break;
        }
    }
    number_rows_matrix1 -= 1;
    int number_columns_matrix1 = number_values_matrix1 / number_rows_matrix1; // spalten = Werte / Reihen

    // werte, Reihen, Spalten für matrix 2
    int number_values_matrix2 = number_values_matrix1;
    int number_rows_matrix2 = number_rows_matrix1 + 1;
    int number_columns_matrix2 = number_columns_matrix1 - 1;

    // matrix1 und matrix2 deklarieren
    float matrix1[number_rows_matrix1][number_columns_matrix1];
    float matrix2[number_rows_matrix2][number_columns_matrix2];
    
    // matrix 1   
    int cursor = 0;
    for (int y = 0; y < number_rows_matrix1; y++) {
        for (int x = 0; x < number_columns_matrix1; x++) {
            while (Angabe[cursor] != 46) {
                cursor ++;
                
            }
            
            char ch1 = Angabe[cursor - 1];
            char ch2 = Angabe[cursor];
            char ch3 = Angabe[cursor + 1];
            char ch4 = Angabe[cursor + 2];
            string value;
            value += ch1;
            value += ch2; 
            value += ch3;
            value += ch4;
            float float_value = stof(value);
            matrix1[x][y] = float_value;
            cursor ++;   
        }
    } 
    
}