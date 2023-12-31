#!!!!!!Добавить в корень файл txts !!!!!!!!!!!!

import shutil
import zipfile

def extract_passwords(zip_files):
    for zip_file in zip_files:
        # Копирование zip файла в папку txts
        shutil.copy2(zip_file, 'txts/')

        # Замена расширения на .txt
        new_file = 'txts/' + zip_file.split('.')[0] + '.txt'
        shutil.move('txts/' + zip_file, new_file)

        # Чтение последних 17 символов и открытие zip файла с паролем
        password = open(new_file, 'rb').read()[-17:].decode('utf-8')
        with zipfile.ZipFile(zip_file, 'r') as zf:
            try:
                zf.extractall(pwd=password.encode()[1::])
                print(f"Пароль для файла {zip_file}: {password}")
            except Exception as e:
                print(f"Ошибка при раскрытии файла {zip_file}: {e}")

# Пример использования
zip_files = ["flag290.zip","flag289.zip","flag288.zip","flag287.zip","flag286.zip","flag285.zip","flag284.zip","flag283.zip","flag282.zip","flag281.zip","flag280.zip","flag279.zip","flag278.zip","flag277.zip","flag276.zip","flag275.zip","flag274.zip","flag273.zip","flag272.zip","flag271.zip","flag270.zip","flag269.zip","flag268.zip","flag267.zip","flag266.zip","flag265.zip","flag264.zip","flag263.zip","flag262.zip","flag261.zip","flag260.zip","flag259.zip","flag258.zip","flag257.zip","flag256.zip","flag255.zip","flag254.zip","flag253.zip","flag252.zip","flag251.zip","flag250.zip","flag249.zip","flag248.zip","flag247.zip","flag246.zip","flag245.zip","flag244.zip","flag243.zip","flag242.zip","flag241.zip","flag240.zip","flag239.zip","flag238.zip","flag237.zip","flag236.zip","flag235.zip","flag234.zip","flag233.zip","flag232.zip","flag231.zip","flag230.zip","flag229.zip","flag228.zip","flag227.zip","flag226.zip","flag225.zip","flag224.zip","flag223.zip","flag222.zip","flag221.zip","flag220.zip","flag219.zip","flag218.zip","flag217.zip","flag216.zip","flag215.zip","flag214.zip","flag213.zip","flag212.zip","flag211.zip","flag210.zip","flag209.zip","flag208.zip","flag207.zip","flag206.zip","flag205.zip","flag204.zip","flag203.zip","flag202.zip","flag201.zip","flag200.zip","flag199.zip","flag198.zip","flag197.zip","flag196.zip","flag195.zip","flag194.zip","flag193.zip","flag192.zip","flag191.zip","flag190.zip","flag189.zip","flag188.zip","flag187.zip","flag186.zip","flag185.zip","flag184.zip","flag183.zip","flag182.zip","flag181.zip","flag180.zip","flag179.zip","flag178.zip","flag177.zip","flag176.zip","flag175.zip","flag174.zip","flag173.zip","flag172.zip","flag171.zip","flag170.zip","flag169.zip","flag168.zip","flag167.zip","flag166.zip","flag165.zip","flag164.zip","flag163.zip","flag162.zip","flag161.zip","flag160.zip","flag159.zip","flag158.zip","flag157.zip","flag156.zip","flag155.zip","flag154.zip","flag153.zip","flag152.zip","flag151.zip","flag150.zip","flag149.zip","flag148.zip","flag147.zip","flag146.zip","flag145.zip","flag144.zip","flag143.zip","flag142.zip","flag141.zip","flag140.zip","flag139.zip","flag138.zip","flag137.zip","flag136.zip","flag135.zip","flag134.zip","flag133.zip","flag132.zip","flag131.zip","flag130.zip","flag129.zip","flag128.zip","flag127.zip","flag126.zip","flag125.zip","flag124.zip","flag123.zip","flag122.zip","flag121.zip","flag120.zip","flag119.zip","flag118.zip","flag117.zip","flag116.zip","flag115.zip","flag114.zip","flag113.zip","flag112.zip","flag111.zip","flag110.zip","flag109.zip","flag108.zip","flag107.zip","flag106.zip","flag105.zip","flag104.zip","flag103.zip","flag102.zip","flag101.zip","flag100.zip","flag99.zip","flag98.zip","flag97.zip","flag96.zip","flag95.zip","flag94.zip","flag93.zip","flag92.zip","flag91.zip","flag90.zip","flag89.zip","flag88.zip","flag87.zip","flag86.zip","flag85.zip","flag84.zip","flag83.zip","flag82.zip","flag81.zip","flag80.zip","flag79.zip","flag78.zip","flag77.zip","flag76.zip","flag75.zip","flag74.zip","flag73.zip","flag72.zip","flag71.zip","flag70.zip","flag69.zip","flag68.zip","flag67.zip","flag66.zip","flag65.zip","flag64.zip","flag63.zip","flag62.zip","flag61.zip","flag60.zip","flag59.zip","flag58.zip","flag57.zip","flag56.zip","flag55.zip","flag54.zip","flag53.zip","flag52.zip","flag51.zip","flag50.zip","flag49.zip","flag48.zip","flag47.zip","flag46.zip","flag45.zip","flag44.zip","flag43.zip","flag42.zip","flag41.zip","flag40.zip","flag39.zip","flag38.zip","flag37.zip","flag36.zip","flag35.zip","flag34.zip","flag33.zip","flag32.zip","flag31.zip","flag30.zip","flag29.zip","flag28.zip","flag27.zip","flag26.zip","flag25.zip","flag24.zip","flag23.zip","flag22.zip","flag21.zip","flag20.zip","flag19.zip","flag18.zip","flag17.zip","flag16.zip","flag15.zip","flag14.zip","flag13.zip","flag12.zip","flag11.zip","flag10.zip","flag9.zip","flag8.zip","flag7.zip","flag6.zip","flag5.zip","flag4.zip","flag3.zip","flag2.zip","flag1.zip","flag0.zip"] # Замените на список ваших zip-файлов
extract_passwords(zip_files)
