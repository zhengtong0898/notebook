#include <iostream>
#include <assert.h>


struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};


class AddTwoNumbers {
public:
    ListNode* add_two_numbers(ListNode* left_node, ListNode* right_node) {
        ListNode* current = new ListNode();
        ListNode* root = current;

        int carry = 0;

        while (left_node || right_node || carry) {

            if (left_node) {
                carry += left_node->val;
                left_node = left_node->next;
            }

            if (right_node) {
                carry += right_node->val;
                right_node = right_node->next;
            }

            current->next = new ListNode(carry % 10);
            current = current->next;
            carry = static_cast<int>(carry / 10);

        }

        return root->next;
    }
};


int test_add_two_numbers(void) {

    // 准备数据
    ListNode* left_node, * right_node;
    left_node = new ListNode(2);
    left_node->next = new ListNode(4);
    left_node->next->next = new ListNode(3);

    right_node = new ListNode(5);
    right_node->next = new ListNode(6);
    right_node->next->next = new ListNode(1);


    AddTwoNumbers adn{};
    ListNode* resp = adn.add_two_numbers(left_node, right_node);



    // 测试-1
    assert(resp->val == 7);
    assert(resp->next->val == 0);
    assert(resp->next->next->val == 5);

    return 0;
}
