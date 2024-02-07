#include <iostream>

using namespace std;

double celsiusToFahrenheit(double celsius){
    return (celsius * (9.0/5.0)) + 32;
}
double fahrenheitToCelsius(double fahrenheit){
    return (fahrenheit - 32) * (5.0/9.0);
}
double celsiusToKelvin(double celsius){
    return celsius + 273.15;
}
double fahrenheitToKelvin(double fahrenheit){
    return (fahrenheit + 459.67) * (5.0/9.0);
}
double kelvinToCelsius(double kelvin){
    return kelvin - 273.15;
}
double kelvinToFahrenheit(double kelvin){
    return (kelvin * (9.0/5.0)) - 459.67;
}

int main(){
    char repeat;
    do {
        double celsius, fahrenheit, kelvin;
        cout << "1. Celsius to Fahrenheit" << endl;
        cout << "2. Fahrenheit to Celsius" << endl;
        cout << "3. Celsius to Kelvin" << endl;
        cout << "4. Fahrenheit to Kelvin" << endl;
        cout << "5. Kelvin to Celsius" << endl;
        cout << "6. Kelvin to Fahrenheit" << endl;
        cout << "Enter your choice: ";

        int choice, temperature;
        if (!(cin >> choice)){
            cout << "Invalid input" << endl;
            return 0;
        }
        else{
            cout << "Enter temperature: ";
            cin >> temperature;
            }

        double convertedTemperature;
        switch (choice){
            case 1:
                convertedTemperature = celsiusToFahrenheit(temperature);
                break;
            case 2:
                convertedTemperature = fahrenheitToCelsius(temperature);
                break;
            case 3:
                convertedTemperature = celsiusToKelvin(temperature);
                break;
            case 4:
                convertedTemperature = fahrenheitToKelvin(temperature);
                break;
            case 5:
                convertedTemperature = kelvinToCelsius(temperature);
                break;
            case 6:
                convertedTemperature = kelvinToFahrenheit(temperature);
                break;
        }
        cout << endl << endl << "Converted temperature: " << convertedTemperature << endl << endl;
        cout << "Do you want to exit the program? (y/n): ";
        cin >> repeat;
    } while (repeat == 'n' || repeat == 'N');
}