package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	String com;
	private JButton btnReset;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
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
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 269, 407);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("세 자리 수:");
		lbl.setBounds(41, 31, 89, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(142, 28, 75, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞혀보자ㅏ");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(33, 64, 97, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(33, 106, 184, 231);
		contentPane.add(ta);
		
		btnReset = new JButton("Reset");
		btnReset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myreset();
			}
		});
		btnReset.setBounds(142, 64, 75, 23);
		contentPane.add(btnReset);
		
		setCom();
	}
	
	public int getStrike(String com, String mine) {
		int cnt = 0;
		String c1 = com.substring(0, 1);
		String c2 = com.substring(1, 2);
		String c3 = com.substring(2, 3);
		
		String m1 = mine.substring(0, 1);
		String m2 = mine.substring(1, 2);
		String m3 = mine.substring(2, 3);
		
		if(c1.equals(m1)) {
			cnt++;
		}
		
		if(c2.equals(m2)) {
			cnt++;
		}
		
		if(c3.equals(m3)) {
			cnt++;
		}
		return cnt;
	}
	
	
	public int getBall(String com, String mine) {
		int cnt = 0;
		String c1 = com.substring(0, 1);
		String c2 = com.substring(1, 2);
		String c3 = com.substring(2, 3);
		
		String m1 = mine.substring(0, 1);
		String m2 = mine.substring(1, 2);
		String m3 = mine.substring(2, 3);
		
		if(c1.equals(m2) || c1.equals(m3)) {
			cnt++;
		}
		
		if(c2.equals(m1) || c2.equals(m3)) {
			cnt++;
		}
		
		if(c3.equals(m1) || c3.equals(m2)) {
			cnt++;
		}
		return cnt;
	}
	
	
	public void myclick() {
		String str_old = ta.getText();
		
		String mine = tf.getText();
		int s = getStrike(com,mine);
		int b = getBall(com,mine);
		System.out.println(s);
		System.out.println(b);
		
		String str_new = mine+"\s"+s+"S"+b+"B\n";
		ta.setText(str_old+str_new);
		tf.setText("");
		
		if(s==3) {
			JOptionPane.showMessageDialog(null, "와~~"+mine+"을 맞혔습니다.");
		}
//		ta.append(mine+"\s"+s+"S"+b+"B\n");
	}
	
	public void myreset() {
		
		tf.setText("");
		ta.setText("");
		setCom();
	}
	
	public void setCom() {
		
		// 맨 처음 게임 랜덤숫자 뽑기
		int[] ran = {1,2,3,4,5,6,7,8,9};
		
	      for(int i=0; i<100; i++) {
	          int num = (int) (Math.random()*9);
	          int a = ran[0];
	          int b = ran[num];
	          ran[0] = b;
	          ran[num] = a;
	       }
	      
	      com = ""+ran[0]+ran[1]+ran[2];
	      System.out.println("com: "+com);
	}
}
