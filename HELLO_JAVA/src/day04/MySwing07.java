package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 216, 273);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나");
		lblMine.setBounds(30, 32, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴");
		lblCom.setBounds(30, 74, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과");
		lblResult.setBounds(30, 119, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(116, 29, 50, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(116, 71, 50, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(116, 116, 50, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("가위바위보 하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		
		btn.setBounds(30, 166, 136, 23);
		contentPane.add(btn);
	}
	
	private void myclick() {
		
		String na = tfMine.getText();
		String com = "";
		String result = "";
		
		double rnd = Math.random();
		
		if (rnd>0.66) {
			com = "가위";
		} else if (rnd>0.33) {
			com = "바위";
		} else {
			com = "보";
		}
		
		if(com.equals("가위") && na.equals("가위")) result = "무승부";
		if(com.equals("가위") && na.equals("바위")) result = "승리";
		if(com.equals("가위") && na.equals("보")) result = "패배";
		
		if(com.equals("바위") && na.equals("가위")) result = "패배";
		if(com.equals("바위") && na.equals("바위")) result = "무승부";
		if(com.equals("바위") && na.equals("보")) result = "승리";
		
		if(com.equals("보") && na.equals("가위")) result = "승리";
		if(com.equals("보") && na.equals("바위")) result = "패배";
		if(com.equals("보") && na.equals("보")) result = "무승부";

		tfCom.setText(com);
		tfResult.setText(result);
		
	}
}
