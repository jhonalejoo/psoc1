# from tkinter import *  # Carga módulo tk (widgets estándar)
# from tkinter import ttk
# import serial
# import serial.tools.list_ports
# import time
#
# class Aplication():
#
#     def __init__(self):
#         self.raiz = Tk()
#         self.raiz.geometry('300x200')  # anchura x altura
#         self.raiz.configure(bg='beige')
#         self.raiz.title('Aplicación')
#         self.mensa = StringVar()
#         self.etiq3 = Label(self.raiz,textvariable=self.mensa)
#         self.etiq3.pack(side=TOP)
#         self.bserial = ttk.Button(self.raiz, text='Potenciometro', command=self.serial)
#         self.bserial.pack(side=LEFT)
#         self.bsalir = ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy)
#         self.bsalir.pack(side=RIGHT)
#         self.raiz.mainloop()
#
#
#     def serial(self):
#         contador = 0
#         try:
#             print(serial.Serial('COM8'))
#             Puerto = serial.Serial('COM8', 9600, bytesize=8, parity='N', timeout=1)
#             print(Puerto.readline())
#             # while True:
#             #     if Puerto.in_waiting() > 0:
#             #         data_str = Puerto.read(Puerto.inWaiting()).decode('ascii')
#             #         print(data_str, end='')
#             #     time.sleep(0.01)
#                     #self.mensa.set(Puerto.readline().decode())
#         except IOError:
#             Puerto.close()
#             print('Verifique el puerto COM')
#
#
# def main():
#     mi_app = Aplication()
#     return 0
#
#
# if __name__ == '__main__':
#     global Puerto
#     main()

import threading
import serial

connecte = False
port = 'COM8'
baud = 9600

serial_port = serial.Serial(port, baud, timeout=0)


def handle_data(data):
    print(data)


def read_from_port(ser):

    while not connecte:
        # serin = ser.read()
        connected = True

        while True:
            #print("test")
            taxto='a'
            ser.write(taxto.encode('ascii'))
            reading = ser.readline()
            handle_data(reading)


thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()
