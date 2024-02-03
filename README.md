# Decod3wizard

**Decod3wizard** is a Python script that simplifies the process of identifying and decoding various hashes and encodings. Whether you're dealing with cryptographic hashes, Base64 encoding, URL encoding, or even more complex schemes like ROT13 or hexadecimal encoding, Decod3wizard can handle it all. You can use it in single mode for quick identification and decoding or enter the world of magic mode for continuous, recursive decoding.

![Decod3Wizard](/images/1.png)


## Features

- Identify and decode a wide range of hash types and encoding schemes.
- Choose between single mode and magic mode for different use cases.
- Automatically continues to decode until a final readable value is found.

## Demo Output
![Decod3Wizard](/images/4.png)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MrNeoTr1n0/Decod3wizard.git
   ```

2. Install the required dependencies:

   ```bash
   pip install prettytable
   ```

## Usage

To run Decod3wizard, execute the `decod3wizard.py` script:

```bash
python decod3wizard.py
```

## Modes

Decod3wizard operates in two modes:

1. **Single Mode:** Use this mode to identify and decode a single hash or encoded value.

2. **Magic Mode:** Enter the world of magic mode to continuously decode a value until a final readable result is found.

## Examples

### Single Mode

In Single Mode, simply enter the hash or encoded value, and Decod3wizard will identify and decode it. If a readable value is found, it will be displayed.

```bash
Enter the hash or encoded value: <your_value>
```

![Decod3Wizard](/images/2.png)

### Magic Mode

In Magic Mode, the script will continuously decode the value you provide, attempting to find the final readable result.

```bash
Enter the hash or encoded value: <your_value>
```

![Decod3Wizard](/images/3.png)

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or additional features you'd like to see in Decod3wizard.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.
