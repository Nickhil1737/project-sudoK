#include <iostream>
using namespace std;
int trackarr[10][30], T = 0,hsh[30];
void makeknutharray(int i, int j, int val)
{
	trackarr[T][10 + 3*(i-1)+val] = hsh[10 + 3 * (i - 1) + val] = 1;
	trackarr[T][20 + 3*(j-1)+val] = hsh[20 + 3 * (j - 1) + val] = 1;
	trackarr[T][3 * (i - 1) + j] = val;
	hsh[3 * (i - 1) + j] = val;
	T++;
}
void printknutharray()
{
	for (int i = 0; i < T; ++i) {
		for (int j = 1; j < 10; ++j) {
			cout << trackarr[i][j] << ' ';
		}
		cout << '\t';
		for (int j = 11; j < 20; ++j) {
			cout << trackarr[i][j] << ' ';
		}
		cout << '\t';
		for (int j = 21; j < 30; ++j) {
			cout << trackarr[i][j] << ' ';
		}
		cout << '\n';
	}
	for (int i = 0; i < 30; ++i)	cout << hsh[i] << ' ';
	cout << '\n';

}
void solvesudok()
{
	
	for (int i = 1; i < 10; ++i) {
		if (!hsh[i]) {
			int row, column;
			row = (i - 1) / 3 + 1;
			column = i - (row - 1) * 3;
			if (!hsh[10 + (row - 1) * 3 + 1] && !hsh[20 + 3*(column - 1) + 1]) makeknutharray(row, column, 1);
			
			else if (!hsh[10 + (row - 1) * 3 + 2] && !hsh[20 + 3*(column - 1) + 2])	makeknutharray(row, column, 2);
			else if (!hsh[10 + (row - 1) * 3 + 3] && !hsh[20 + 3 * (column - 1) + 3])makeknutharray(row, column, 3);
		}
	}
}
bool checkvalue(int row, int column, int val)
{
	if (hsh[(row - 1) * 3 + column])	return 0;
	if (hsh[10 + (row - 1) * 3 + val])	return 0;
	if (hsh[20 + (column - 1) * 3 + val])	return 0;
	return 1;
}
void playsudok()
{
	int temphsh[10],countunFilled = 0,row,column,val,invcount = 0;
	for (int i = 1; i < 10; ++i) {
		if (!hsh[i])	countunFilled++;
		temphsh[i] = hsh[i];

	}
	while (countunFilled) {
		cout << "row? ";	cin >> row;
		cout << "column? ";		cin >> column;
		cout << "val? ";	cin >> val;
		if (row + column + val < 3 || row + column + val > 9)	break;
		if (checkvalue(row, column, val)) {
			makeknutharray(row, column, val);
			countunFilled--;
		}
		else cout << "some invalid move/s " << ++invcount << '\n';

		if (invcount > 3) {
			cout << "exceeded invalid moves \n"; break;
		}
		int k = 1;
		for (int i = 0; i < 3; ++i) {
			for (int j = 0; j < 3; ++j)	cout << hsh[k++] << ' ';
			cout << '\n';
		}
	}
	if (!countunFilled)	cout << "\t\tSUCCESS!!!\n\n";
	else cout << "Try again\n";
}
int main()
{
	int n, arr[5][5];
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			cin >> arr[i][j];
			if (arr[i][j]) {
				makeknutharray(i, j, arr[i][j]);
			}
		}
	}
	int k = 1;
	printknutharray();
	playsudok();
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 3; ++j)	cout << hsh[k++] << ' ';
		cout << '\n';
	}
	return 0;
}