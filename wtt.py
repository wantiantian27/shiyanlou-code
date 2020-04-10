print('*'*30)
print('欢迎进入游戏')
print('*'*30)
username=input('请输入你的用户名：')
money=0
answer=input('是否进入游戏：')
if answer=='yes':
    while money<2:
        n=int(input('金币不足，请充值（充值必须是10的倍数）：'))
        if n>0 and n%10==0:
            money=n
            print('充值成功，当前账户金币为{}'.format(money))
        print('开始游戏')
        import random
        while money>=2:
            a=random.randint(1,6)
            b=random.randint(1,6)
            m=input('是否开始游戏：')
            if m=='yes':
                money-=5
                guess=input('请输入你的猜想：')
                print(a+b)
                if((a+b)>=6 and guess=='大') or ((a+b)<=6 and guess=='小'):
                    money+=1
                    print('恭喜中奖，当前账户余额为{}'.format(money))
                else:
                    print('很遗憾！没有中奖，请再接再厉')
                    print('当前账户余额为{}'.format(money))
            else:
                break   
print('成功退出游戏')

        

    
        
    
