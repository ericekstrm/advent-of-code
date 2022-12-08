#include <iostream>
#include <fstream>



int main()
{
    std::ifstream ifs {"6.txt"};

    std::string line;

    do
    {
        getline(ifs, line);

        std::istringstream iss {line};
        std::string part;
        iss >> part;
        if (part == turn
        
        
    } while(ifs);

}
