# 💧 Water Reminder Application

A Python desktop application that monitors your focus and reminds you to stay hydrated! Perfect for developers, students, and anyone who spends long hours at their computer.

## 🌟 Features

- **🎯 Activity Monitoring**: Tracks keyboard and mouse movements to detect focus periods
- **⏰ Smart Reminders**: Sends desktop notifications after 2 minutes of continuous focus
- **💡 Fun Facts**: Displays motivational hydration facts with each reminder
- **📊 Activity Logging**: Keeps a log of all water break reminders
- **📈 Daily Summary**: Shows total reminders sent each day
- **🖥️ Simple GUI**: Clean interface displaying last reminder time

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.7 or higher installed
- pip (Python package installer)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/water-reminder.git
cd water-reminder
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

## 📦 Dependencies

- `pynput` - For monitoring keyboard and mouse activity
- `plyer` - For cross-platform desktop notifications
- `tkinter` - For GUI (usually comes with Python)

## 🎮 How It Works

1. **Start the Application**: Run `main.py` to launch the water reminder
2. **Work as Usual**: The app runs in the background monitoring your activity
3. **Get Reminded**: After 2 minutes of focus, you'll receive a notification with a fun hydration fact
4. **Stay Hydrated**: Take a water break and return to work refreshed!

## 📁 Project Structure

```
water-reminder/
│
├── main.py              # Main application code
├── Fun_Facts.txt        # Motivational hydration facts
├── reminder_log.txt     # Log of all reminders (auto-generated)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## ⚙️ Configuration

You can modify the focus threshold in `main.py`:

```python
FOCUS_THRESHOLD = 2 * 60  # Change this value (in seconds)
```

**Examples:**
- `5 * 60` = 5 minutes
- `10 * 60` = 10 minutes
- `30 * 60` = 30 minutes

## 📝 Customization

### Adding Your Own Fun Facts

Edit `Fun_Facts.txt` and add your own motivational messages, one per line:

```
Your custom hydration reminder here!
Another fun fact about water!
```

### Viewing Reminder History

Check `reminder_log.txt` to see all your past water break reminders with timestamps.

## 🖥️ Platform Support

- ✅ **Windows**: Fully supported
- ✅ **macOS**: Fully supported
- ✅ **Linux**: Supported (may require additional setup for notifications)

### Linux Note

On Linux, you might need to install additional packages:

```bash
sudo apt-get install python3-tk
sudo apt-get install libnotify-bin
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💡 Future Enhancements

- [ ] Customizable reminder intervals via GUI
- [ ] Sound alerts option
- [ ] Water intake tracking
- [ ] Configurable notification messages
- [ ] Statistics dashboard
- [ ] System tray icon
- [ ] Snooze functionality

## 🐛 Known Issues

- The application needs to remain running to send reminders
- Initial notification might take 2 minutes + 10 seconds to appear

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)

## 🙏 Acknowledgments

- Built with Python and love ❤️
- Inspired by the need to stay healthy while coding
- Thanks to all contributors who help improve this project

## 📧 Contact

Have questions or suggestions? Feel free to:
- Open an issue on GitHub
- Reach out via [your-email@example.com]

---

**Remember**: Stay hydrated, stay productive! 💧✨
