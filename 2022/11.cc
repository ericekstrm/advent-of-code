#include <cmath>
#include <vector>
#include <deque>


class Monkey
{
public:
    
    Monkey(std::vector<int> starting_items, int worry_factor, int dividing_factor, int monkey_if_true, int monkey_if_false)
        : items {starting_items}, monkey_if_true {monkey_if_true}, monkey_if_false{monkey_if_false}, dividing_factor{dividing_factor}, worry_factor{worry_factor}
    {
    }
    virtual ~Monkey() = default;

    virtual void change_worry(int& old_worry) const = 0;
    void take_turn(std::vector<Monkey> & monkey_list)
    {
        while(!items.empty())
        {
            int item {items.front()};
            items.erase(items.begin());

            change_worry(item);
            item = static_cast<int>(std::floor(item / 3.0));
            if (item % dividing_factor == 0)
            {
                monkey_list[monkey_if_true].items.push_back(item);
            }
            else
            {
                monkey_list[monkey_if_false].items.push_back(item);
            } 
        }
    }

    std::vector<int> items;
    int monkey_if_true;
    int monkey_if_false;
    int dividing_factor;
    int worry_factor;

    int total_inspections {0};
};

class AMonkey : public Monkey
{
    using Monkey::Monkey;

    void change_worry(int& old_worry) const override
    {
        old_worry = old_worry + worry_factor;
    }
};

class MMonkey : public Monkey
{
    using Monkey::Monkey;

    void change_worry(int& old_worry) const override
    {
        old_worry = old_worry * worry_factor;
    }
};

int main()
{
    std::vector<Monkey*> monkeys;
    monkeys.push_back(new MMonkey({1,2,3}, 3,3,4,5));
    monkeys.push_back(new MMonkey({1,2,3}, 7,3,4,5));
    monkeys.push_back(new MMonkey({1,2,3}, 5,3,4,5));
    monkeys.push_back(new MMonkey({1,2,3}, 8,3,4,5));
    monkeys.push_back(new MMonkey({1,2,3}, 4,3,4,5));
    monkeys.push_back(new MMonkey({1,2,3}, 2,3,4,5));
    monkeys.push_back(new MMonkey({1,2,3}, 6,3,4,5));
    monkeys.push_back(new MMonkey({1,2,3},   3,4,5));

    int nr_of_rounds {20};

    for (int i = 0; i < nr_of_rounds; ++i)
    {
        for(Monkey& monkey : monkeys)
        {
            monkey.take_turn(monkeys);
        }
    }

}
