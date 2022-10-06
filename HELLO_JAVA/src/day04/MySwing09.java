package day04;

import java.awt.EventQueue;
import javax.swing.JOptionPane;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.SwingConstants;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JButton btn;
	JButton btn2;
	JButton btn3;
	JButton btn4;
	JButton btn5;
	JButton btn6;
	JButton btn7;
	JButton btn8;
	JButton btn9;
	JButton btn0;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 285, 271);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(28, 32, 211, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn = new JButton("1");
//		btn.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//		//		JButton b = (JButton) e.getSource(); //캐스팅
//		//		System.out.println(b.getText());
//				numclick(e);
//			}
//		});
		btn.setBounds(28, 72, 67, 23);
		contentPane.add(btn);
		
		btn2 = new JButton("2");
		btn2.setBounds(107, 72, 60, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
		btn3.setBounds(179, 72, 60, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.setBounds(28, 105, 67, 23);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
		btn5.setBounds(107, 105, 60, 23);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
		btn6.setBounds(179, 105, 60, 23);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
		btn7.setBounds(28, 139, 67, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.setBounds(107, 139, 60, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.setBounds(179, 138, 60, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.setBounds(28, 172, 67, 23);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("CALL");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				callclick();
			}
		});
		btnCall.setBounds(107, 172, 132, 23);
		contentPane.add(btnCall);
		
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				numclick(e);
			}
		});
		
	}
	
	
	private void numclick(MouseEvent e) {
		JButton b = (JButton) e.getSource();
		String str_old = tf.getText();
		String str_new = b.getText();
		tf.setText(str_old+str_new);
	}

	private void callclick() {
		String str_tel = tf.getText();
		JOptionPane.showMessageDialog(null,"Calling\n"+str_tel); // 자기자신일때 null이나 this를 넣으면 된다
	}
}
