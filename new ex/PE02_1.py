import xml.etree.ElementTree as elemTree
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

tree = elemTree.parse('C:/Users/jim26/OneDrive/바탕 화면/공학프로그래밍/공학프로그래밍2/HY202103_D07_(0,0)_LION1_DCM_LMZC.xml')
root = tree.getroot()
print('<IV-analysis>')
for i in root.iter():       #iter()함수, 반복을 끝낼 값을 지정하면 특정 값이 나올 때까지 반복
    if i.tag == 'Voltage':  #반복 태그가 'Voltage'일 경우
        voltage_list = list(map(float, i.text.split(','))) # voltage data list 변환
        print(f'Voltage = {voltage_list}') # voltage list 출력
    elif i.tag == 'Current': #반복 태그가 'Current'일 경우
        current_list = list(map(float, i.text.split(','))) # voltage data list 변환
        print(f'Current = {current_list}') # voltage list 출력

voltage = np.array(voltage_list)
current = np.abs(current_list)
#from sklearn.metrics import r2_score
#R2 = r2_score(voltage,current)
#print(f'R2score = {R2}')
plot.scatter(voltage,current ,c='k', alpha=1.0)                    # 점 color = black, 투명도 = 1(투명하지 않음)
plot.title('IV-analysis', fontsize =16)                              # 그래프 제목 설정, font 크기 설정
plot.xlabel("Voltage[V]", fontsize=12, labelpad=5, loc='right')     # X축 제목, font 크기, 그래프와 거리, 위치 설정
plot.xticks(fontsize=10)                                            # X축 숫자 크기 설정
plot.ylabel("Current[A]", fontsize=12, labelpad=5, loc='top')       # Y축 제목, font 크기, 그래프와 거리, 위치 설정
plot.yticks(fontsize=10)                                            # Y축 숫자 크기 설정
plot.yscale('logit')                                                # Y축 log scale 설정
plot.grid(True)                                                     # 가독성을 위해 grid 삽입
plot.tight_layout()                                                 # layout 맞춤 설정
plot.savefig('IV-analysis.png')     # 저장
plot.show()

for i in range(1,7):
    a = tree.find('.ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/L'.format(i)).text #각각의 WavelengthSweep에서 Wavelength 추츨
    b = tree.find('.ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/IL'.format(i)).text #각각의 WavelengthSweep에서 Transmission 추출
    a1 = np.array(list(map(float,a.split(','))))
    b1 = np.array(list(map(float,b.split(','))))
    plot.plot(a1,b1) # Wavelength와 transmission에 대하여 그래프 그리기
    plot.xlabel("Wavelength [nm]") #x축 제목
    plot.ylabel("Transmission") #y축 제목
aa= tree.find('.ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L').text # DBias = 0일때의 Wavelength 추출
bb= tree.find('.ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL').text # DBias = 0일때의 Transmission 추출
aa1 = np.array(list(map(float,aa.split(','))))
bb1 = np.array(list(map(float,bb.split(','))))
plot.plot(aa1,bb1) # 그래프 그리기
plot.show()