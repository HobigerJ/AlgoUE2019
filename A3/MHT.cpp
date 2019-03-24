#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <sstream>
#include <ctime>
#include <typeinfo>

using namespace std;

string Angabe;


void read_in() { // string read_in(string filename) {
        ifstream input_file ("rmHV_10_12"); //  ifstream input_file (filename);
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        Angabe = buffer.str();  // return buffer.str();
       
}


int main() {
    
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
    for (int c = 0; c < 90; c++) {
        if (Angabe[c] == '.') {
            char ch1 = Angabe[c-1];
            char ch2 = Angabe[c];
            char ch3 = Angabe[c+1];
            char ch4 = Angabe[c+2];
            string value;
            value += ch1;
            value += ch2; 
            value += ch3;
            value += ch4;
            float float_value = stof(value);
            cout << float_value << endl;
        }
    }
}