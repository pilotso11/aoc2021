#include <iostream>
#include <string>
using namespace std;
string R="RIGHT",L="LEFT",W="WAIT",B="BLOCK",D,m;

int main()
{
    int N,w,X,x,U,M,C,c,E,e,i;
    cin>>N>>w>>U>>X>>x>>U>>U>>M;
    cin.ignore();

    int V[N];

    for(i=0;i<M;i++)
    {
        cin>>E>>e;
        cin.ignore();
        V[E]=e;
    }

    while(1)
    {
        m=W;
        cin>>C>>c>>D;
        cin.ignore();

        if(C==X) 
        {
            if(D==R&&c>x||D==L&&c<x)
                m=B;
        }
        else if(C!=-1&&(D==R&&c>V[C]||D==L&&c<V[C]))
            m=B;

        if(m==W&&(D==R&&c==w-1||D==L&&c==0))
                m=B;

        cout<<m<<endl;
    }
}
