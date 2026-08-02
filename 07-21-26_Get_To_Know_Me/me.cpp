#include <iostream>
#include <string>

using namespace std;

void showHeader();
void displayProfile(string fullName, string nickname, string birthday,
                    string address, string favSong);

int main()
{
	string fullName = "Nielmar Porras Tutesora";
	string nickname = "Pon";
	string birthday = "10/23/2003";
	string address = "Calumpang Molo Iloilo City";
	string favSong = "I Like You The Most";

	showHeader();
	displayProfile(fullName, nickname, birthday, address, favSong);

	return 0;
}

void showHeader()
{
	cout << "=====================================================\n";
	cout << "           🌟 MY PROFILE PROGRAM 🌟\n";
	cout << "=====================================================\n\n";
}

void displayProfile(string fullName, string nickname, string birthday,
                    string address, string favSong)
{
	cout << "Fullname    : " << fullName << endl;
	cout << "Nickname    : " << nickname << endl;
	cout << "Birthday    : " << birthday << endl;
	cout << "Address     : " << address << endl;
	cout << "Fav Song    : " << favSong << endl;
}