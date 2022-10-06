package day04;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;

public class MySwing02 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing02 frame = new MySwing02();
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
	public MySwing02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("100");
		lbl.setBounds(68, 57, 38, 32);
		contentPane.add(lbl);
		
		JButton btn = new JButton("decrease");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int result = Integer.parseInt(lbl.getText());
				result -= 1;
				lbl.setText(""+result);
			}
		});
		
		btn.setBounds(118, 62, 97, 23);
		contentPane.add(btn);
	
	}
}
