#!/bin/bash
# Jenkins Agent Setup Script for Test Automation

echo "Setting up Jenkins agent for test automation..."

# Update system
sudo apt-get update

# Install Python 3 and pip
sudo apt-get install -y python3 python3-pip python3-venv

# Install Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install -y google-chrome-stable

# Install ChromeDriver
CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# Install Git
sudo apt-get install -y git

# Set display for headless Chrome
export DISPLAY=:99

echo "Jenkins agent setup completed!"
echo "Chrome version: $(google-chrome --version)"
echo "ChromeDriver version: $(chromedriver --version)"
echo "Python version: $(python3 --version)"