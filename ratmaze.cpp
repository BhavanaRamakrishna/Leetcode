#include <bits/stdc++.h>
using namespace std;

#define N 4
#define M 4

// QItem for current location and distance
// from source location
class QItem {
public:
	int row;
	int col;
	int dist;
	QItem(int x, int y, int w)
		: row(x), col(y), dist(w)
	{
	}
};

int minDistance(int grid[N][M], int si, int sj, int di, int dj)
{
	QItem source(0, 0, 0);
	int tempgrid[N][M];
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			tempgrid[i][j] = grid[i][j];
		}
	}
	tempgrid[si][sj] = 5;
	tempgrid[di][dj] = 10;
	// To keep track of visited QItems. Marking
	// blocked cells as visited.
	bool visited[N][M];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
		{
			if (tempgrid[i][j] == 1)
				visited[i][j] = true;
			else
				visited[i][j] = false;

			// Finding source
			if (tempgrid[i][j] == 5)
			{
			   source.row = i;
			   source.col = j;
			}
		}
	}

	// applying BFS on matrix cells starting from source
	queue<QItem> q;
	q.push(source);
	visited[source.row][source.col] = true;
	while (!q.empty()) {
		QItem p = q.front();
		q.pop();

		// Destination found;
		if (tempgrid[p.row][p.col] == 10)
			return p.dist;

		// moving up
		if (p.row - 1 >= 0 &&
			visited[p.row - 1][p.col] == false) {
			q.push(QItem(p.row - 1, p.col, p.dist + 1));
			visited[p.row - 1][p.col] = true;
		}

		// moving down
		if (p.row + 1 < N &&
			visited[p.row + 1][p.col] == false) {
			q.push(QItem(p.row + 1, p.col, p.dist + 1));
			visited[p.row + 1][p.col] = true;
		}

		// moving left
		if (p.col - 1 >= 0 &&
			visited[p.row][p.col - 1] == false) {
			q.push(QItem(p.row, p.col - 1, p.dist + 1));
			visited[p.row][p.col - 1] = true;
		}

		 // moving right
		if (p.col + 1 < M &&
			visited[p.row][p.col + 1] == false) {
			q.push(QItem(p.row, p.col + 1, p.dist + 1));
			visited[p.row][p.col + 1] = true;
		}
	}
	return -1;
}

// Driver code
int main()
{
	int grid[N][M] = { { 0, 1, 2, 0 },
						{ 0, 2, 0, 0 },
						{ 2, 0, 1, 2 },
						{ 0, 0, 0, 0 } };

	int si, sj, mini, minj, min=999;
	int flag = 0, totalmin = 0;

	//get cheese location
	list< std::pair<int,char> > cheese;
	while(flag < 4){
		min = 999;
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if(grid[i][j] == 2){
				cheese.emplace_front(i,j);
			}
		}
	}
	if(cheese.size()==0)
		break;
	for(auto& x:cheese){
		int dis = minDistance(grid, si, sj, x.first, x.second);
		if(dis<min){
			min = dis;
			mini = x.first;
			minj = x.second;
		}
	}
	cout<<min;
	cout<<mini;
	cout<<minj;
	cout<<endl;
	grid[mini][minj] = 0;
	si = mini;
	sj = minj;
	totalmin += min;
	cheese.clear();
	flag++;
	}
	totalmin += minDistance(grid, si, sj, 3, 3);
	cout<<totalmin;
	return 0;
}
