using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace Login_Register
{
    public partial class Pong : Form
    {
        public Pong()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Form form2 = new Form();
            form2.Show();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection conn = new SqlConnection("Data Source = DUONGDAT, Initial Catalog = PONG; Integrated Security=SSPI");
            try
            {
                conn.Open();
                string account = textBox1.Text;
                string password = textBox2.Text;
                string sql = "select *from USERS where Tên_đăng_nhập= '" + account + "' and Mật_khẩu= '" + password + "'";
                SqlCommand cmd = new SqlCommand(sql, conn);
                SqlDataReader reader = cmd.ExecuteReader();
                if (reader.Read())
                {
                    MessageBox.Show("Đăng nhập thành công!");
                }
                else
                {
                    MessageBox.Show("Đăng nhập thất bại"); 
                }

            }        
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi kết nối");
            }
        }

        private void Pong_Load(object sender, EventArgs e)
        {

        }
    }
}
