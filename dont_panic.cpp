#include<iostream>
#include<string>
using namespace std;string R="RIGHT",B="BLOCK",D,m;int main(){int n,w,X,x,M,C,c;cin>>n>>w>>C>>X>>x>>C>>C>>M;cin.ignore();int V[n];for(;M-->0;){cin>>C>>V[C];cin.ignore();}while(1){m="WAIT";cin>>C>>c>>D;cin.ignore();if(C==X){if(D==R&&c>x||D!=R&&c<x)m=B;}else if(C>-1&&(D==R&&c>V[C]||D!=R&&c<V[C]))m=B;cout<<m<<endl;}}