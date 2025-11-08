import ferramenta
import time
while True:
	try:
		print("\033[0;33;40mPara parar use Ctrl + c \033[0;0m")
		ferramenta.temperatura()
		time.sleep(1)
		ferramenta.clear()
	except:
		break
