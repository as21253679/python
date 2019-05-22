using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace test
{
    /// <summary>
    /// MainWindow.xaml 的互動邏輯
    /// </summary>
    public partial class MainWindow : Window
    {
        DateTime current, before;
        public SerialPort serialPort;//串口对象类
        public MainWindow()
        {
            InitializeComponent();
            InitCOM("COM9");
        }

        DispatcherTimer _timer = new DispatcherTimer();
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            _timer.Interval = TimeSpan.FromMilliseconds(10);
            _timer.Tick += _timer_Tick;
            _timer.Start();
        }

        //開始計時
        void _timer_Tick(object sender, EventArgs e)
        {
            before = current;
            current = DateTime.Now;//計時結束 取得目前時間
            string result2 = ((TimeSpan)(current - before)).TotalMilliseconds.ToString();

            SendCommand("1234567");//发送字符
            SendCommand("12345678");//发送字符
            SendCommand("1234567");//发送字符
            SendCommand("1234567");//发送字符

            Debug.WriteLine(result2);
        }
        
        /// 串口接收通信配置方法
        /// 端口名称
        public bool InitCOM(string PortName)
        {
            serialPort = new SerialPort(PortName, 9600, Parity.None, 8, StopBits.One);
            serialPort.RtsEnable = true;
            return OpenPort();//串口打开
        }
        //打开串口的方法
        public bool OpenPort()
        {
            try//这里写成异常处理的形式以免串口打不开程序崩溃
            {
                serialPort.Open();
            }
            catch { }
            if (serialPort.IsOpen)
            {
                return true;
            }
            else
            {
                MessageBox.Show("串口打开失败!");
                return false;
            }
        }
        //向串口发送数据
        public void SendCommand(string CommandString)
        {
            byte[] WriteBuffer = Encoding.ASCII.GetBytes(CommandString);
            serialPort.Write(WriteBuffer, 0, WriteBuffer.Length);
        }
    }
}
