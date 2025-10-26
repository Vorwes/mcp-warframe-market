# Description
This repository contains an mcp server implementation for [warframe market](https://warframe.market/) using [pywmapi](https://github.com/leonardodalinky/pywmapi). Currently, it only supports placing buy/sell orders.

## Instructions
1. Clone the repository:
```bash
git clone 
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory with your warframe market credentials:
```text
EMAIL=your_email
PASSWORD=your_password
```

4. Add this command to your mcp config file to run the server:
```json
"warframe-market": {
    "command": "python",
    "args": ["-m", "src.server"],
    "cwd": "PATH/TO/REPO"
}
```

## Example Usage
```text
Create an order for Kronen Prime Blade, make it not visible and its a sell type of order, the asking 
price is 1000 platinum
```

## TODO
- [ ] Add support for fetching orders
