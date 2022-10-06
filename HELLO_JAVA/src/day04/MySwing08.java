package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	private JButton btn;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 315, 449);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblFirst = new JLabel("첫 별 수:");
		lblFirst.setBounds(44, 40, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝 별 수:");
		lblLast.setBounds(44, 83, 57, 15);
		contentPane.add(lblLast);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(140, 37, 116, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		tfLast = new JTextField();
		tfLast.setColumns(10);
		tfLast.setBounds(140, 80, 116, 21);
		contentPane.add(tfLast);
		
		btn = new JButton("별 출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		
		btn.setBounds(44, 129, 212, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(44, 177, 212, 205);
		contentPane.add(ta);
	}
	
	private void myclick() {
		
		int first = Integer.parseInt(tfFirst.getText());
		int last = Integer.parseInt(tfLast.getText());
		
		for(int i=first; i<=last; i++) {
			for(int j=1; j<=i; j++) {
				ta.append("*");
			}
			ta.append("\n");
		}
		
	}
}
