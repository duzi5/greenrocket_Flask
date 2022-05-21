from bs4 import BeautifulSoup

with open('https://www.google.com/finance/?rlz=1C5CHFA_enBR995BR995&oq=a%C3%A7%C3%A3o+da+&aqs=chrome.1.69i57j0i131i433i512j0i512j0i433i512l2j69i60l3&pf=cs&sourceid=chrome&ie=UTF-8&sa=X&sqi=2&ved=2ahUKEwiyiYvlv-f3AhW-RWwGHcI_DLMQ6M8CegQIFxAI', 'r') as f:
    acao = BeautifulSoup(f, 'lxml')


lista = acao.find_all('span')
    

print(' IsqQVc NprOob wT3VGc')