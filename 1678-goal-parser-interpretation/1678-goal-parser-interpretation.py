class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res=[]
        for i in range(len(command)):
            if command[i]=="G":
                res.append("G")
            elif command[i]=="(":
                if command[i+1]==")":
                    res.append("o")
                elif command[i+1]=="a":
                    res.append("al")
        return "".join(res)