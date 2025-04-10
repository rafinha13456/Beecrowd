num = int(input())

def relogio(num):
    if num < 60:
        print(f"0:0:{num}")
    elif num > 60 and num < 3600:
        m = num//60
        s = num%60
        print(f"0:{m}:{s}")
    else:
        h = num//3600
        m = (num%3600)//60
        s = num%60
        print(f"{h}:{m}:{s}")

relogio(num)