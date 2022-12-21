#include <fstream>
#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

template<typename T>
struct Dlist
{
    struct Node;

    Dlist(initializer_list<T> args)
        : head {}, size {}, pointer_list {}
    {
        for (auto&& v : args)
        {
            insert(v);
        }
    }
    Dlist(string const& file)
        : head {}, size {}, pointer_list {}
    {
        ifstream ifs {file};
        string line;
        while (ifs >> line)
        {
            insert(stoi(line));
        }
    }
            
        
    Dlist<T>(Dlist const&) = delete;
    Dlist<T>& operator=(Dlist<T> const&) = delete;
    
    
    void insert(T v)
    {
        v = v * 811589153;
        if ( head == nullptr )
        {
            head = new Node{ 0, 0, v };
            head->prev = head->next = head;
        } else
        {
            Node* last = head->prev;
            head->prev = new Node{ last, head, v };
            last->next = head->prev;
        }
        size++;
        pointer_list.push_back(head->prev);
    }

    void rotate_value(Node* ptr)
    {
        long long steps { ptr->value % (size - 1) };
        steps = steps < 0 ? steps + size - 1 : steps;

        if ( steps == 0)
        {
            cout << ptr->value << " does not move" << endl;
            return;
        }
        
        Node* curr {ptr};
        for(int i = 0; i < steps; ++i)
        {
            curr = curr->next;
        }

        // Delink the value
        ptr->next->prev = ptr->prev;
        ptr->prev->next = ptr->next;

        ptr->next = curr->next;
        ptr->prev = curr;

        curr->next->prev = ptr;
        curr->next = ptr;

        cout << ptr->value << " moves between " << ptr->prev->value << " and " << ptr->next->value << endl;
    }

    void rotate_all()
    {
        for(Node* p : pointer_list)
        {
            rotate_value(p);
            // cout << *this << endl;
        }
    }

    long long get_grove()
    {
        Node* curr = head;
        while(curr->value != 0)
        {
            curr = curr->next;
        }

        long long result {0};
        for (int i = 0; i < 3010; ++i)
        {
            if (i % 1000 == 0)
            {
                cout << "A grove coord is " << curr->value << endl;
                result += curr->value;
            }
            curr = curr->next;
        }
        cout << "The sum of the grove coords is " << result << endl;
        return result;
    }

    friend ostream& operator<<(ostream& os, Dlist<T> const& l)
    {
        Node* curr = l.head;
        os << "[" << curr->value;
        curr = curr->next;
        for (int i = 0; i < l.size - 1; ++i)
        {
            os <<  ", " << curr->value;
            curr = curr->next;
        }
        os << "]";
        return os;
    }

    struct Node
    {
        Node* prev;
        Node* next;
        T value;
    };
    Node* head;
    int size {};
    vector<Node*> pointer_list;

};

int main()
{
    Dlist<long long> l {"20.txt"}; 
    for (int i = 0; i < 10; i++)
    {
        l.rotate_all();
    }
    l.get_grove();
}
