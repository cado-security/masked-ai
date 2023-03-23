# Run with ./release/generate_linux_binary.sh
pip3 install -r requirements.txt
pyinstaller  --onefile --clean masked_ai/masker.py