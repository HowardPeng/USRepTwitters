#include<fstream>
#include<iostream>
#include<dirent.h>
#include<vector>
#include<algorithm>
#include<streambuf>

using namespace std;

int count(string& str, string& str2find){
	const size_t step = str2find.size();

	int count(0);
	int pos(0) ;

	while( (pos=str.find(str2find, pos)) != std::string::npos) {
		pos += step;
		++count;
	}

	return count;
}

void printOut(string& str, string& keyword, string location){
	DIR *dir;
	struct dirent *ent;
	vector<pair<int, string> > result;
	if ((dir = opendir(str.c_str())) != NULL) {
		while ((ent = readdir (dir)) != NULL) {
			string filename = ent->d_name;
			if(filename == "." || filename == "..") continue;
			string fileFullDir = str + ent->d_name;
			ifstream infile(fileFullDir.c_str());

			if(infile.is_open()){
				std::string textInput((std::istreambuf_iterator<char>(infile)),
								 std::istreambuf_iterator<char>());
				int num = count(textInput, keyword);
				if(num > 0){
					result.push_back({num, filename.substr(0, filename.length()-13)});
				}
			}
			infile.close();
		}
		closedir (dir);
	} else {
		cout << "Error, cannot open directory " << str;
		return;
	}

	sort(result.begin(), result.end());


	cout << "	\"" + location + "\":[" << endl;

	for(int i = result.size()-1 ; i >= 0; --i){
		cout << "		{" << endl;
		cout << "			\"twitter_account\":\"" << result[i].second << "\"" << endl;
		cout << "			\"count\":\"" << result[i].first << "\"" << endl;
		cout << "		}," << endl;
	}
	cout << "	]" << endl;
}


int main(int argc, char* argv[]){
	if(argc != 3) return -1;
	string root = string(argv[1]);
	string keyword = string(argv[2]);
	string str = root + "/HouseTweets/";
	cout << "{" << endl;
	printOut(str, keyword, "House");

	cout << "," << endl;
	str = root + "/SenateTweets/";
	printOut(str, keyword, "Senate");
	cout << "}" << endl;
	return 1;
}
