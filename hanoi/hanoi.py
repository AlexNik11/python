def move(height,axel1, axel3, axel2):
    if height >= 1:
        move(height-1,axel1,axel2,axel3)
        print("Перемещаем диск с",axel1,"на",axel3)
        move(height-1,axel2,axel3,axel1)

def main():
    move(3,"1","2","3")

if __name__ == '__main__':
   main()