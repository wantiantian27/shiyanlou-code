print('*'*30)
print ('欢迎进入游戏')
print ('*'*30)
import random 
username=input('请输入你的用户民：')
money=0
answer=input ('确定进入游戏吗？（y/n）:')
if answer=='y':
    while money<2:
        n=int(input('金币不足，请充值（100块钱30个币，充值必须是100的倍数）：'))
        if n%100==0 and n>0:
            money=(n//100)*30
    print('当前剩余游戏币是：{}，玩一局游戏扣除2个币'.format(money))
    print('进入游戏中......')
while true:
    t1=random.randint(1,6)
    t2=random.randint(1,6)
    print ('系统洗牌完毕，请输入大小：')
    guess=input('输入大或者小：')
    if((t1+t2)>6 and guess=='大') or ((t1+t2)<=6 and guess=='小'):
        print ('恭喜{}！本局游戏奖励获得一个游戏币！')
