namespace MatchInterface
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            player1 = new PictureBox();
            cpuPlayer = new PictureBox();
            pongBall = new PictureBox();
            pictureBox4 = new PictureBox();
            playerScoreLabel = new Label();
            cpuScoreLabel = new Label();
            pongTimer = new System.Windows.Forms.Timer(components);
            btOut = new Button();
            ((System.ComponentModel.ISupportInitialize)player1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)cpuPlayer).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pongBall).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox4).BeginInit();
            SuspendLayout();
            // 
            // player1
            // 
            player1.BackColor = Color.Navy;
            player1.Location = new Point(12, 188);
            player1.Name = "player1";
            player1.Size = new Size(18, 137);
            player1.TabIndex = 0;
            player1.TabStop = false;
            // 
            // cpuPlayer
            // 
            cpuPlayer.BackColor = Color.GreenYellow;
            cpuPlayer.Location = new Point(1322, 188);
            cpuPlayer.Name = "cpuPlayer";
            cpuPlayer.Size = new Size(18, 137);
            cpuPlayer.TabIndex = 1;
            cpuPlayer.TabStop = false;
            // 
            // pongBall
            // 
            pongBall.BackColor = Color.Transparent;
            pongBall.BackgroundImage = (Image)resources.GetObject("pongBall.BackgroundImage");
            pongBall.BackgroundImageLayout = ImageLayout.Stretch;
            pongBall.Location = new Point(667, 258);
            pongBall.Name = "pongBall";
            pongBall.Size = new Size(37, 37);
            pongBall.TabIndex = 2;
            pongBall.TabStop = false;
            // 
            // pictureBox4
            // 
            pictureBox4.BackColor = Color.Transparent;
            pictureBox4.BackgroundImage = (Image)resources.GetObject("pictureBox4.BackgroundImage");
            pictureBox4.BackgroundImageLayout = ImageLayout.Stretch;
            pictureBox4.Location = new Point(622, 14);
            pictureBox4.Name = "pictureBox4";
            pictureBox4.Size = new Size(125, 62);
            pictureBox4.TabIndex = 4;
            pictureBox4.TabStop = false;
            // 
            // playerScoreLabel
            // 
            playerScoreLabel.BackColor = Color.Transparent;
            playerScoreLabel.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            playerScoreLabel.ForeColor = Color.Cyan;
            playerScoreLabel.Location = new Point(585, 34);
            playerScoreLabel.Name = "playerScoreLabel";
            playerScoreLabel.Size = new Size(31, 25);
            playerScoreLabel.TabIndex = 5;
            playerScoreLabel.Text = "0";
            playerScoreLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // cpuScoreLabel
            // 
            cpuScoreLabel.BackColor = Color.Transparent;
            cpuScoreLabel.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            cpuScoreLabel.ForeColor = Color.OrangeRed;
            cpuScoreLabel.Location = new Point(753, 34);
            cpuScoreLabel.Name = "cpuScoreLabel";
            cpuScoreLabel.Size = new Size(31, 25);
            cpuScoreLabel.TabIndex = 6;
            cpuScoreLabel.Text = "0";
            cpuScoreLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // pongTimer
            // 
            pongTimer.Enabled = true;
            pongTimer.Interval = 20;
            pongTimer.Tick += PongTimer_Tick;
            // 
            // btOut
            // 
            btOut.Location = new Point(12, 12);
            btOut.Name = "btOut";
            btOut.Size = new Size(94, 29);
            btOut.TabIndex = 7;
            btOut.Text = "Thoát";
            btOut.UseVisualStyleBackColor = true;
            btOut.Click += btOut_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            BackgroundImage = (Image)resources.GetObject("$this.BackgroundImage");
            BackgroundImageLayout = ImageLayout.Stretch;
            ClientSize = new Size(1352, 620);
            Controls.Add(btOut);
            Controls.Add(cpuScoreLabel);
            Controls.Add(playerScoreLabel);
            Controls.Add(pictureBox4);
            Controls.Add(pongBall);
            Controls.Add(cpuPlayer);
            Controls.Add(player1);
            DoubleBuffered = true;
            Name = "Form1";
            Text = "Pong";
            Load += Form1_Load;
            KeyDown += Form1_KeyDown;
            KeyUp += Form1_KeyUp;
            ((System.ComponentModel.ISupportInitialize)player1).EndInit();
            ((System.ComponentModel.ISupportInitialize)cpuPlayer).EndInit();
            ((System.ComponentModel.ISupportInitialize)pongBall).EndInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox4).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private PictureBox player1;
        private PictureBox cpuPlayer;
        private PictureBox pongBall;
        private PictureBox pictureBox4;
        private Label playerScoreLabel;
        private Label cpuScoreLabel;
        private System.Windows.Forms.Timer pongTimer;
        private Button btOut;
    }
}
