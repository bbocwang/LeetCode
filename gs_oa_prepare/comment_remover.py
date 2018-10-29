class commentRemover():
    def remove(self,c):
        in_comment=False
        in_line_comment=False
        if c == None: return None
        s = c
        result=[]
        buffer=[]
        for idx,i in enumerate(s):
            if not in_comment and not in_line_comment:
                if i == '/' and idx + 1 < len(s):
                     if s[idx+1] == '/':
                         in_line_comment=True
                         continue
                     elif s[idx+1] == '*':
                         buffer.append(i)
                         in_comment=True
                elif idx==len(s)-1:
                    buffer.append(i)
                    result.append(''.join(str(x) for x in buffer))
                else:
                    result.append(i)
            elif in_line_comment:
                if i == '\n':
                    result.append("\n")
                    in_line_comment = False
                else:
                    continue

            else:
                if i == '*' and idx+1<len(s) and s[idx+1] == '/':
                    buffer=[]
                    in_comment=False
                elif idx==len(s)-1:
                    buffer.append(i)
                    result.append(''.join(str(x) for x in buffer))
                else:
                    buffer.append(i)
        return ''.join(str(x) for x in result)






a=commentRemover()

print(a.remove("/*Test program */int main(){ // variable declaration \n int a, b, c;/* This is a test multiline comment for testing a = b + c;}"))
