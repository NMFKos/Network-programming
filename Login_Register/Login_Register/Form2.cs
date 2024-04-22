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
using static System.Net.Mime.MediaTypeNames;

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
            SqlConnection conn = new SqlConnection("Data Source=MSI;Initial Catalog=PONG;Integrated Security=True");
            string account = textBox1.Text;
            string password = textBox2.Text;
            string email = textBox3.Text;
            Random rnd = new Random();
            int id_user = rnd.Next(1, 99);
            string user_name = textBox4.Text;

            string sql = "insert into USERS(ID_user, Tên_đăng_nhập, Mật_khẩu, Email, Tên_người_dùng) values (@id_user, @Tên_đăng_nhập, @Mật_khẩu, @Email, @Tên_người_dùng)";
            try
            {
                conn.Open();
                SqlCommand cmd = new SqlCommand(sql, conn);
                cmd.Parameters.AddWithValue("@id_user", id_user);
                cmd.Parameters.AddWithValue("@Tên_đăng_nhập", account);
                cmd.Parameters.AddWithValue("@Mật_khẩu", password);
                cmd.Parameters.AddWithValue("@Email", email);
                cmd.Parameters.AddWithValue("@Tên_người_dùng", user_name);

                if (cmd.ExecuteNonQuery() > 0)
                    MessageBox.Show("Đăng ký thành công");
                else
                    MessageBox.Show("Đăng ký thất bại");
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
