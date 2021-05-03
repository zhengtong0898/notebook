#include "chainlist.h"


void test_chainlist(void) {

    Chain<std::string> * chain = new Chain<std::string>(10);

    chain->insert(0, "hello world!");
    chain->insert(1, "hello python!");
    chain->insert(2, "hello c++!");
    chain->insert(1, "hello rust!");
    chain->output(std::cout);

    std::cout << "\n\n\n" << std::endl;
    chain->erase(0);
    chain->output(std::cout);

    std::cout << "\n\n\n" << std::endl;
    std::cout << "chain->index_of('hello rust!'): " << chain->index_of("hello rust!") << std::endl;
    std::cout << "chain->index_of('hello python!'): " << chain->index_of("hello python!") << std::endl;
    std::cout << "chain->index_of('hello c++!'): " << chain->index_of("hello c++!") << std::endl;

    std::cout << "\n\n\n" << std::endl;
    std::cout << "chain->get(0): " << chain->get(0) << std::endl;
    std::cout << "chain->get(1): " << chain->get(1) << std::endl;
    std::cout << "chain->get(2): " << chain->get(2) << std::endl;

    return void();
}