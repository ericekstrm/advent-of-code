
#include <vector>
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>

void move(std::string& s1, std::string& s2)
{
    char to_move {*(s1.end() - 1)};

    s1.erase(s1.end() - 1);
    s2.push_back(to_move);
}

void move_many(std::string& s1, std::string& s2, int amount)
{
    std::string to_move {(s1.end() - amount), s1.end()};

    s1.erase(s1.end() - amount, s1.end());
    s2.append(to_move);
}

int main()
{
    int nr_of_stacks {9};
    std::map<int, std::string> m {};
    m[1] = "DMSZRFWN";
    m[2] = "WPQGS";
    m[3] = "WRVQFNJC";
    m[4] = "FZPCGDL";
    m[5] = "SPT";
    m[6] = "HDFWRL";
    m[7] = "ZNDC";
    m[8] = "WNRFVSJQ";
    m[9] = "RMSGZWV";

    std::ifstream ifs {"5.txt"};

    std::string line;
    do {
        getline(ifs, line);
    } while(line != "");

    while(true) {
        getline(ifs, line);
        if (!ifs)
        {
            break;
        }
        std::istringstream iss {line};
        std::string part {};
        iss >> part >> part;
        int amount {stoi(part)};
        iss >> part >> part;
        int origin {stoi(part)};
        iss >> part >> part;
        int destination {stoi(part)};

        move_many(m[origin], m[destination], amount);

        
    } 

    for(int i; i <= nr_of_stacks; ++i)
    {
        std::cout << *(m[i].end() - 1);
    }
}
