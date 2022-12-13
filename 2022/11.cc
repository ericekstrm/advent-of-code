#include <cmath>
#include <list>
#include <vector>
#include <deque>
#include <iostream>

class Monkey
{
public:
    
    Monkey(std::list<long long> starting_items, int worry_factor, int dividing_factor, int monkey_if_true, int monkey_if_false)
        : items {starting_items}, monkey_if_true {monkey_if_true}, monkey_if_false{monkey_if_false}, dividing_factor{dividing_factor}, worry_factor{worry_factor}
    {
    }
    virtual ~Monkey() = default;

    virtual void change_worry(long long& old_worry) const = 0;
    void take_turn(std::vector<Monkey*> & monkey_list)
    {
        while(!items.empty())
        {
            long long item {items.front()};
            items.pop_front();
            total_inspections++;

            change_worry(item);
            // item = item / 3;
            item %= 9699690;
            if (item % dividing_factor == 0)
            {
                monkey_list[monkey_if_true]->items.push_back(item);
            }
            else
            {
                monkey_list[monkey_if_false]->items.push_back(item);
            } 
        }
    }

    std::list<long long> items;
    long long monkey_if_true;
    long long monkey_if_false;
    long long dividing_factor;
    long long worry_factor;

    long long total_inspections {0};
};

class AMonkey : public Monkey
{
public:
    using Monkey::Monkey;

    void change_worry(long long& old_worry) const override
    {
        old_worry = old_worry + worry_factor;
    }
};

class MMonkey : public Monkey
{
public:
    using Monkey::Monkey;

    void change_worry(long long& old_worry) const override
    {
        old_worry = old_worry * worry_factor;
    }
};

class CMonkey : public Monkey
{
public:
    CMonkey(std::list<long long> starting_items, int worry_factor, int monkey_if_true, int monkey_if_false)
        : Monkey{starting_items, 0, worry_factor, monkey_if_true, monkey_if_false}
    {
    }

    void change_worry(long long& old_worry) const override
    {
        old_worry = old_worry * old_worry;
    }
};

void print_monkeys(std::vector<Monkey*> const& monkeys)
{
    long long i {0};
    for (Monkey* m : monkeys)
    {
        std::cout << "Monkey " << i << ": ";
        for (long long w : m->items)
        {
            std::cout << w << ", ";
        }
        std::cout << std::endl;
        ++i;
    }
}
        
int main()
{
    std::vector<Monkey*> monkeys;
    monkeys.push_back(new MMonkey({78, 53, 89, 51, 52, 59, 58, 85}, 3, 5, 2, 7));
    monkeys.push_back(new AMonkey({64},                             7, 2, 3, 6));
    monkeys.push_back(new AMonkey({71, 93, 65, 82},                 5,13, 5, 4));
    monkeys.push_back(new AMonkey({67, 73, 95, 75, 56, 74},         8,19, 6, 0));
    monkeys.push_back(new AMonkey({85, 91, 90},                     4,11, 3, 1));
    monkeys.push_back(new MMonkey({67, 96, 69, 55, 70, 83, 62},     2, 3, 4, 1));
    monkeys.push_back(new AMonkey({53, 86, 98, 70, 64},             6, 7, 7, 0));
    monkeys.push_back(new CMonkey({88, 64},                           17, 2, 5));

    // monkeys.push_back(new MMonkey({79, 98},        19,23, 2, 3));
    // monkeys.push_back(new AMonkey({54, 65, 75, 74}, 6,19, 2, 0));
    // monkeys.push_back(new CMonkey({79, 60, 97},       13, 1, 3));
    // monkeys.push_back(new AMonkey({74},             3,17, 0, 1));

    long long nr_of_rounds {10000};

    for (long long i = 0; i < nr_of_rounds; ++i)
    {
        // std::cout << "-==============-" << std::endl;
        // std::cout << "Round " << i + 1 << std::endl;
        for(Monkey* monkey : monkeys)
        {
            monkey->take_turn(monkeys);
        }
        // print_monkeys(monkeys);

        if ((i + 1) % 1000 == 0)
        {
            long long x {};
            std::cout << "-============-" << std::endl;
            std::cout << "Round " << i + 1 << std::endl;
            for(Monkey* m : monkeys)
            {
                std::cout << "Monkey " << x++ << ": " << m->total_inspections << std::endl;
            }
        }
    }
}
