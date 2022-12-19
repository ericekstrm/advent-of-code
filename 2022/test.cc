#include <iostream>

int main()
{
    for (long long i = 0; i < 1000000000000; ++i)
    {
        if (i % 10000000 == 0)
            std::cout << i / 1000000000000.0 * 100 << " %i\r";
    }
    std::cout << "Done" << std::endl;
}
