#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

struct vec2
{
    int x, y;
    vec2 operator+(vec2 const& rhs) const { return vec2{x + rhs.x, y + rhs.y}; }
    bool operator==(vec2 const& rhs) const { return x == rhs.x and y == rhs.y; }
    bool operator<(vec2 const& rhs) const { return (x * 10 + y) < (rhs.x * 10 + rhs.y); }
};

set<vec2> get_shape(int shape_nr, vec2 const& pos)
{
    vector<set<vec2>> shapes {}; 
    shapes.push_back({ { 0,0 }, { 1,0 }, { 2,0 }, { 3,0 } });
    shapes.push_back({ { 1,0 }, { 0,1 }, { 1,1 }, { 2,1 }, { 1,2 } });
    shapes.push_back({ { 2,2 }, { 2,1 }, { 0,0 }, { 1,0 }, { 2,0 } });
    shapes.push_back({ { 0,0 }, { 0,1 }, { 0,2 }, { 0,3 } });
    shapes.push_back({ { 0,0 }, { 1,0 }, { 0,1 }, { 1,1 } });
    set<vec2> target_set {};
    transform(begin(shapes[shape_nr]),
              end(shapes[shape_nr]),
              inserter(target_set, begin(target_set)),
              [](vec2 p) -> vec2
              {
                  return p;
              });
    return target_set;
}

class Rock
{
public:
    Rock(int shape_nr, vec2 pos)
        : tiles{get_shape(shape_nr, pos)}
    {}

    void move(int vx, int vy)
    {
    }

    void push(string const& wind_direction)
    {
    }

    bool push_down(set<vec2> const& tiles)
    {
    }

    set<vec2> tiles;
    
    bool collided(set<vec2> const& tiles)
    {
    }
};

void print_grid(Rock const& rock, set<vec2> const& tiles, int max_height)
{
    for (int row = max_height + 10; row >= 0; --row)
    {
        cout << "|";
        for (int col = 0; col < 7; ++col)
        {
            if (find(begin(tiles), end(tiles), vec2{col, row}) != end(tiles))
            {
                cout << "#";
            } else if (find(begin(rock.tiles), end(rock.tiles), vec2{col, row}) != end(rock.tiles))
            {
                cout << "@";
            } else
            {
                cout << ".";
            }
        }
        cout << "|" << endl;
    }
    cout << "+-------+" << endl;
}

    
int main()
{

}
