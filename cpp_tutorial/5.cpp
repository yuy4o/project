# include <iostream>

using namespace std;

const int ArSize = 8;

int sum_arr(int arr[], int n);

int main(void)
{
	int cookies[ArSize] = {1,2,4, 8,16,32,64,128};
	int sum = sum_arr(cookies, ArSize);
	cout << "Total cookies eaten: "<< sum << endl;
	return 0;
}

int sum_arr(int arr[], int n)
{
	int total = 0;
	for (int i = 0; i <  n; i++)
		total += arr[i];
	return total;
}
