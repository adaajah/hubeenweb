from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "rahasia-besar"

# Data password tiap hero
hero_passwords = {
    "Nara": "n4r*123",
    "Qilan": "q1lan*123",
    "Iza": "iz44123",
    "Hada": "hadanaja",
    "Muti": "mut1*123",
    "Nur": "nur*123",
    "Mufid": "muf1d*123",
    "Bagus": "bagu5*123",
    "Dimas": "d1m4s123",
    "Devara": "d3vara*123",
    "Jiyad": "jiy4d*123"
}

# Data detail hero
hero_data = {
    "Nara": {
        "title": "Nara Kaka Paling Ceria",
        "image": "nara.jpg",
        "music": "nara.mp3",
        "description": """<p> Assalamu'alaikum, teh nara Gimana kabarnya? \n </p>
<p> Semoga sehat selalu ya, semoga bisa lulus dgn hasil yang memuaskan, trus kita bisa main bareng lagi sama hubin yg seru ini.
Makasih juga teh untuk satu setengah tahunnya, makasih udah nerima aku di stafma hubin. Bikin aku jatuh cinta di hubin, gabakal mau aku masuk kmmk kalo ga dikenalin Pangandaran PSDKU, LDF-LDF semua itu karena hubin ini. </p>
<p> makasih juga ya teh, udah mau bantu aku di ahlan ini, keren bgt support tmn2 hubin buat bantuin aku, aku beneran ngerasa terbantu bgt teh. juga PR wewww. Aku juga seneng liat tmn-tmn yang masih istiqomah jaga hapalan, nuansa islamnya, jarang bgt ketemu org keren kyk gini teh. Semoga Istiqomah ya teh.. Nanti ketemu orang yang ganteng sholeh idaman cocok sama teteh jga wkwkwk aaminnn... </p>
<p> Jujur ya, aku juga seneng kebiasaan dokumentasi dari teteh kyk kumpul dikit foto, ada yg kocak lgsg video, semua tu bikin kenangan ini bisa diabadikan, terlebih lagi hpnya mendukung wkwkwk. Tapi terlepas dari itu semua aku seneng bgt liat dokumentasi-dokumentasi kita selama di hubin. Terus pertahanin kebiasaan lucu ini teh wkwk, oiya sekalian aja jadi yutuberr. Aku dukung no 1 klo jadi🤲 </p>
<p> Oiya mau bilang satu hal lagi, maafin klo aku ada salah teh, baik itu perkataan perbuatan atau apapun itu, kalo ada utang bilang aja teh ke akumah, klo sanggup aku gnti hehehe, diikhlasin lebih gacor wkwkw canda. </p>
<p> Semangat teh jadi BA wardahnya semoga nanti bisa kerja juga di paragonnya, trs dpt jodo(h) yg dimau cieehh kiwkiw cukurupyuk... Awww. </p>
<p> Dah ah teh sekian gabakal bisa nulis disini semua nanti bakal berlembar-lembar malah jadi novel 'teh nara si paling ceria' nnti. </p>
<p> Dah Assalamu'alaikum teh. 👋.</p>
<p>Salam hangat,</p>
<p>Hada</p>"""
    },
    "Iza": {
        "title": "Iza Kaka Pengayom para Adik",
        "image": "iza.jpg",
        "music": "iza.mp3",
        "description": """ <p> A es es.. </p> 
<p> Assalamu'alaikum tehh izaaa, </p>
<p> Gimana kabarnya tehh? Semoga baik baik saja ya disini aku slalu do'ain untuk kesehatan dan kelancaran teteh dalam segala urusan. Ciee yang bentar lagi mau lulus. Jadi gasabar nge-apres teteh-teteh hubin nih, semoga dapet hasil yang terbaik yaa. </p>

<p>Btw makasih teh udah ngenalin aku di hubin ini, makasih udah nerima aku di stafma hubin karna hal ini bikin aku jatuh cinta ama hubin ini. Gabakal aku mau masuk kmmk klo ga dikenalin Pangandaran Psdku, ldf-ldf dan keasikan di dalemnya. Aku juga seneng liat teteh yang masih istiqomah menjaga hapalannya, nuansa islamnya jarang bgt ketemu org keren kyk teteh gini. Semoga Istiqomah ya teh.. Nanti ketemu orang yang ganteng sholeh idaman cocok sama teh izaa jga wkwkwk aaminnn... </p>
<p> Makasih juga teh, udah mau bantu aku di ahlan ini, keren bgt support tmn2 hubin buat bantuin aku, aku beneran ngerasa terbantu bgt teh. apalagi medkraf itu suka ada ajaa revisi, tugas numpuk parah bgett, maaf ya teh ade satu ini sangat  merepotkan, makasih sebanyak-banyaknya buat teh izaa</p>
<p>Jujur selama teteh ada di hubin ini, aku ngerasain sosok kakak yang mengayomi ade-adenya. Ikut bantu permasalahan kita, slalu ada buat kita, bahkan slalu nenangin kita klo ada yang berantem wkwkw meskipun bercanda sih. Makasih udah jadi kaka kita selama satu setengah tahun ini, asliii banyak banget yang mau aku sampein ke teteh. Tapi gabakal cukup kyknya klo di tulisan kecil gini wkwk, nanti malah jadi novel 'iza si kaka hubin' 😆</p>

<p>Oiya sama satu hal lagi, maafin ya kalo hada ada salah sama teteh baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo aku ada utang ama teteh, klo aku sanggup InsyaAllah aku ganti teh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>

<p> Dah ya tehhh nanti lagi, semoga hubin bisa main lagi bareng2. </p>
<p>Salam hangat,</p>
<p>Hada</p>"""
    },
    "Qilan": {
        "title": "Qilan Si Penyayang",
        "image": "qilan.jpg",
        "music": "qilan.mp3",
        "description": """ <p> Assalamu'alaikum qilan, </p> 
        <p> Gimana kabarnya qilan? Semoga sehat selalu ya, disini gwe slalu do'ain untuk kesehatan dan kelancaran lo dalam segala urusan.</p>
        <p>Makasih ya udah mau nemenin gwe dihubin ini selama kurang lebih satu setengah tahun, mulai dari magang ampe jadi staff wkwk masih ae betah bang, banyak cerita, kocak-kocakan bareng apalagi kalau kita kumpul bareng, Kagak bisa ditahan ngakak bah wkwkw, kadang kasian ama bagus suka kena bully wkwkwk parah si lu qil</p>
        <p>Tapi jujur itu juga bikin gwe kangen sama hubin ini, semoga kita bisa terus bareng-bareng, kita bisa terus bertemu dan menjaga silaturahim kita . jangan lupain gwe ya, eh kali kali ajak gwe main sumedang lah yehh kumaha maneh. padahal tinggal naik motor ae wkwk. atur jadwal ae bang ye hehe</p>
        <p>Oiya sama satu hal lagi, maafin ya kalo gwe ada salah sama lo baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo gwe ada utang ama lu qil, klo sanggup InsyaAllah aye ganti deh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>
        <p>Dah ya masss nanti lagi, semoga hubin bisa main lagi bareng2. </p>
        <p>Salam hangat,</p>
        <p>Hada</p>"""
    },
    "Hada": {
        "title": "Hada Sang Kreator",
        "image": "hada1.jpg",
        "music": "hada.mp3",
        "description": """<p> Assalamu'alaikum hadaaa, </p>
<p> Gimana kabarnya hada? Semoga sehat selalu ya, disini aku slalu memanjatkan do'a untuk kelancaranmu dalam segala urusan da. jangan pernah berhenti berharap ya, berharap pada Tuhanmu da,,, </p>
<p> Makasih ya udah mau tumbuh da, makasih udah mau lewatin masa perkuliahan ini, makasih udah berusaha jadi versi terbaik dirimu, makasih udah mau jadi kreator dari website ini, makasih udah berani ngambil keputusan.</p>
<p> Aku tau, ini bukan hal yang mudah, aku tau ini berat, aku tau ini bikin pusing, capek, stress, galau, baper, sedih, nangis, marah, kesel, kecewa, sakit hati, sakit fisik, aku tau ini semua berat. tapi, i know u strong</p>
<p> i hope you know that you are not alone, aku disini selalu ada buat kamu, aku disini selalu support kamu, aku disini selalu do'ain kamu, aku disini selalu sayang kamu. </p>
<p> always remember that you are family hopes, kmu punya adik yang harus dijaga dididik, kamu pasti bisa.</p>
<p> maaf ya, blm bisa jadi versi terbaik hada.</p>
<p> maaf ya</p>
<p> <br> </p>
<p> its okay u always have Allah on your side, did u remember how u born? </p>
<P> how u survived? </p>
<p> how u made it this far? </p>
<p> He always have a plan for you, always gives you the best part of u're life.</p>
        
        <p>wait, i have a poem for you </p>
<p>  <br> </p>
        
        
        
        
        <p> Ada masanya ingin memiliki seseorang, </p>

<p> Tapi itu tak sepadan dengan kehilangan ketenangan, </p>
<p> tak sepadan dengan kehilangan keimanan </p>
<p> Jangan biarkan perasaan sementara itu menghancurkan versi terbaik dirimu </p>
<p> Jangan biarkan cinta yang belum halal mengganggumu dari pasangan yang sudah Allah siapkan dan Allah jaga untukmu🩹 </p>

<p> salam hangat,</p>
<p>Hada</p>"""
    },
    "Muti": {
        "title": "Muti Si Dedek Hubin",
        "image": "muti.jpg",
        "music": "muti.mp3",
        "description": """<p> hai </p>
<p>Konnichiwa </p>
<p>annyeong haseyo </p>
<p>holaa</p>
<p>Assalamualaikum mutia,</p>
<p>Gimana kabarnya mutt? Semoga baik baik saja ya disini aku slalu do'ain untuk kesehatan dan kelancaran kmu dalam segala urusan. ciee udah jadi kaka pk yaa, wkwk ga nyangka aja si dede hubin ini jadi kaka hahaha maap maap. canda lho ya. btw suka bgt di kmmk ini ketemu banyak org soleh solehah, udah jarang bgt sekarang nyari yang pakaiannya rapi tertutup, semoga kamu istiqomah yeee </p>
<p>makasih ya udah mau nemenin aku di hubin ini kurang lebih hampir 1 tahun, jujur ini seru banget di hubin apalagi sama kamu. banyak kenangan yg ga bisa aku lupain kocak kocakan bareng, cerita cerita, main games...semua itu bikin aku kangen deh ama hubin ini. aku ngerasa hubin ini bukan cuma departemen aja tpi lebih dari itu. </p>
<p>oiya aku juga pgn bilang makasi banyak kamu udah mau bantu proker pengabdian aku, meskipun awalnya aku cuma mau minta sumbangan buku aja, eh tiba tiba bgt kmu ikutt weiii,, kaget bgt. tpi jujur klo gada kamu keknya aku bakal cape bgt deh,  u know lah gmn nak te kmrn. thanks ya. sama klo ada yg mau disampein feel free aja mut. aman azaaa </p>
<p>makasih juga udah mau nemenin aku di Ahlan ini. lagi lagi aku kaget kamu mau jadi logistik kek gimana gitu akhwat ambil logis mana kamu ada pk lagi sibuk bgt, mana banyak angkut barang lagi duh maaf ya. makanya aku kmrn gamau ninggalin logis sendiri. semoga kamu ga nyesel ya ikut bantu logis di Ahlan ini. btw mood kmu lucu bgt suka tiba-tiba habis wkwkw real aku jga gtu sih, kadang butuh waktu sendiri, kadang pgn bareng-bareng. apapun itu tetep happy ya hadapin pelan-pelan. </p>
<p>Oiya sama satu hal lagi, maafin ya kalo aku ada salah sama kmu baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo aku ada utang, klo aku sanggup InsyaAllah aku ganti mutt... Klo diikhlasin.. Siapa sih yang gamau 😅 </p>
<p>sebenernya banyak yang mau aku sampein ke kamu tapi gabakal muat lah disini , nanti malah berlembar lembar bisa jadi novel kali, 'muti si ade hubin' wkwk. dah ya </p>
<p>salam hangat,</p>
<p>hada</p>
"""
    },
    "Nur": {
        "title": "Nur Si Paling doi",
        "image": "nur.jpg",
        "music": "nur1.mp3",
        "description": """<p> Assalamu'alaikum nur, </p>
<p> Gimana kabarnya nur? Semoga sehat selalu ya, disini gwe slalu do'ain untuk kesehatan dan kelancaran kmu dalam segala urusan.</p>
<p>Makasih ya udah mau nemenin aku dihubin ini selama kurang lebih satu tahun banyak cerita, kocak-kocakan bareng apalagi kalau udah kumpul bareng, Kagak bisa ditahan ngakak bah wkwkw, kadang kasian ama mupidd suka kamu bully wkwkwk parah si nur</p>
<p>Tapi jujur itu juga bikin aku kangen sama hubin ini semoga kita bisa terus bareng-bareng, kita bisa terus bertemu dan menjaga silaturahim kita . jangan lupain aku ya, eh kali kali ajak aku main sumatra lah yehh kumaha maneh. padahal pengen banget tau pergi ke sumatera atas sana. atur jadwal ae kak ye, bantu ongkos jga hehe</p>
<p>Oiya sama satu hal lagi, maafin ya kalo aku ada salah sama kmu baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo aku ada utang ama kmu  nur, klo sanggup InsyaAllah aye ganti deh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>
<p> BTWWWWW oi belum cerita! gamau nunggu lulus. utang bomat.<p/>
<p>Dah ya nurr nanti lagi, semoga hubin bisa main lagi bareng2. jgn lupain aku.</p>
<p>Salam hangat,</p>
<p>hada</p>"""
    },
    "Mufid": {
        "title": "Mufid El Risol",
        "image": "mufid.jpg",
        "music": "mufid.mp3",
        "description": """<p> Assalamualaikum pid,</p>
<p> Gimana kabarnya pid? Semoga sehat selalu ya, disini aku slalu do'ain untuk kesehatan dan kelancaran lu dalam segala urusan. </p>
<p>Makasih ya udah mau nemenin aku dihubin ini selama kurang lebih satu tahun banyak cerita, kocak-kocakan bareng apalagi kalau lo ngomong tuh suka paling ngena dah hahah, Kagak bisa ditahan ngakak bah wkwkw </p>
<p>Tapi jujur itu juga bikin aku kangen sama hubin ini semoga kita bisa terus bareng-bareng, kita bisa terus bertemu dan menjaga silaturahim kita . jangan lupain gwe ya, eh kali kali ajak gwe main serang lah yehh kumaha maneh. padahal tinggal naik krl ae wkwk. atur jadwal ae bang ye hehe</p>
<p>Oiya sama satu hal lagi, maafin ya kalo hada ada salah sama lo pid, baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo gwe ada utang ama lu pid, klo sanggup InsyaAllah aye ganti deh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>
<p>Dah ya masss nanti lagi, semoga hubin bisa main lagi bareng2. </p>
<p>Salam hangat,</p>
<p>Hada</p>"""
    },
    "Bagus": {
        "title": "Bagus Si Paling Komedi",
        "image": "bagus1.jpg",  
        "music": "lagu.mp3",
        "description": """<p> Assalamu'alaikum gus, </p>
<p> Gimana kabarnye bos? Semoga baik baik saja ya, disini gua slalu do'ain untuk kesehatan dan kelancaran lu dalam segala urusan. </p>
<p>Makasih ya udah mau nemenin gua dihubin ini selama kurang lebih satu setengah tahun banyak cerita, kocak-kocakan bareng apalagi kalau lo ngelawak tuh paling kocak dah, Kagak bisa ditahan ngakak bah wkwkw </p>
<p>Tapi jujur itu juga bikin gua kangen sama hubin ini semoga kita bisa terus bareng-bareng, kita bisa terus bertemu dan menjaga silaturahim kita gus . jangan lupain gwe ya, woi lu jaga kesehatan jangan begadang bae lah yehh kumaha maneh. kuliah itu no 1 bang wkwk. semoga lulus cepet bareng</p>
<p>makasih juga ya gus udah mau bantuin gua di Ahlan ini, keren bgt support tmn2 hubin buat bantuin gua, asli beneran ngerasa terbantu bgt gus. apalagi Logis itu kerjanya ekstra parah, mana bnyk barang dadakan pula, maaf ya gus orang satu ini sangat merepotkan, makasih sebanyak-banyaknya buat bagus</p>
<p>Oiya sama satu hal lagi, maafin ya kalo hada ada salah sama lo baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo gwe ada utang ama lu gus, klo sanggup InsyaAllah aye ganti deh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>
<p>Dah ya masss nanti lagi, semoga hubin bisa main lagi bareng2. </p>
<p>Salam hangat,</p>
<p>Hada</p>"""
    },
    "Dimas": {
        "title": "Dimas Si Paling Ketawa Brutal",
        "image": "dimas.jpg",
        "music": "dimas.mp3",
        "description": """
       <p> Halooo </p>
       <p> Hola </p>
       <p> Helo</p>

<p>Assalamu'alaikum mas dim, </p>

<p>Gimane kabarnye bos? Semoga baik baik saja ya, disini gua slalu do'ain untuk kesehatan dan kelancaran lu dalam segala urusan. </p>
<p>Makasih ya udah mau nemenin gua dihubin ini selama kurang lebih satu setengah tahun banyak cerita, mulai dari magang ampe jadi staff wkwk masih ae betah bang, banyak cerita, kocak-kocakan bareng apalagi kalau lo ketawa tuh paling kenceng dah, Kagak bisa ditahan ngakak bah wkwkw </p>
<p>Tapi jujur itu juga bikin gua kangen sama hubin ini semoga kita bisa terus bareng-bareng, kita bisa terus bertemu dan menjaga silaturahim kita . jangan lupain gwe ya, eh kali kali ajak naik gunung bareng lah yehh kumaha maneh. seru seruannya ama sasrab ae wkwk. atur jadwal ae bang ye hehe</p>
<p>Oiya sama satu hal lagi, maafin ya kalo hada ada salah sama lo baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo gwe ada utang ama lu dim, klo sanggup InsyaAllah aye ganti deh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>
<p>Dah ya masss nanti lagi, semoga hubin bisa main lagi bareng2. </p>
<p>Salam hangat,</p>
<p>Hada</p>"""
    },
    "Devara": {
        "title": "Devara Si Paling Humble",
        "image": "devara.jpg",
        "music": "devara.mp3",
        "description": """ <p> Assalamu'alaikum devara, </p>
        <p> Gimana kabarnya dep? Semoga sehat selalu ya, disini gwe slalu do'ain untuk kesehatan dan kelancaran teteh dalam segala urusan.</p>
        <p>Makasih ya udah mau nemenin gwe dihubin ini selama kurang lebih satu tahun banyak cerita, kocak-kocakan bareng apalagi kalau lo ber-tiga udah kumpul, Kagak bisa ditahan ngakak bah wkwkw, kadang kasian ama bagus suka kena bully wkwkwk parah si dep</p>
        <p>Tapi jujur itu juga bikin gwe kangen sama hubin ini semoga kita bisa terus bareng-bareng, kita bisa terus bertemu dan menjaga silaturahim kita . jangan lupain gwe ya, eh kali kali ajak gwe main Subang lah yehh kumaha maneh. padahal tinggal naik motor ae wkwk. atur jadwal ae bang ye hehe</p> 
        <p>Makasih juga ya dep udah mau bantuin gw di Ahlan ini, keren bgt support tmn2 hubin buat bantuin gw, asli beneran ngerasa terbantu bgt dep. apalagi medkraf itu suka ada ajaa revisi, tugas numpuk parah bgett, maaf ya dep vpo satu ini sangat merepotkan, makasih sebanyak-banyaknya buat devara</p>
        <p>Oiya sama satu hal lagi, maafin ya kalo gwe ada salah sama lo baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo gwe ada utang ama lu dep, klo sanggup InsyaAllah aye ganti deh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>
        <p>Dah ya masss nanti lagi, semoga hubin bisa main lagi bareng2. </p>
        <p>Salam hangat,</p>
        <p>Hada</p>"""
    },
    "Jiyad": {
        "title": "Jiyad si Paling Famous",
        "image": "jiyad.jpg",
        "music": "jiyad.mp3",
        "description": """<p> Assalamualaikum jiyad, </p>
        <p> Gimana kabarnya jiyad? Semoga sehat selalu ya, disini gwe slalu do'ain untuk kesehatan dan kelancaran lu dalam segala urusan.</p>
        <p>Makasih ya udah mau nemenin gwe dihubin ini selama kurang lebih satu tahun banyak cerita, kocak-kocakan bareng apalagi kalau lo ber-tiga udah kumpul, Kagak bisa ditahan ngakak bah wkwkw, kadang kasian ama bagus suka kena bully wkwkwk parah si yad</p>
        <p>Tapi jujur itu juga bikin gwe kangen sama hubin ini semoga kita bisa terus bareng-bareng, kita bisa terus bertemu dan menjaga silaturahim kita . jangan lupain gwe ya, eh kali kali ajak gwe main Subang lah yehh kumaha maneh. padahal tinggal naik motor ae wkwk. atur jadwal ae bang ye hehe</p>
        <p>Makasih juga ya jiyad udah mau bantuin aku di Ahlan ini, keren bgt support tmn2 hubin buat bantuin aku, aku beneran ngerasa terbantu bgt jiyad. apalagi fundra itu cuma 2 org weii,mana mnh baru pertama kali kan disini, maaf ya jiyad orang satu ini sangat merepotkan, makasih sebanyak-banyaknya buat jiyad</p>
        <p>Oiya sama satu hal lagi, maafin ya kalo gwe ada salah sama lo baik itu perkataan, perbuatan sikap atau apapun itu, bilang juga kalo gwe ada utang ama lu yad, klo sanggup InsyaAllah aye ganti deh... Klo diikhlasin.. Siapa sih yang gamau 😅</p>
        <p>Dah ya masss nanti lagi, semoga hubin bisa main lagi bareng2. </p>
        <p>Salam hangat,</p>
        <p>Hada</p>"""
    }
}

@app.route("/")
def index():
    return render_template("index.html", hero_data=hero_data)

@app.route("/hero/<hero>", methods=["GET", "POST"])
def hero_login(hero):
    if hero not in hero_data:
        return "<h3>Hero tidak ditemukan.</h3><a href='/'>Kembali</a>"
    
    if request.method == "POST":
        pw = request.form.get("password", "")
        if pw == hero_passwords.get(hero):
            data = hero_data[hero]
            return render_template("hero_detail_template.html",
                                   hero_name=hero,
                                   hero_title=data["title"],
                                   hero_image=data["image"],
                                   hero_description=data["description"],
                                   hero_music=data["music"])
        else:
            return render_template("hero_login_template.html",
                                   hero_name=hero,
                                   hero_title=hero_data[hero]["title"],
                                   error="Password salah!")
    return render_template("hero_login_template.html",
                           hero_name=hero,
                           hero_title=hero_data[hero]["title"])

if __name__ == "__main__":
    app.run(debug=True)
