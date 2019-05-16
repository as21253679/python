#include<iostream>
using namespace std;
#define max 510
#define adder 100

int arr[100] = { 0,100,200,300,400,500,-420,-320,-220,-120,-20,80,180,280,380,480,-440,-340,-240,-140,-40,60,160 };
int motor_value = 0;

void motor(bool dir)//right=true,left=false
{
	if (dir == true)
	{
		if (motor_value + adder > max)
		{
			motor_value = -max + (adder - (max - motor_value));
		}
		else
		{
			motor_value = motor_value + adder;
		}
	}
	else if (dir == false)
	{
		if (motor_value - adder < -max)
		{
			motor_value = max - (adder - (max + motor_value));
		}
		else
		{
			motor_value = motor_value - adder;
		}
	}
}

int main()
{
	char input;
	int count=0;
	int current = 0;
	int before = 0;

	while (1)
	{
		cin >> input;
		if (input == 'r')
		{
			before = motor_value;
			motor(true);
			current = motor_value;

			if (current < before)
			{
				count += (max - before) + (current + max);
			}
			else
			{
				count += current - before;
			}
		}
		else if (input == 'l')
		{
			before = motor_value;
			motor(false);
			current = motor_value;

			if (current > before)
			{
				count += (-max - before) + (current - max);
			}
			else
			{
				count += current - before;
			}
		}
		printf("%d\r\n", count);
	}

	system("pause");
	return 0;
}
