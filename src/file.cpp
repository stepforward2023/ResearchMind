#include<iostream>
using namespace std;
bool fun_palindrome(string word){

    

    int num=word.length()-1;

    for(int i=0; i<=num/2 ;i++){
         if (word[i] != word[num-i]){
             return false;

         }
           

    } 
       

    return true;

}

int main(){

    string word;
    cin>>word;
    bool is_palindrome=fun_palindrome(word);
    cout<<is_palindrome;
    return 0;

}

 


