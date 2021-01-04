# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Mitsuha", color="#c8ffc8")
define s = Character("Kana", color="#c8c8ff")
define b = Character("Yamazaki", color="#0000ffff")
define c = Character("Sakura")
define d = Character("Ibu")
define z = Character("Guru")


  
# The game starts here.

label start:
    play music "music1.mp3"
    
    show kamar
    with fade
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    e "Ini masih sangat pagi...*menguap*"
    e "Semangat, semangat, tinggal satu bulan lagi sebelum libur tiba"
    e "Rasanya hidup sebagai mahasiswa lebih menyenangkan, daripada di SMA"
    e "Serasa lebih bebas melakukan apapun"
    
    d "Ginsan bangun, nanti kamu terlambat"
    e "Iya, Iya"
    e "Uggh, setidaknya ini hari jumat dan besok libur"
    
    hide kamar
    
    play music "music2.mp3"
    show kelas
    with fade
    
    "Hari berjalan seperti biasa"
    "Kamu duduk dipojok kelas dan sibuk dengan duniamu sendiri"
    z "Yamazaki sudah ibu bilang untuk melepas headphonemu saat berada dikelas"
    
    "Teriakan Guru membuatmu sadar dari lamunan"
    
    show yamaken1
    with fade
    
    "Yamazaki seketika terkejut dan melepas headphonenya"
    b "ooooh... Maaf saya tidak melihat ibu datang"
    "Yamazaki merupakan teman sekelasmu, lebih muda sebulan, dan orangnya sangat santai. Bisa dibilang kamu dan dia berteman akrab"
    
    hide yamaken1
    show sakura2
    with dissolve
    
    "Kamu melihat Sakura, yang merupakan pacar Yamazaki dan juga teman dekat dengan Kana"
    "Sakura dan Yamazaki sudah satu tahun pacaran, kamu heran kenapa mereka langgeng padahal keduanya memiliki kepribadian yang berbeda"
    
    "Lalu kamu melihat kearah Kana, Dia sedikit pemalu dibandingkan dua lainnya"
    "Kamu memikirkan bagaimana bisa bersahabat dengan ketiga orang ini..."
    "Kamu tersadar ketika melihat Kana dan Sakura mulai mengobrol"
    
    hide sakura2
    
    menu:
        
        "Apakah kamu ingin bergabung?"
        "Bergabung.":
            jump bergabung
        "Lanjut Tidur.":
            jump lanjut
        
label bergabung:
    show mitsuha1 at right
    show sakura2 at left
    
    s "Hey Ginsan, kau sedang apa? dari tadi aku lihat kau bengong terus?"
    c "Apakah kau sakit?"
    
    "Mereka menatap cemas kearahku"
    
    jump jawab

label lanjut:
    
    e "aku mengantuk lebih baik tidur saja"
    
label jawab:
    
    show mitsuha1 at right
    show sakura2 at left
    with fade
    
    e "Aku tidak apa-apa, hanya mengantuk saja"
    hide sakura1
    c "hmmm.. Ginsan ada yang ingin aku tanyakan"
    show sakura1 at left
    with dissolve 
    s "Sebentar sebelum itu mari kita panggil pacarku dulu"
    s "Yamazaki siniii"
    
    show mitsuha1 at right
    show yamaken1 at center
    with fade
    b "Ada apa? Sepertinya seru sekali"
    hide mitsuha1
    show yamaken1 at right
    with dissolve
    s "Sini deh, Kau masih ingat rencana kita yang kemarin?"
    hide sakura1
    b "Menyelinap diam-diam?"
    show sakura3 at left
    with dissolve
    s "Tepat sekali... Kau memang pacar terbaikk"
    
    "Mereka berdua berpelukan, sedangkan aku dan Kana hanya bisa menyasikkan keromantisan yang cukup memuakkan"
    
    show mitsuha1 at center
    with dissolve
    c "Ekhemmm.... tolong ya jangan bermesraan disini"
    hide yamaken1
    show mitsuha1 at right
    with dissolve
    s "Hehehe maaf, kalian berdua single kan? Kenapa tidak jadian saja?"
    
    hide yamaken1
    hide sakura1
    hide mitsuha1
    show mitsuha2 at center
    with dissolve
    "Akupun terbatuk saking kagetnya, kulirik Kana mukanya memerah"
    
    
        
        
    
    
    
    
    
        
        

    # These display lines of dialogue.

   
    
    
   
        

    # This ends the game.
    

    return
    
