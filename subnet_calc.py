from tkinter import *
from tkinter import ttk
from ipaddress import ip_network, ip_address
from tkinter import messagebox

window = Tk()
window.title("Calculate IP addresses")

frame1 = Frame(window)
frame1.grid(row=0, column=0)

LblSubnet = Label(frame1, text="Subnet:")
LblSubnet.grid(row=0, column=0)

txtSubnet = Entry(frame1, width=20)
txtSubnet.insert(0, "192.168.2.0/24")
txtSubnet.grid(row=0, column=1)

btnCalculate = ttk.Button(
    frame1, text="Calculate")
btnCalculate.grid(row=0, column=2)

frame2 = Frame(window)
frame2.grid(row=1, column=0)

LblSubnet2 = Label(frame2, text="Subnet without Prefix:")
LblSubnet2.grid(row=0, column=0)

txtSubnet2 = Entry(frame2, width=20)
txtSubnet2.insert(0, "192.168.2.0")
txtSubnet2.grid(row=0, column=1)

choices=['128.0.0.0',
'192.0.0.0',
'224.0.0.0',
'240.0.0.0',
'248.0.0.0',
'252.0.0.0',
'254.0.0.0',
'255.0.0.0',
'255.128.0.0',
'255.192.0.0',
'255.224.0.0',
'255.240.0.0',
'255.248.0.0',
'255.252.0.0',
'255.254.0.0',
'255.255.0.0',
'255.255.128.0',
'255.255.192.0',
'255.255.224.0',
'255.255.240.0',
'255.255.248.0',
'255.255.252.0',
'255.255.254.0',
'255.255.255.0',
'255.255.255.128',
'255.255.255.192',
'255.255.255.224',
'255.255.255.240',
'255.255.255.248',
'255.255.255.252',
'255.255.255.254',
'255.255.255.255']

cbMask = ttk.Combobox(frame2, values=choices)
cbMask.current(23)
cbMask.grid(row=0, column=2)

text = Text(window, width=80, height=30)
text.grid(row=2, column=0)

def calculate():
    text.delete(1.0, END)
    subnet = txtSubnet.get()
    try:
        subnet = ip_network(subnet)
    except:
        return messagebox.showinfo("Info", "Not valid IP address subnet")
    ip_list = list(subnet.hosts())
    first_host = ip_list[0]
    last_host = ip_list[-1]
    broadcast_ip = subnet.broadcast_address
    hostmask = subnet.hostmask
    netmask = subnet.netmask
    prefix_len = subnet.prefixlen
    num_addresses = subnet.num_addresses
    # print(ip_network(subnet).with_prefixlen)
    # print(ip_network(subnet).with_netmask)
    # print(ip_network(subnet).with_hostmask)

    text.insert(END, first_host)
    text.insert(END,'\n')
    text.insert(END, last_host)
    text.insert(END,'\n')
    text.insert(END, netmask)
    text.insert(END,'\n')
    text.insert(END, hostmask)
    text.insert(END,'\n')
    text.insert(END, prefix_len)
    text.insert(END,'\n')
    text.insert(END, num_addresses)
    text.insert(END,'\n')

btnCalculate.config(command=calculate)

def updateEntry(event):
    #txtSubnet.configure(text= cbMask.get())
    txtSubnet.delete(0, END) #deletes the current value
    txtSubnet.insert(0, ip_network(txtSubnet2.get()+"/"+cbMask.get())) #inserts new value assigned by 2nd parameter


cbMask.bind('<<ComboboxSelected>>', updateEntry)

window.mainloop()