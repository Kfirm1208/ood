class TorKham:
    def __init__(self) -> None:
        self.wordlst = []
    def next(self,word):
        if self.wordlst == []:
            self.wordlst.append(word)
            print('\''+str(word)+'\' ->',self.wordlst)
        else:
            if self.wordlst[len(self.wordlst)-1][-1].casefold()==word[1].casefold() and self.wordlst[len(self.wordlst)-1][-2].casefold()==word[0].casefold():
                self.wordlst.append(word)
                print('\''+str(word)+'\' ->',self.wordlst)
            else:
                print('\''+str(word)+'\' -> game over')
    def restart(self):
        self.wordlst = []
        print("game restarted")
        
def main():       
    print("*** TorKham HanSaa ***")
    x = list(map(str,input("Enter Input : ").split(",")))
    TorKham = TorKham()

    for i in x:
        word = i.split()
        if word[0] == 'P':
            TorKham.next(word[1])
        elif word[0] == 'R':
            TorKham.restart()
        elif word[0] == 'X':
            exit()
        else:
            print('\''+' '.join(word)+'\' is Invalid Input !!!')
            break
    
if __name__ == '__main__':
    main()