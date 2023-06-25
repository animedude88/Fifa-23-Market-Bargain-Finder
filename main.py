from bs4 import BeautifulSoup
import requests
from replit import db
from website import keep_alive

icons = [
 '/en/fifa23/player/robert-lewandowski/17315', '/en/fifa23/player/kevin-de-bruyne/17264', '/en/fifa23/player/franco-baresi/1136', '/en/fifa23/player/karim-benzema/54', '/en/fifa23/player/marco-van-basten/1129', '/en/fifa23/player/bobby-moore/19082', '/en/fifa23/player/robert-lewandowski/53', '/en/fifa23/player/kevin-de-bruyne/52', '/en/fifa23/player/roberto-baggio/1137', '/en/fifa23/player/lionel-messi/51', '/en/fifa23/player/sadio-mane/17576', '/en/fifa23/player/xavi/1141', '/en/fifa23/player/virgil-van-dijk/22', '/en/fifa23/player/cristiano-ronaldo/49', '/en/fifa23/player/luka-modric/19067', '/en/fifa23/player/dennis-bergkamp/1144', '/en/fifa23/player/puyol/1153', '/en/fifa23/player/jean-pierre-papin/4', '/en/fifa23/player/jurgen-kohler/19027', '/en/fifa23/player/petr-cech/19096', '/en/fifa23/player/ruud-van-nistelrooy/1154', '/en/fifa23/player/andrea-pirlo/1151', '/en/fifa23/player/alessandro-nesta/1152', '/en/fifa23/player/mohamed-salah/50', '/en/fifa23/player/peter-schmeichel/1157', '/en/fifa23/player/petr-cech/19096', '/en/fifa23/player/jean-pierre-papin/4', '/en/fifa23/player/cristiano-ronaldo/49', '/en/fifa23/player/luka-modric/19067', '/en/fifa23/player/bobby-moore/1175', '/en/fifa23/player/lev-yashin/1163', '/en/fifa23/player/roberto-baggio/1161', '/en/fifa23/player/laurent-blanc/1169', '/en/fifa23/player/didier-drogba/1180', '/en/fifa23/player/fernando-hierro/1164', '/en/fifa23/player/sergej-milinkovic-savic/19029', '/en/fifa23/player/michael-ballack/1178', '/en/fifa23/player/paul-scholes/1172', '/en/fifa23/player/miroslav-klose/1179', '/en/fifa23/player/gheorghe-hagi/1171', '/en/fifa23/player/gary-lineker/1170', '/en/fifa23/player/alan-shearer/1160', '/en/fifa23/player/michael-laudrup/1166', '/en/fifa23/player/steven-gerrard/1162', '/en/fifa23/player/rafael-marquez/8', '/en/fifa23/player/ricardo-carvalho/10', '/en/fifa23/player/socrates/1167', '/en/fifa23/player/hugo-sanchez/1177', '/en/fifa23/player/pique/17453', '/en/fifa23/player/thiago/17505', '/en/fifa23/player/gianluigi-donnarumma/17418', '/en/fifa23/player/bastian-schweinsteiger/1190', '/en/fifa23/player/ian-rush/1182', '/en/fifa23/player/casillas/1112', '/en/fifa23/player/xabi-alonso/164', '/en/fifa23/player/alan-shearer/1160', '/en/fifa23/player/phil-foden/17394', '/en/fifa23/player/erling-haaland/17361', '/en/fifa23/player/rafael-marquez/8', '/en/fifa23/player/luka-modric/17290', '/en/fifa23/player/abedi-pele/15487', '/en/fifa23/player/david-trezeguet/1189', '/en/fifa23/player/fabio-cannavaro/1181', '/en/fifa23/player/paul-scholes/1172', '/en/fifa23/player/pavel-nedved/1173', '/en/fifa23/player/bobby-moore/1175', '/en/fifa23/player/gary-lineker/1170', '/en/fifa23/player/hernan-crespo/19090', '/en/fifa23/player/javier-mascherano/7', '/en/fifa23/player/kaka/1185', '/en/fifa23/player/marco-van-basten/1184', '/en/fifa23/player/didier-drogba/1180', '/en/fifa23/player/ricardo-carvalho/10', '/en/fifa23/player/marcelo-brozovic/19033', '/en/fifa23/player/rafael-marquez/15514', '/en/fifa23/player/christian-vieri/1205', '/en/fifa23/player/andriy-shevchenko/1203', '/en/fifa23/player/paulo-dybala/17319', '/en/fifa23/player/martin-odegaard/17400', '/en/fifa23/player/roy-keane/1208', '/en/fifa23/player/robert-pires/1218', '/en/fifa23/player/juan-sebastian-veron/1206', '/en/fifa23/player/raul/1204', '/en/fifa23/player/javier-mascherano/15505', '/en/fifa23/player/rafael-marquez/15514', '/en/fifa23/player/diego-forlan/15508', '/en/fifa23/player/fernando-torres/1209', '/en/fifa23/player/sergio-busquets/19102', '/en/fifa23/player/reece-james/17556', '/en/fifa23/player/franco-baresi/1198', '/en/fifa23/player/patrick-kluivert/1199', '/en/fifa23/player/emmanuel-petit/1196', '/en/fifa23/player/andrea-pirlo/1193', '/en/fifa23/player/alessandro-nesta/1197', '/en/fifa23/player/nemanja-vidic/1216', '/en/fifa23/player/luis-figo/1210', '/en/fifa23/player/petr-cech/1211', '/en/fifa23/player/freddie-ljungberg/18990', '/en/fifa23/player/georginio-wijnaldum/19070', '/en/fifa23/player/theo-hernandez/17557', '/en/fifa23/player/alessandro-nesta/1197', '/en/fifa23/player/patrick-kluivert/1199', '/en/fifa23/player/frank-lampard/1192', '/en/fifa23/player/andrea-pirlo/1193', '/en/fifa23/player/andriy-shevchenko/1203', '/en/fifa23/player/theo-hernandez/17557', '/en/fifa23/player/reece-james/17556', '/en/fifa23/player/sergio-busquets/19102', '/en/fifa23/player/georginio-wijnaldum/19070', '/en/fifa23/player/javier-mascherano/15505', '/en/fifa23/player/jay-jay-okocha/15503', '/en/fifa23/player/hidetoshi-nakata/14', '/en/fifa23/player/landon-donovan/13', '/en/fifa23/player/dirk-kuyt/12', '/en/fifa23/player/marcelo-brozovic/19033', '/en/fifa23/player/hidetoshi-nakata/15523', '/en/fifa23/player/harry-kewell/15522', '/en/fifa23/player/miroslav-klose/1230', '/en/fifa23/player/benjamin-white/19071', '/en/fifa23/player/luis-hernandez/1229', '/en/fifa23/player/davor-suker/1228', '/en/fifa23/player/gary-lineker/1226', '/en/fifa23/player/christian-pulisic/19035', '/en/fifa23/player/edwin-van-der-sar/1225', '/en/fifa23/player/hernan-crespo/1224', '/en/fifa23/player/jack-grealish/17756', '/en/fifa23/player/serge-gnabry/17743', '/en/fifa23/player/rivaldo/1262', '/en/fifa23/player/ashley-cole/1261', '/en/fifa23/player/juan-roman-riquelme/1260', '/en/fifa23/player/david-beckham/1259', '/en/fifa23/player/gianfranco-zola/1258', '/en/fifa23/player/carlos-alberto-torres/1257', '/en/fifa23/player/michael-essien/1256', '/en/fifa23/player/javier-zanetti/1255', '/en/fifa23/player/hristo-stoichkov/1254', '/en/fifa23/player/bobby-moore/1253', '/en/fifa23/player/didier-drogba/1251', '/en/fifa23/player/claude-makelele/1250', '/en/fifa23/player/ian-wright/1248', '/en/fifa23/player/socrates/1247', '/en/fifa23/player/john-barnes/1246', '/en/fifa23/player/dennis-bergkamp/1244', '/en/fifa23/player/hugo-sanchez/1243', '/en/fifa23/player/gennaro-gattuso/1242', '/en/fifa23/player/bastian-schweinsteiger/1240', '/en/fifa23/player/hirving-lozano/19049', '/en/fifa23/player/henrik-larsson/1239', '/en/fifa23/player/kaka/1238', '/en/fifa23/player/gianluca-zambrotta/1236', '/en/fifa23/player/ian-rush/1235', '/en/fifa23/player/alan-shearer/1234', '/en/fifa23/player/fabio-cannavaro/1233', '/en/fifa23/player/paul-scholes/1232', '/en/fifa23/player/miroslav-klose/1230', '/en/fifa23/player/yannick-carrasco/19038', '/en/fifa23/player/luis-hernandez/1229', '/en/fifa23/player/davor-suker/1228', '/en/fifa23/player/gary-lineker/1226', '/en/fifa23/player/christian-pulisic/19035', '/en/fifa23/player/edwin-van-der-sar/1225', '/en/fifa23/player/hernan-crespo/1224', '/en/fifa23/player/sol-campbell/1223', '/en/fifa23/player/fred/17559', '/en/fifa23/player/robin-van-persie/1117', '/en/fifa23/player/park-ji-sung/19', '/en/fifa23/player/casillas/1111', '/en/fifa23/player/xabi-alonso/163', '/en/fifa23/player/benjamin-white/19071', '/en/fifa23/player/moussa-sissoko/17508', '/en/fifa23/player/wilfried-zaha/17459', '/en/fifa23/player/fikayo-tomori/17420', '/en/fifa23/player/bremer/17411', '/en/fifa23/player/raphinha/17399', '/en/fifa23/player/robbie-keane/15571', '/en/fifa23/player/joan-capdevilla/15567', '/en/fifa23/player/wlodzimierz-smolarek/15558', '/en/fifa23/player/sidney-govou/15554', '/en/fifa23/player/ronald-araujo/17778', '/en/fifa23/player/frank-rijkaard/1286', '/en/fifa23/player/christian-vieri/1284', '/en/fifa23/player/petr-cech/1283', '/en/fifa23/player/david-trezeguet/1282', '/en/fifa23/player/peter-schmeichel/1281', '/en/fifa23/player/roy-keane/1278', '/en/fifa23/player/ruud-van-nistelrooy/1277', '/en/fifa23/player/raul/1276', '/en/fifa23/player/michael-owen/1275', '/en/fifa23/player/pavel-nedved/1274', '/en/fifa23/player/puyol/1273', '/en/fifa23/player/steven-gerrard/1272', '/en/fifa23/player/andriy-shevchenko/1271', '/en/fifa23/player/juan-sebastian-veron/1270', '/en/fifa23/player/john-barnes/1269', '/en/fifa23/player/frank-lampard/1268', '/en/fifa23/player/fernando-hierro/1266', '/en/fifa23/player/patrick-kluivert/1265', '/en/fifa23/player/michael-ballack/1264', '/en/fifa23/player/henrik-larsson/1263', '/en/fifa23/player/cristian-romero/19040', '/en/fifa23/player/theo-hernandez/17626', '/en/fifa23/player/denis-zakaria/18994', '/en/fifa23/player/antony/17325', '/en/fifa23/player/darwin-nunez/17324', '/en/fifa23/player/aurelien-tchouameni/17323', '/en/fifa23/player/gabriel-jesus/17321', '/en/fifa23/player/wayne-rooney/1120', '/en/fifa23/player/timo-werner/19074', '/en/fifa23/player/saeed-al-owairan/15592', '/en/fifa23/player/michael-essien/1308', '/en/fifa23/player/ronald-koeman/1307', '/en/fifa23/player/gheorghe-hagi/1306', '/en/fifa23/player/emmanuel-petit/1305', '/en/fifa23/player/michael-laudrup/1304', '/en/fifa23/player/fernando-torres/1303', '/en/fifa23/player/hernan-crespo/1302', '/en/fifa23/player/clarence-seedorf/1301', '/en/fifa23/player/gianfranco-zola/1300', '/en/fifa23/player/ashley-cole/1299', '/en/fifa23/player/davor-suker/1298', '/en/fifa23/player/gennaro-gattuso/1297', '/en/fifa23/player/robert-pires/1296', '/en/fifa23/player/rui-costa/1295', '/en/fifa23/player/laurent-blanc/1294', '/en/fifa23/player/ian-wright/1293', '/en/fifa23/player/sol-campbell/1292', '/en/fifa23/player/jari-litmanen/1291', '/en/fifa23/player/rio-ferdinand/1290', '/en/fifa23/player/nemanja-vidic/1289', '/en/fifa23/player/claude-makelele/1288', '/en/fifa23/player/luis-hernandez/1287', '/en/fifa23/player/kim-min-jae/18996', '/en/fifa23/player/ousmane-dembele/17533'
]
icons1 = []
result = []
db['playerbase'] = []
while True:
    keep_alive()
    result = []
    tempdb = []
    for i in icons:
        url = 'https://www.futwiz.com' + i + '/soldprices/pc'
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        div = soup.find('div', class_='main-content background-bright')
        if div == None:
            continue
        div = div.find('div', class_='text-right mb-20')
        price = div.b.text.split(',')
        Lbin = ''
        for j in price:
            Lbin = Lbin + j
        Lbin = int(Lbin)
        temp = 0
        avquant = 0
        bins = []

        leftContent = soup.find('div', class_='col-9 leftContent').find_all(
            'div', class_='salerow')
        if len(leftContent) == 0:
            continue
        number = min(20, len(leftContent))
        for j in range(number):
            if leftContent[j]['data-status'] == 'BIN':
                avquant += 1
                st = ''
                buyprice = leftContent[j].find_all(
                    'div', class_='sale-table-data')[2].text.split(',')
                for k in buyprice:
                    st += k
                bins.append(int(st.strip()))
                buyprice = int(st)
                temp += buyprice
        if avquant == 0:
            continue
        bin_average = int(temp / avquant)
        binstring = ''
        for h in range(len(bins)):
            if bins[h] > bin_average * 12 / 10 or bins[
                    h] < bin_average * 8 / 10:
                temp -= bins[h]
                avquant -= 1
                bins[h] = -1
            else:
                binstring += str(bins[h]) + ' '
        if avquant == 0:
            continue
        bin_average = int(temp / avquant)
        if Lbin == 0:
            continue
        gain_percentage = round((bin_average * 95 / 100 - Lbin) / Lbin, 2)
        img_src = soup.find('div', class_='col-9 leftContent').find(
            'div', class_='sale-block').find('img')['src']
        card_name = soup.find('div', class_='headertitle').find(
            'div', class_='wrap').h1.text.strip()
        flag = gain_percentage > 0.03 and Lbin > 10000
        if flag:
            print("found")
            temps = card_name.split()[0:-2]
            card_name = ''
            for s in temps:
                card_name += s + ' '
            tempdb.append([
                img_src, card_name, url, gain_percentage, Lbin, bin_average,
                binstring
            ])
    db['playerbase'] = tempdb
