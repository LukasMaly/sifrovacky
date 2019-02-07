sifry = [['2:20,20:38,12:44,8:73,9:74,1:76,11:77,17:78/20', '4:58,5:69,2:75/7'],
         ['7:2,4:29,3:49,1:64/7', '1:9,4:13,3:31,6:43/6'],
         ['7:3,3:30,10:52,6:60,9:65/10', '2:17,6:40,3:48,8:62/8'],
         ['/0', '4:10,2:23,3:28,7:37,1:46,3:54/7'],
         ['1:25,3:33,7:56,6:53/14', '3:5,5:19,1:34/5'],
         ['4:14,3:18/7', '2:8,1:22,8:41,7:47,9:57/9'],
         ['5:6,1:7,7:11,2:67,4:71/7', '5:36,1:51/5'],
         ['3:16,2:72/5', '6:4,9:21,9:24,3:45,7:50,4:55,8:70/9'],
         ['3:15,6:26,1:39,2:66/8', '6:32,3:35,8:59/8'],
         ['1:12,2:27,12:42,11:63/12', '1:1,9:61,3:68/11']]

mista = [['SPOJENESTATYAMERICKE', 'NEWYORK'],
         ['NEMECKO', 'BERLIN'],
         ['ANTARKTIDA', 'JIZNIPOL'],
         ['', 'VATIKAN'],
         ['CESKOSLOVENSKO', 'PRAHA'],
         ['NEMECKO', 'NORIMBERK'],
         ['FRANCIE', 'PARIZ'],
         ['MESIC', 'MOREKLIDU'],
         ['JAPONSKO', 'IVODZIMA'],
         ['SEVERNIKOREA', 'PCHJONGJANG']]

heslo = 100 * [' ']

for sifra, misto in zip(sifry, mista):
    sifra_stat = sifra[0]
    sifra_mesto = sifra[1]

    misto_stat = misto[0]
    misto_mesto = misto[1]

    stat_len = int(sifra_stat.split('/')[1])
    mesto_len = int(sifra_mesto.split('/')[1])
    assert len(misto_stat) == stat_len
    assert len(misto_mesto) == mesto_len

    sifra_stat = sifra_stat.split('/')[0]
    sifra_mesto = sifra_mesto.split('/')[0]

    if len(sifra_stat.split(',')) > 1:
        for pozice in sifra_stat.split(','):
            v_nazvu = int(pozice.split(':')[0]) - 1
            v_heslu = int(pozice.split(':')[1]) - 1
            heslo[v_heslu] = misto_stat[v_nazvu]

    if len(sifra_mesto.split(',')) > 1:
        for pozice in sifra_mesto.split(','):
            v_nazvu = int(pozice.split(':')[0]) - 1
            v_heslu = int(pozice.split(':')[1]) - 1
            heslo[v_heslu] = misto_mesto[v_nazvu]

heslo = ''.join(heslo)
print(heslo)
