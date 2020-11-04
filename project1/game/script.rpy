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
    
    d "Mitsuhaaaa bangun, nanti kamu terlambat"
    e "Iya, Iya"
    e "Uggh, setidaknya ini hari jumat dan besok libur"
    
    hide kamar
    show kelas
    with fade
    
    "Hari berjalan seperti biasa"
    "Kamu duduk dipojok kelas dan sibuk dengan duniamu sendiri"
    z "Yamazaki sudah ibu bilang untuk melepas headphonemu saat berada dikelas"
    
    "Teriakan Guru membuatmu sadar dari lamunan"
    
    show yamazaki
    with fade
    
    "Yamazaki seketika terkejut dan melepas headphonenya"
    b "ooooh... Maaf saya tidak melihat ibu datang"
    "Yamazaki merupakan teman sekelasmu, lebih muda sebulan, dan orangnya sangat santai. Bisa dibilang kamu dan dia berteman akrab"
    
    hide yamazaki
    show Kana
    with dissolve
    
    "Kamu melihat Sakura, yang merupakan pacar Yamazaki dan juga teman dekat dengan Kana"
    "Sakura dan Yamazaki sudah satu tahun pacaran, kamu heran kenapa mereka langgeng padahal keduanya memiliki kepribadian yang berbeda"
    
    "Lalu kamu melihat kearah Kana, Dia sedikit pemalu dibandingkan dua lainnya"
    "Kamu memikirkan bagaimana bisa bersahabat dengan ketiga orang ini..."
    "Kamu tersadar ketika melihat Kana dan Sakura mulai mengobrol"
  
    "Apakah kamu ingin bergabung?"
        
        

    # These display lines of dialogue.

   
    
    
   
        

    # This ends the game.
    

    return
    
