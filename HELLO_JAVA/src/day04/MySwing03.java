package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 481, 333);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lblNewLabel = new JLabel("+");
		lblNewLabel.setBounds(105, 48, 22, 15);
		contentPane.add(lblNewLabel);
		
		tf01 = new JTextField();
		tf01.setBounds(12, 45, 69, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		tf02.setBounds(144, 45, 72, 22);
		contentPane.add(tf02);
		tf02.setColumns(10);
		
		
		tf03 = new JTextField();
		tf03.setBounds(326, 45, 72, 22);
		contentPane.add(tf03);
		tf03.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int first = Integer.parseInt(tf01.getText());
				int second = Integer.parseInt(tf02.getText());
				int result = first+second;
				tf03.setText(""+result);
			}
		});
		
		btn.setBounds(247, 44, 48, 22);
		contentPane.add(btn);
	}
}
