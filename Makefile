compile:
	#rm -rf ../logec_attack_compile
	#cp ../logec_attack ../logec_attack_compile -r
	#cd ../logec_attack_compile

	#rm -rf Beta_Tests
	#rm -rf logec-attack.bin
	nuitka3 logec-attack.py --standalone --onefile --plugin-enable=pyside6 --follow-imports --nofollow-import-to=tkinter --lto=yes --remove-output --output-filename=logec-suite
	
	rm -rf Gui Dev Documentation requirements.txt venv logec-attack.py gui.py gui.ui  Modules/General/ScriptGen/ Modules/General/SysShell/ Modules/General/utility.py Modules/General/savefiles/fileops.py Modules/Wrappers/CompilationWrapper.py agent/friendly_client.py

gui:
	/home/kali/PycharmProjects/logec-suite/venv/bin/pyside6-uic gui.ui > gui.py 

dev:
	pip install -r requirements.txt
	pip install pyqt5-tools

clean:
	echo "" > logs/bruteforce.log
	echo "" > logs/logec-main.log
req:
	pipreqs ./ --force

venv:
	echo "run: source logec-suite/bin/activate"
	
install:
	pip install -r requirements.txt
