std::vector<std::string> allLongestStrings(std::vector<std::string> inputArray) {
    using namespace std;
    std::map<int,std::vector<std::string>> m;
    int index = 0;
    for( const string &str: inputArray){
        auto iter = m.insert({str.length(), vector<string>()});
        iter.first->second.push_back(str);
       if ( str.length() > index) {
           index = str.length();
       }
    }
    
    return m.find(index)->second;
    
}
