class ACapLock():
    def process(self,input):
        pressed = False
        result =  []
        for i in input:
            if i == 'a' or i == 'A':
                pressed = not pressed
                continue
            else:
                if pressed:
                    result.append(i.upper())
                else:
                    result.append(i)
        return ''.join(str(x) for x in result)

a= ACapLock()
print(a.process("My keyboard is broken!"))
