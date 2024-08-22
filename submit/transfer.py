#include <iostream>
#include <queue>
using namespace std;

struct ticket
{
	long long money;
	long long sTime;
};

long long mcnt=0;

queue <ticket> tickets;
queue <ticket> temptickets;

void CheckTickets(int m,int t,int s)
{
	if (!tickets.empty())
	{
		while ((t-tickets.front().sTime>45))
		{
			tickets.pop();
			if (tickets.empty())
			{
				break;
			}
		}
		if (!tickets.empty())
		{
			if (tickets.front().money>=m)
			{
				tickets.pop();
			}else{
				ticket tempTicket=tickets.front();
				tickets.pop();
				temptickets.push(tempTicket);
				CheckTickets(m,t,1);
				if (s==0)
				{
					while (!tickets.empty())
					{
						tempTicket=tickets.front();
						tickets.pop();
						temptickets.push(tempTicket);
					}
					while (!temptickets.empty())
					{
						tempTicket=temptickets.front();
						temptickets.pop();
						tickets.push(tempTicket);
					}
				}
			}
		}else{
			mcnt+=m;
		}
	}else{
		mcnt+=m;
	}
}

int main()
{
	long long n,temp,m,t;
	ticket ttemp;
	cin >> n;
	for (int i=0;i<n;i++)
	{
		cin >> temp >> m >> t;
		if (temp==0)
		{
			ttemp.money=m;
			ttemp.sTime=t;
			tickets.push(ttemp);
			mcnt+=m;
		}else{
			CheckTickets(m,t,0);
		}
	}
	cout << mcnt;
	return 0;
}