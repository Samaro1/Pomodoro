Pomodoro Technique Application

📌 About

This is a Pomodoro Timer Application built using Python and Tkinter. It follows the Pomodoro Technique, which helps improve focus and productivity by using timed work sessions followed by short and long breaks.

🎯 Features

- Start and reset the timer

- Customizable work and break durations

- Automatic cycle through work and break sessions

- Visual indicators for work and break periods
 
- Checkmarks to track completed work sessions

🛠 Technologies Used

- Python

- Tkinter (for GUI development)

- Math module (for handling time calculations)

⚙️ How It Works

Click Start to begin a Pomodoro session.

After 25 minutes of work (default), a 5-minute short break starts.

Every 4 work sessions, a long 20-minute break occurs.

After each work session, a green checkmark ✔ is added as progress.

Click Reset to stop and restart the timer.

📝 Customization

To change the work/break durations, modify these values in main.py:

WORK_MIN = 25  # Work duration in minutes
SHORT_BREAK_MIN = 5  # Short break duration
LONG_BREAK_MIN = 20  # Long break duration

🏗 Future Enhancements

- Sound alerts for session transitions

- Dark mode option

- Task list integration

- Make the time duration be user defined
  
-  Data tracking for completed Pomodoros

🤝 Contributing

Pull requests are welcome! If you’d like to improve the project, feel free to fork and submit a PR.
