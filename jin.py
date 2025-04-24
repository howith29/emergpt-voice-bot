import re
import pytz
from datetime import datetime

def emergency(message):
    # 추가 하고 싶으면 if문 뒤에 "or '엑' in message"작성해서 추가
    if '악' in message or '윽' in message or message=='' or '엑' in message :
        emer='긴급'
    else:
        emer=''
    korea_timezone = pytz.timezone('Asia/Seoul') 
    current_time = datetime.now(korea_timezone)
    report = current_time.strftime('%Y-%m-%d %H:%M:%S') # 원하는 포맷으로 시간 포맷팅
    return emer, report

def jin_time(message,report_time):
    print(message, report_time)
    word=''
    if '지금' in message: 
        current_time = report_time.split(' ')[1].split(':')
        hour, minute = current_time[0],current_time[1]
    else:
        korean_to_digits = {
        '한': '1', '두': '2', '세': '3', '네': '4', '다섯': '5','여섯': '6', '일곱': '7', '여덟': '8', '아홉': '9', '열': '10',
        '일':'1', '이':'2', '삼':'3', '사':'4', '오':'5', '육':'6', '칠':'7', '팔':'8', '구':'9', 
        '십': '10', '이십': '20', '삼십': '30', '사십': '40', '오십': '50', '육십':'60'}
        if '시간' in message:
            hour, minute=message.split('시간')[0],message.split('시간')[1]
            if '반' in minute:
                minute,word=30,minute.split('반')[1]
            elif '분' in minute:
                minute,word=minute.split('분')[0].replace(' ',''),minute.split('분')[1]
            else:
                word=minute
                minute=0 
        elif '시' in message:
            hour, minute=message.split('시')[0],message.split('시')[1]
            if '반' in minute:
                minute,word=30,minute.split('반')[1]
            elif '분' in minute:
                minute,word=minute.split('분')[0].replace(' ',''),minute.split('분')[1]
            else:
                word=minute
                minute=0 
        else:
            hour='0'
            if '분' in message:
                minute,word=message.split('분')[0].replace(' ',''),message.split('분')[1]
                
        if hour:
            pattern1=r'(아침|저녁|오전|오후|밤|새벽|낮)?\s*(\S+)\s*'
            match1= re.findall(pattern1, hour)
            hour=match1[0][1]
            #시간 처리
            if hour.isdigit()==False:
                if '십' in hour:
                    a,b=hour.split('십')[0][-1], hour.split('십')[1:]
                    hour = int(korean_to_digits.get(a, '1'))*10+int(korean_to_digits.get(''.join(b), '00'))
                elif '열' in hour:
                    a,b=hour.split('열')[0], hour.split('열')[1:]
                    hour = int(korean_to_digits.get(a, '1'))*10+int(korean_to_digits.get(''.join(b), '00'))
                else:
                    hour = int(korean_to_digits.get(hour, '1'))
            if '오후' in match1[0][0] or '저녁' in match1[0][0] or '밤' in match1[0][0]:
                hour=int(hour)+12
            
        #분 처리
        if minute and minute.isdigit()==False:
            if '십' in minute:
                a, *b = minute.split('십')
                a = a[-1] if a else ''
                minute = int(korean_to_digits.get(a, '1'))*10+int(korean_to_digits.get(''.join(b), '00'))
            elif '열' in minute:
                a,b=minute.split('열')[0], minute.split('열')[1:]
                minute = int(korean_to_digits.get(a, '1'))*10+int(korean_to_digits.get(''.join(b), '00'))
            else:
                minute = korean_to_digits.get(minute[-1], '00')
                
        #전, 후 처리
        if '전' in word or '후' in word:
            word = '전' if '전' in word else '후'
        else:
            word=''
            
    hour = int(hour)
    minute = int(minute) if minute else 0  # 분이 없을 경우, 0으로 설정
    return hour, minute, word
    
    