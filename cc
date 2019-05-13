public MainWindow()
        {
            InitializeComponent();
        }
        DispatcherTimer timer1 = new DispatcherTimer();
        private void start(object sender, RoutedEventArgs e)
        {
            timer1.Tick += new EventHandler(timer1_Tick);
            timer1.Interval = TimeSpan.FromSeconds(0.01);
            timer1.Start();
        }
        private void stop(object sender, RoutedEventArgs e)
        {
            timer1.Stop();
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime time_start = DateTime.Now;//計時開始 取得目前時間
            Debug.WriteLine(time_start.Millisecond);
        }

        private Timer MotionTimer;
        private void ListenMotionStatus()
        {
            new Thread(() => {
                MotionTimer?.Dispose();
                MotionTimer = new Timer(
                    (state) => {
                        DateTime time_start = DateTime.Now;//計時開始 取得目前時間
                        Debug.WriteLine(time_start.Millisecond);
                    }, this, 0, 10);
            }).Start();
        }
