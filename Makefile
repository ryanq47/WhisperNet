compile:
	#rm -rf ../logec_attack_compile
	#cp ../logec_attack ../logec_attack_compile -r
	#cd ../logec_attack_compile

	#rm -rf Beta_Tests
	#rm -rf logec-attack.bin
	nuitka3 logec-attack.py --standalone --onefile --plugin-enable=pyside6 --follow-imports --nofollow-import-to=tkinter --lto=yes


gui:
	/home/kali/.local/bin/pyside6-uic gui.ui > gui.py 
