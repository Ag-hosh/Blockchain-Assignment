# Blockchain-based Charity Donation Platform

Welcome to the Blockchain-based Charity Donation Platform project! This open-source initiative aims to revolutionize the way charitable contributions are made and tracked by leveraging the power of blockchain technology.

**Important note**

   This works with SepoliaETH, eth and all the types of etharium blockchain refer to  web3.js documentation for more details.

## Project Overview

In a world where transparency and accountability are paramount, our platform seeks to provide a secure and immutable way to facilitate charitable donations. With the blockchain as its foundation, our system ensures that every donation is traceable, tamper-proof, and easily auditable.

## Key Features

- **Transparent Transactions**: Using blockchain's decentralized ledger, all donation transactions are publicly recorded and can be verified by anyone, ensuring the integrity of the process.

- **Smart Contracts**: We implement smart contracts to automate donation execution, ensuring funds reach their intended beneficiaries without intermediaries.

- **User-Friendly Interface**: Our user interface is designed with simplicity in mind, making it easy for donors to contribute and charities to manage their funds.

- **Real-time Tracking**: Donors can track the progress of their contributions in real-time, fostering trust and transparency in the charity sector.

- **Security**: Robust security measures are in place to protect user data and financial information, while blockchain's encryption ensures the safety of transactions.

## Installation and Setup

1. Clone the repository:
git clone https://github.com/Ag-hosh/Blockchain-Assignment.git
2. Open app.py
3. Install all dependencies using `pip install -r requirements.txt`
4. To run the server type `./run.sh`
    Note: this only works on windows please create a batch file for linux(code is same for both)
5. Open http://localhost:5000 and display the webpage

## Technology Stack

- **Flask** - Flask is a lightweight web framework written in Python. It is utilized for building the web application and managing routing.
- **HTML** - HTML (Hypertext Markup Language) is the standardized markup language for establishing the structure and content of web pages. It is employed for defining the user interface of the application.
- **JavaScript** - JavaScript is a programming language that enables interactivity and dynamic functionality in web pages. In the Payment APP, it handles user actions, interacts with the Ethereum blockchain via web3.js, and manipulates the DOM (Document Object Model).
- **web3.js** - web3.js is a JavaScript library that offers an interface for interacting with the Ethereum blockchain. It plays a role in the Payment APP by connecting to MetaMask, retrieving wallet balances, and executing transactions.
- **CSS** - CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation and styling of an HTML document. It is used in the Payment APP to style the user interface elements.
- **MetaMask** - MetaMask is a browser extension that enables users to manage Ethereum wallets and interact with Ethereum-based applications. It is employed in the Payment APP to establish a connection to the user's wallet and facilitate transactions.
- **lottie-player.js** - lottie-player.js is a JavaScript library for rendering animations using Lottie files. It is utilized in the Payment APP to display animations within the transaction details popup.



## File Structure
The relevant files and their descriptions in the project are as follows:

-**run.sh**:this is the windows batch file to start the flask server.
- **app.py**: The main Flask application file that handles routing and serves the web pages.
- **templates/index.html**: The HTML file containing the user interface and JavaScript code for the Payment APP.
- **templates/contact.html**: The HTML file that provides the contact information and form for user inquiries.
- **templates/about.html**: The HTML file that presents information about the project or organization, including its mission, team, and goals.
- **templates/home.html**: The HTML file serving as the main homepage of the website, showcasing essential content and navigation elements for users.


## Usage

The Payment webpage provides the following functionalities:

- ***Connect Wallet***: Allows users to connect their wallets with MetaMask.

- ***Get Balance of Wallet***: Retrieves and displays the balance of the connected wallet.

- ***Transfer Funds***: Enables users to transfer funds to another Ethereum address. Users need to enter the recipient's address and the transfer amount. Upon successful transfer, a transaction details popup will be displayed with the transaction amount and ID.


