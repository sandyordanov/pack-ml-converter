#include <string>
class Stage{
    public:
        std::string name;
        bool start;
        bool stop;

        Stage(std::string nodeName, bool isStart = false, bool isStop = false)
            : name(nodeName), start(isStart), stop(isStop) {}
};