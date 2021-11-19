#jaffer Razavi
#oct 9 2019

CODE = 'password'
Pass = input("Enter the password. \n")

Pass=Pass.lower()


if CODE in Pass:
    print("Correct Passcode")
    print("""
MWWWMMMMMMxxxxxxMWMxxxxWnWMMxxxxxxxxWxxxxxxxxxx@@Wnxxxxxxxxxxxxxxxxnnxxxxxxxxxnnnzzzzzzzzzz######++++*****++####++++++++++++##########################
MWWWWMMMMMMxxxM@@##WMxx@xxWMnxxxxxxxWMxxxxxxxxW@@@Mnnxxxxxxxxnnnzzzzzznnnnnnxnnnzzzzzzzzz###++++++*iiiiiii******i******+++++++++#######++++++++++#####
MWWWWWMMMMMMM@@######Mn@WnMWxxMxxxMMWMxxxxxxxxW@W@@Wnxxxxxxnnz########zzzzzznnnnz#zzzzzz##+++++++*ii;;;;ii*****i*******+++++++++++++++++++++++++++++++
MWWWWWMMMWW@@@###@##@xnW@WzWWWxnxxxW@xnnnnnnnx@W@@W@xnxxxnnzz#++#++++##zzznnzzzzz##z####+*******ii;:;:;;;ii*************+++++++++++++++++++++++++++*++
WWWWWWW@@@@@@@##Mn@#Mz#MM@WMW@MnzznM@nnnnzzznWMzz@WW@xznnnnzz#+++++++##zzzzzzzzzzzzz###+i;;ii;;;;:::::::::;;iiii*ii*****i****************++++++*****+#
MWWWWW@@@@@@@@#Mnn@Wx##nWW@@W@@x##zx@nznzz###Mnzn@@WW@Wnz#+++*****++#zzzzzzzzzzzzzz+++*iii;;;;;::,,,,,,,,,:;;iiiiiiiiiiiiii****************++******++#
MWWW@@@@@@@@@#@nzMWzxzznWWM@@@@Wx##nWz#n#####nn#M@@@WMW@Wn+*++****+#zzzzzzzzzzzzz##+*ii;;;;;;::,,,,,,,,,,,,:;;i;;ii;iiiiiiiiiii*****++++**+++*****++##
MW@#@@@@@##@##xnxMnznMzxn@@@@@#Wxx+xM*#z##+###z#M@@@@WMWWW#++++++++zzzzzzzzzzzzzz##+*;:::::,,,,,,..,,,,,,,,,,::;;;;;;;;;;iiii*i****+++++**+++****+++##
W@#@@@@###@##@nnnzzznWnMzMW#@W@WMMx@#*n+##+#####n@@@@@@@WWWMxnz##zzznnznnnzzzz###+**i;::::,.,,...............,::::::::::;;iii*****++++++++++*****+++##
#@@@@@@##@@##Mzzz#zxxxW@@@WW#@WWMx@@inz++#+#+##+n@@@@@@@@WWWWMzzzzzzznzzzz######+*i;;;::;::,,..................,::::::::;;;iii******++++++*****+++####
@@@@@@@@@@###nznz#z#+WW@@@WW@#@WxnMWxMz#+###+++#n@@@@@W@@@@@WWWMMxz##zzz##+++++***iiii;;;;::,,.....`..........,,::::::::;;;;;iiii**++++++++***++++####
@@@@@@@@@###@zznz#z#zMM##WWWWWWWWnxWWMn#++#z+++#n@@@@@@@@@@@@@WWMMMnnxnz++******ii;;ii;;;;::,,,,,,.............,,:::::::;;;;ii*****+++++++*****++++###
@@@@@@@W@###Wzznz###MxW###@MWW@@WxnW@Wz++#zn###zn@@@@@@@@@@@@@@@WWMWWWWxz#+**iii;i;;;;;;:::::,,,,,.......`....,,,,:::::;;;;ii******************+++####
W@@@@@@@####Mzznz###x#M###@@WW@WMMxWW###znnnzzzzn@@@@@@@@@@@@@@@@@WWWWWWMMMn#i;;;;;::::::::,,,.,,,,...```....,,,,,::::;;;;;iiiiiiiii*********++####z##
@@@@W@W#####xzzzn####xM###@@@@@@MMMWxnxxxzznznzzx@@W@@@@@@@@@@@@WW@@WWWWWWMMMx#i;:::::::,,::,```.,,,...`....,,,,,,,,::;;;ii;;;;;;iii**+++++++###zzzzz#
@@@WW@W#####nzzzxn###+z##@@WWxWWWWWn#zzzznnnnnzzx@W@@@@@WW@@@@@@WWW@@@@WWWWWWMMxn+;:::::,,::.```.,,,........,,,,,,,,,:;;;;;;;;;;iii*++++++#####zzzzz##
@@WW@W@#####nzzzzxxz#+##@#@WWzzM@WMnxxnznnnnnnzzx@W@@@@WWW@@@@@@@WWWWW@@WWWWWWWMMMx#i:,,,,,,.````.,,........,,,,,,,,,,:;;;:;;;;iii*++++######zzzzzzzz#
@@WW@W######xzzzzzzxxxx@@#@@Wnx#@WMz#zxxxxnnnnzzMWW@@WWW@WW@@@@WWWWWWWWW@WWWMMxMMMMxn#i,,,,,,.```..,........,,,,,.....,::::;;;ii**+++#######zzzznnzzz#
@WWW@W######M##z#zzzz##M@#@WWxzx@WxzzznnnnnnnzznW@W@@WW@@@W@W@@@WWWWWWWWWWMMMzMxnxxxxnz+;,,,,,.```..,..,,...............:;;;;i***++#######zzzzzzznzzzz
@@WW@@######@####zzznzzn#@#@WW#+MWzzznnnnnzzz##xW@@@@@WWWW@W@W@@@WWWWWMMWMMMMM#zzzzzzzzz+i,.,,,......,,,,,..............,;;iii***+#######zzzznzznnnzzz
@WWWW#####@##n##zzznnnzn####WMM++n#zzznnnzzz#+#W@@@@WWWWWWWW@@@@@WWWMWWMMMMxMn*#,,,:;::i++*;,,,,.....,,,,,,,...........,,,;i****++#######zzzzzzznnzzzz
WWWWM########WzzzznnnnnxM#@@@WMx+#zzzznnnnz##+zW@@@@WWWWWWW@WW@WWWWWMWWWMMMMMx#:...,.....;**i:,,,.....,,,,,,,.........,,,,:;****++######zzzzzzzznnzzzz
WWWWW@########xnnnnnnnnnx@@@@@Wxn#zzzzznzzz##zW@@@@@WWWWMMMWMWWWWWWWWWWWWMxMMx+:..........,:;*;,,......,,,,,,,.....,...,,:::i*++++######zzzzzzzzzzzzzz
WWWWW@###@####@nnnnnnnnnnnWW@@WMzx#zzzzzzzz#nW@@@@@@WWWWWWMMMWWWWWWWWWWWWMMMMx*,..............:i,........,,,,,,...,....,,::;;i*+++######zzzzzzzzzzzzzz
WWWWWW###@@@##@MzzznnnnnzzW@@@WMxnnz#zzzzzzxWW@@@@@WWWWWWWMMMWWWWWWWWWWWWWMMMM#,...............,::,......,,,,:,,,,,,...,,:::;;i*++######zzzzzzzzzzzzz#
WWWWM@@@#@@@@@@@Mxxxxnzzznn@W@WMxMnn#zzzznWWWW@@@@@WWWWWWMWMxMWWWWWWWMMWWMxMMMn;:..............,,,:,,,,..,,,:::,,,,,...,,::::;i*+++#####zzzzzzzzzzzz#+
WWW@MW@@@@@@@@@@W@@@@@Mxnzn@@@@WMxxMnznxMWWW@@@@@@@@WWWWMWMMxxMWWWWWWMMWWWMMMMMzii:...........,,,,,,,,,,,,,,:::::,,,..,,,,:::;;i*++######zzzzzzzzzz##+
WWW@WxMMW#@@@@@@@@@@@@@@@W@##@@WWWxnM@@@WWWW@@@@@@@@W@@WMMMMMxxMWWWWWMMWWWMxMxMx#*+;.........,,,,,,,,,:::::,:::;;::,,,,,,::::;;ii*+#####zzzzzzzzzzz##+
WWW@@n#zx@#@@@@@@@@@@@@@##@#@@@WWWWxxW@WMWW@@@@@@@@WW@WWMMMMWMxxMWWWWWMMMWWMMMxMMz+*;,....,,,,,,,,,::::::::::;;;;;:::,,,:,,,::;;ii*+#########zz######+
WWW@@MzzzM#@@@@@@@@@@@@@@@@#@#@WWWMnxM@WWWW@@@@@WW@WW@WWWWWWWWMMMMMWWWMMMMMMMxxxMMxz+*;,,,,,,,::::::::::;;;;;;;;;ii;::::::,,,:;;iii*+##############+**
WWW@WWnznn@@@@@@@@@@@@@@@@@@@#@WWWWxxnWWWW@@@@@@@@W@W@WWWWWWWWWMMMMMWWWMxxxMMxxxxxMMnz+*;,:::::::::::::;iii;;;;;iii;;;:::::,,:;;iiii*+###+++##++++++**
W@WWW@xnnnM@@@@@@@@@@@@@@W@W@#@WWWWMzxM@@@@@@@@@WWWWW@WWWxnxxxMMxxxMMMWMxxxxMMnxnnnxMxz#+i::::::::::::;i***ii;;;iiiiii;;:::::::;;;iii*+#++++++++++***i
@@WWW@Mnnnn@@@@@@@@@@@@W@@W@W@#@W@@WnnxW@@@@@@WWWW@@@@WWW*:;#xxxxznxMMMMxxxxxMxnnnznxMxnz#*;:::::::::;;i*****i;;;iiiiiii;:::::::;;;;ii*+++++++++**iiii
W@WWWWWnnxnW@@@@@@@@@@@@@@W@W@@@@@WWznxWW@@@@@WWWMW@@@WWM;..,*xnziznnMWMxnnnxMMxnzznnnxxzzz+;:::::::;;ii**++**i;;iiiiiiii;;;;::;:;;;;;;i********ii;;ii
@WWWWM@MnnnM@@@@W@@@@@@W@WWWW@@@WW@WnxMW@@@@@@@Wnz#M@@WWM:``.,:+zznznnMMMnznnxMMxn#zznnxxnnn#;::::;;ii****+++**iiiiiiiiii;;;;;:::;;;;;;;iiiiiiii;;;;;i
WWW@WnMMnnnW@@@@@@@@@@@@@W@W@#@@@@WWnxWW@@@@@@Wi.,;zW@WWM:.``.,,+nnnnnxMMxzxnnnMxn#+#znnxnnnn#::::;iii****++++**iiiiiiiii;;;;;:::;:;;;;;:;;;;;;iii;iii
@WW@WxzMxnn@@@WW@@@@@@@@W@@@##@@WW@WnM@@@WWW@@n.``.:MWMMM;..``,,;#nnxxnxMxnznnnxMxn##zzznxxnnn+:::iii******++++**iii;;;ii;;;;;::;;::;:::::;;iiiiii;iii
@WWWWxzxMnx@@@@@@##@@@@@WW@@@@#@@@WWn@@WxznWWW#````.nxMWW*....:::i#nnnnxxMnzzznnxMxz#+#nnxxxnnz+:;ii*******+++++*ii;:::;;;;;;;;;:::::::::::;;iiiiiiii*
@@@W@MzzxxM@@@@@@@###@@@WWWW@@###@@WM#@M+iiz@M+````.*#nMWz,..,::;;iznxxxxMnzzzznnxMxn###znxxnnxn*;ii********+++**ii;:,,,,::;;;;;:::::::,::::;i*iiiii**
@@@WWWzz#xM@@@@xnnW##@@WWMMMMMM@@@WxW#@MiiiiMM+.....,,*xMn:,:::;;;;#znnxxxxxnnxnznxMxxz###zxxnnnn*i**************i;::,,,,:::;;;;;::::,,,,::::;iiii****
@@@@@Wn##xW@Wxnznnn#@@WWWWMMWWWMM@WnM#@niii;#Mz....,,,:#MMi:;;;iiii#nnnxxxMxnnnnnnxxMxxzzz+#znxnnn**************ii;:,,,,,,:::;;;;;:::,,,,,,,::i+******
@@@@@@x#zWWWnzzzznn@WWWWWW@@@@WWMWM#W@@ziii;ixn,,.,,,,:;nM+i;ii*i;;#nnnxxxxxnzzzznnxxMxnnnz#+znnznx#++**++++****ii;:,,:,,,:::::;i;;::,,,,,,,:;*++++++*
@@@@@@W#n@@nzzzzzzx##@@@@@##@@@WWWMnxWxxiiiii#x;..,,,,::ixz*iii;ii*#nznnxxxMxxnzznnnxxxxnnzz##zznznx#++**++++**ii;;::::::::::::;;i;:,,,,,,,,:i++++#zzz
@@@@@@Wnx@xnzzzzzzW##@@@WW@W@WxxWWxWWMWMn*iiii#*,,,::,:::zniiii****+zzznxxxMxxz++znnnxMxnznz##+#zznnx++**++++**ii;;;;;::::::::::;;;,,,::::,,i**++++#zn
@@@@@@WWWxnnnzzz#n@@#@@@WWWWW*;*WW@MW@WMMn+iiii#;,,:::,::ix+**+****+###zxxxMxx#*+++znnxMxnzz#+++#zzznn*********iii;;;;;:::::::::::::,::;;:,:***++++++z
@@@#@@WWWnnnnnznxW@@@@@@@WMWx::nWW@@WxMMW@n+i****:,,::,,:;#z**+**+**+###zxxMxx#*++++znxxxxnz####*+##zn#***ii**iiii;;;;;;::::::::::::::;;;+i+**++**+##+
@@@#@@@WMnnnnnzzW@WW@@@@@WWWM:#@WW**n@z##W@x#*ii*;,,:::,,:*z**++++++++#+#nMMMxz******zxxxxnzzz##++#z#zn#*iiii*iiii;;;;;;;::::::::::::iii+++*i*****+##z
@@@@@@@@WxnnnnzM@WWW@@@@WWWWM;;WWM;;;xM#;z@@Mz+*+i:,,::,,::*#+++++++++###znMMxn*******nxxxxnzz#+i+###zzxz*iiiiii;;;;;;;;;:::,,,,,::;ii*++**ii******+zz
@@@#@#@@WWnzznW@@WWW@@@@WWWWM+ixWW#+*zWxi*W@Mxx+#+;:,:,,,,::++++++#++####zzxMxxii*****#xxxxnnz+;:::*##zzxziii;;;:;;;:::::::,,,,,:;;;i*+++**ii+*****+#z
@@@@@##@@WxzM@@@@WWW@W@WW@WWMxiin@n#+z#x++@@@WWWxM*::,::,,,:i*+++++########nMMM*ii****inxxxxnz+:::,,+##zzx#;;i;;::::::::,,,,,,,:;;;;i**+#+*ii++****++#
@@@@@##@@@MW@@@@WWWWW@@W@@WWWM**+@n+###n#M@@@@@MxxMi:,:::,,:;i++++#########zMMM*ii****i+nnxxxnz::,,,:*+#znx+;;;:::,,,,,,,,,,,,,:;;;;**+##+***#++***##+
@@@@##@@@@WM@@WWWWWWWWWWWWWWWW#zzxWMn#zzz@@MWWWxxnWx*:::::,,:;*+++#########zxMM+ii*****iz*#xnnz*::,,,,;+#zxn;::::::::,,:::,,,,:;;;i*++###++*+##++**###
@@@@@##@@@@MMWWWMMWWM#*+MWWWWMnzznnznzz#M@x##xWzzW#nx;;;;:,,::i+++#########zxMx*iii**iii+;:zzzzz;:,,,..:#znx+::,:::::::::::::;;;;iii+x#z#+++#+##+++###
@@@@@@@@@@@@MWWMMMWMz+#+zWWWWMnnnnnnnzz#MWz###nM+nW#+i;;;;:,:;i*++++#+##+++#nMni;iiiiiiii:,;#zzz*,,,,,,,:#nxn;,::::::::;:::::;;;;ii:+Mnzz+++z###+#####
@@@@@@@@@@@@@xMMMMMxzzzz#WWWWMnnnnnnnnzzn@xzzzzWn#zx*ii;;;;:,;;*+++++++++**+nx#ii;iiiii;;,,,*+##+:,,,,,,,iznx+::::::::::::::::;;iiii+MMnz+++##zz######
@@@@@@@@@@@@@WxxxMMnnzzzn@@W@MxxxxxnxnnzzMMxzzzxMz#n**i;;;;:,:;;*+**********zx*ii;;iii;;::::::+#+i,,,,,:::*znn:::::::::;;:::::::iiiizxxxz###z#z#######
@@@@@@@@@@@@@@MxMMnzzznxWW@WWxxxxxxxxxnnnnnnnznnMzz#+*iii;;;:,;:;********iiizniiii;ii;;::::::,:++*:::::::::#nx*:::::::i#n*:::::;;i*#nxxnzzzzzzz###z###
W@@@@@@@@@@@@@@MxnnnnnxWWWWWMxxxxxxxxnnnnnnnnznznzzzz+i;;i;;:,:::i*iiiiii;;;#z;;ii;;;:::::::::,i#+i::::::::;zxn::::::,:+n;:::*;;;i*+nxMnzzzzznzzz#z###
MW@@@@@@@@@@@@@@xnnnnMWWWWxnnnnnnnnnnnnnnnznnzzzzzzz#+*;;;;;:,,::;*iiii;;;::z+;;;::,,:,,,,,,,,,:+#+:::::::::inx*:::::,:#n;;;;+i;;i+#nxxMzznzznnzzzzzzz
WzWWW@@@W@@@@@@@@xnnnxWWWWxnnnnnnnnzznnnnznnzzznzzz#++*;::;;;:,,:;i;;;;:::,:zi:::,,,,,,,,,,,,,,:;##;:::::::::*xz:::;;;:+n;;;;*+;i*+#nxxMnznzznnnzzzz#z
@zMMWW@@WW@@@@@@#@MMMxxMWWMxnnnnnnzzznnnnnnzzzzzz##+#+*iiii;:,.,:;:;:::::::i#::::,,,,:::::::::,::+#*:i::::::::#x;:;;;;:#n;;;i+n++###nxxMxnnnznxnzzzzzz
@WMMMWWWW@@@@@@@@#WMWxxxxMWMxnnnnnzzzznnnnnzzzz##++++++**;::;;;;;;::;:::;;:*;:::::::::::::::;;:::*##::;:::::::;n+;:;;;:#ni;*+zn+#z#znxxxnnzznnnxxnzzzn
@WWWWWWMW@@@@@@@@@#WWMnxnnMMxnnnnnnznnnnzzzzzz##+++*#nz*iiiii;:....,::;;;;;;:::::;;:::;;;;;;;;:::;#z:::::::::;;*n;:::;:#n#zn#znnnzznzxnxnnxxxxxMMxnnzn
@@WWWWWMMW@@W@@@@@@#@WzzzznMMMxnnnnnnzzzzzzznz##+++znz***++i:,...,:;;;;;;;i;::::;;i;ii;i;;;;;;::::*z;::::;iiii;;#*::i;:#nn+*##nxxxxxnnnxnnzMWWWWWWMxMM
@@WWWMWWWW@@@@@@@@@##@Mz#++xMMMxnnnzzzzzzz#zxz##+#nx#*#zz*;,,:i***+++**ii**i;::;i;iiiiiiii;;;:::::izi::ii***ii;iizi+#*;#nn+*##nxxxxxnnnMxz#nMWWWWWWMMM
W@WWMnWWWWW@@@WW@@@@#@@Wn#+nxxMMMx#########nxz##nnx+*znz*;i*######+iiiiii**i;;;;i;iii;;;;;;;;;;;;::#*::iiiiiii*zznznnz;znn+###nxxxxnznxMx#nnxWWMMMxxMW
@WWMxzM@WWWW@@@@WWW@@#@@@n+#xMxMMMn#######nxMxnnnnz#zzz#znnnnnxxnnn*iiii**ii;;;;n*;;;;;;;ii;;;;;;;;++;iiiiiii*+###znnziznxnn#zxxMMxnzznMMxnnxWMMxxxMMW
@@@xnzn@@@@WW@@WWMxW@@#@@@MzxxnnMMxn#++++nxxxxnnnzznnxxMxxnz####znx#iiii*iiiii;ix+ii;;;;;*****ii*ii*#iiiii;;:i**++##zz+znxxxzzxMMxxxzxnMMMWxxxxxxMxMW@
@@@MnzzW@@@@W@@WWzzx@@@##@@WMMxzxxnx##+#xxxxnnxxxxxxxnz##+++******zx*iiiiiiiiii#MM#;;;;;;iiiiiii;iii#i;;;::::;i**++#nzznnxxxnnxxxxxxnnnxnnxxxxMMMMWWWW
@@@Wn##M@@@@@@@WMznW@@@@@###@Mxzxxznz#zxxxxnxxxxxn#+++++++++*******z+iiiii*iiiixMW@+i;;;;;;;;i;;;ii;*;;:;;;;;*i**++#znznxxxnznznz########xxxMMMMMWW@WM
W@@@M##x@@@@@@@WxzzxW@@@@@#@@@Wxnxzznxxxxxxxxnz##z#zz#++++++++*****#+;;;ii*i*+zWWMWM+ii;;;;;;iiiiii;*ii;iii*n#*++##zzzznnz+++++**++++++#nMxMMMMMW@WMMM
x@@@@zzzM@@@@@@@Mzzz#znM@@@@@@@@Mnznxxxxxxzz#+*****+++++++++++**ii*#*iiii;;;**+WWMMWWWMMn#++#####++**iiii**#z#++######z#+***ii*+++####znMMMMMMMWWWMMMW
zW@@@MnzznM@@@@@@zz#####+zM@@@@@@Wxxnnnzz++++++**++++++++++++**ii*##**i;;:::::#WWzi+#xWWWxnnnnnnnnzz#+***#####++++*****iiiii*+#zznnnnnnMMMMMMMWMMMMMWW
+x@@@WWMxxnM@@@@@M##+++++++#M@@@@@@Wn#+++++++++++++**++++#++++++++*ii;;:i::::;xWWz:;;iz*+i*+#nnnnnznnz####+++****iii*iii**+##znnnnnznnxMMMMMMMMMMMMMWW
*#MW@@MWWWWnx@@@@@M###+++##zzxW@@@@@@x##++#++++****+++*++***iiii;;;;:::i:::::*xnMx*;;;;::;i**nxxxnznxxn+***iiii;;i**+###zzzzzz#####zznMMMMMMMMMMMMMWW@
**+nW@WMWWWxnx@@@@@MzzzznnnnnnnznW@@@#Wz++++******+****+***ii;;;;:;;;:i;:::::inxMMWM#;::::i*iznnxnnzz#*i;:;;;i**+##zznzzzz#########znMMMMMMMMMMMMWWWW@
i**+z@@MMWWWWWW@@@@@MMMMxxxxz#***+n@@@@@M+********+*******ii;;;;;;#znzn#i::::;nxMMWWWWn*i*i*+nnz##+*i;;;**+++++######zzznnnnxxxxxxxxxMMMMMMMMMMWWWWW@@
ii***n@WMMWWWWWW@#@@@WMMxn#********+nW@#@@M+**#+*iiiiii*iiiii;;;i#zxxxzxx+ii#nxxMWWWW@WW@@x#+##++++++*++#++++++####znxxxxMxxxxMxxxxxMMMMMMMMMWWWWWWW@@
#+***+x@nMMMMMMMW@@@@@M#+************+n@@@@@n*i**iii;;;*ii*ii;i*znnxxMxMWxznnnnxMMMWWW@@@WWWMzz#zz####+######zznnxxxxxxxxxxxxxxxxxxMMMMMMMMMWWWWWWW@@@
nnn#+++nM#zzzznzzzM@@@@n+******iiii****#M@@@@Wziii;iii*+++###zznnxxxMMMWWMxMxxxxMMMMMWW@@WWWWMMxxxnnnnnnxxxMMMMMWMWWWWWWWWWWWWWW@WMMMMMMMMWWWWWWWWW@@@
nnnnnz#+Wz+#####+##x@@WWx****iiiii**+##**nW@@Wn#*****#zzzznnnxMMxxxMMMMMMMWMMWMMMWMMMWWWWWWWWMMMMxxxMMMMWWWWWWWWWWWWWWWWMMWWW@@@@MMMMMMMMWWWWWWWWWW@@@
xnnxnnzzxM+*++++++++nW@WWn****ii******++#++#x@@MnnznxxxxxxxxMMMxxMMMMMMMWMMMMMMWWWWWWWWWWWWWWMMMMMMxxxMMMMMMMMWWWWWWWWWWW@@@@@@@MMMMMMMWWWWWWWWWWWW@W@
MMxxxxnnnWMnz#++*****zWWWMn+i**i**#znnnnxnzznxW@@WMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMWWWWWWWWW@@@@@MMMMMMMWWWWWWWWWWWWWWW@
xxxxMMxxnMWMMMMxnz##++n@@WWxz###zxMMMxxxxMMMMMMM@@WWMMMMMWWWWWWMMWWMWWMWWWWWWWWWWWWW@WWWWWMMMMMMWWMMMMMMMMMMMMMMMMMMWWWWWWW@@WMMMMMMWWWWWWWWWWWWWWW@@@
""")
else:
    print("Incorrect Password")

          
