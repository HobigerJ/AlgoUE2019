#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <sstream>
#include <ctime>

using namespace std;

string Angabe;

void read_in() {
        ifstream input_file ("rmHV_10_12");
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        Angabe = buffer.str();
       
}


int main() {
    
    read_in();
    
    
}