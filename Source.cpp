#include<iostream>
using namespace std;
struct node {
	int data;
	node* left, * right;
	node(int x) {
		data = x;
		left = NULL;
		right = NULL;
	}
};
struct ltnode {
	struct node** info;
	struct ltnode* next;
}*front ,*rear;


node* root;
node* insert(node* x,int data) {
	if (x == NULL)	return new node(data);
	if (x->data > data)	x->left = insert(x->left, data);
	else
	{
		x->right = insert(x->right, data);
	}
	return x;
}
void insert(int data) {
	root = insert(root, data);
}
void inorderr(node* x) {
	if (x == NULL)	return;
	inorderr(x->left);
	cout << x->data << ' ';
	inorderr(x->right);
}

void addq(node** x) {
	ltnode* temp = new ltnode;
	temp->info = x;
	temp->next = NULL;
	if (front == NULL) {
		front = rear = temp;
		cout << rear << ' ' << front << '\n';
		return;
	}
	rear->next = temp;
	rear = rear->next;
}
node** dequeue() {
	if (front == NULL) {
		return NULL;
	}
	node** temp = front->info;
	front = front->next;
	return temp;
}

void levelorderr(node ** root)
{
	addq(root);
	int tracker = 1;
	cout << "\nleven order \n";
	while (front != NULL) {

		for (int i = 0; i < tracker; ++i) {
			node** temp = dequeue();
			node* x = *temp;
			if (x != NULL) {
				cout << x->data<< ' ';
				addq(&(x->left));	cout << rear <<' '<<front<< '\n';	
				addq(&(x->right));	cout << rear << ' '<<front<< '\n';
			}
			else {
				addq(NULL); addq(NULL);
			}
		}
		cout << "level " <<  tracker << '\n';
		tracker *= 2;
	}
}


int main()
{
	int n;	cin >> n;
	for (int i = 0; i < n; ++i) {
		int k;	cin >> k;
		insert(k);
	}
	inorderr(root);

	levelorderr(&root);
	return 0;
}
