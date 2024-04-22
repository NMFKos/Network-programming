using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Login_Register
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection conn = new SqlConnection("Data Source = DUONGDAT, Initial Catalog = PONG; Integrated Security=SSPI");
            try
            {
                conn.Open();
                string account = textBox1.Text;
                string password = textBox2.Text;
                string email = textBox3.Text;
                Random rnd = new Random();
                int id_user = rnd.Next(1,99);
                string user_name = textBox4.Text;

                string sql = "insert into USERS(id_user, Tên_đăng_nhập, Mật khẩu, Email, Tên_người_dùng) values ('" + id_user + "', '" + account + "', '" + password + "', '" + email + "' ,'" + user_name + "')";
                SqlCommand cmd = new SqlCommand(sql, conn);
                cmd.Connection.Open();
                if (cmd.ExecuteNonQuery() > 0)
                    Console.WriteLine("Đăng ký thành công");
                else
                    Console.WriteLine("Đăng ký thất bại");


            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi kết nối");
            }
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {

        }
    }
}
