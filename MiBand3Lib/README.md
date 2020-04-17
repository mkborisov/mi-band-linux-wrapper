# MiBand3
Library to work with Xiaomi MiBand 3

Base lib provided by Leo Soares
Additional debug & fixes was made by Volodymyr Shymanskyy

# Run

### Install dependencies



`pip install -r requirements.txt`

### Using python 3

If you're having python 3.x just use following codes to automatically convert files:

`2to3 -w main.py`
`2to3 -w auth.py`

### Connection to MiBand

Turn on your Bluetooth

Unpair you MiBand2 from current mobile apps

Find out your MiBand3 MAC address

```sudo hcitool lescan```

Run this to auth device

```python main.py MAC_ADDRESS --init```

If you having problems(BLE can glitch sometimes)

```sudo hciconfig hci0 reset```

### If you have trouble installing bluepy

```sudo apt-get install libglib2-dev  ```
