This is a wrapper python script for Xiaomi Mi Band 3 and Mi Band 4 utilizing existing python libraries by [Yogesh Ojha](https://github.com/yogeshojha/MiBand3) for Mi Band 3 and [Satkar Dhakal](https://github.com/satcar77/miband4) for Mi Band 4.

The script has additional feature to demonstrate a DoS attack by jamming the BLE advertising channel constantly sending connection requests and quering for a specific characteristic.

Installation steps:

### Install dependencies

The script requires python 2.7 and python 3 libraries
`pip install -r requirements.txt`

### Connection to MiBand

Turn on your Bluetooth

Unpair you Mi Band from current mobile apps

Find out your Mi Band MAC address

```sudo hcitool -i hci0 lescan```

Run this to perform authentication with Mi Band 3

```python3 main.py -m 3 -mac C3:66:88:8F:4D:85```

Run this to perform authentication with Mi Band 4. 
Note: some features will not work until authkey is provided. For more information check the guide for [Mi Band 4](https://github.com/satcar77/miband4)

```python3 main.py -m 4 -mac C3:66:88:8F:4D:85```

or

```python3 main.py -m 4 -mac C3:66:88:8F:4D:85 -k 8fa9b42078627a654d22beff985655db```

Run this to perform a DoS attack by jamming the BLE advertising channel on Mi Band 3. This also works for Mi Band 4. 

```python3 main.py -m 3 -mac C3:66:88:8F:4D:85 -j```

To check all available options

```python3 main.py -h```

If you having problems(BLE can glitch sometimes)

```sudo hciconfig hci0 reset```