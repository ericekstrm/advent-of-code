
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <iterator>


int priority(char item_type)
{
    if (std::isupper(item_type))
    {
        return item_type - 'A' + 27;
    }
    else
    {
        return item_type - 'a' + 1;
    }
}

void part1()
{
    std::ifstream ifs {"3.txt"};

    int result{};
    std::string line;
    while(ifs >> line)
    {
        auto middle = line.begin() + line.size() / 2;
        std::string output{"   "};
        std::sort(line.begin(), middle);
        std::sort(middle, line.end());
        std::set_intersection(line.begin(), middle, middle, line.end(), output.begin());
        result += priority(output[0]);
    }
    std::cout << result << std::endl;
}
        
void part2()
{
    std::ifstream ifs {"3.txt"};

    int result{};
    std::string l1, l2, l3;
    while(ifs >> l1 >> l2 >> l3)
    {
        std::sort(l1.begin(), l1.end());
        std::sort(l2.begin(), l2.end());
        std::sort(l3.begin(), l3.end());
        std::string out1;
        std::string out2;
        std::set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(), std::back_inserter(out1));
        std::set_intersection(out1.begin(), out1.end(), l3.begin(), l3.end(), std::back_inserter(out2));
        std::cout << out2 << std::endl;
        result += priority(out2[0]);
    }
    std::cout << result << std::endl;
}

int main()
{
        
    part1();
    part2();
}
