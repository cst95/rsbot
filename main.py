import pyautogui
import win32gui


#print(pyautogui.position())
#print("Hello")

#print(pyautogui.size())


#max_x = pyautogui.size().width
#max_y = pyautogui.size().height

#print(max_x)


#pag.moveTo(max_x, max_y, 10)
#print(pyautogui.screenshot('test.pngn))

def callback(hwnd, extra):
	print(win32gui.GetWindowText(hwnd))

	print(win32gui.GetWindowRect(hwnd))


def find_window_coords(username):
	window_name = f'RuneLite - {username}'
	try:
		window_id = win32gui.FindWindow(None, window_name)
	except:
		print('')
		return None

	return win32gui.GetWindowRect(window_id)




def main():
	username = 'RumbIe'
	print(find_window_coords(username))

    



if __name__ == '__main__':
    main()
