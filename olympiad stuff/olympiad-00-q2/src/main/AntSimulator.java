package main;

import java.awt.Button;
import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class AntSimulator extends Frame {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public int GRID_SIZE = 50;
	public int LANDSCAPE_DIMENSION = 11;
	public int NUM_ANTS = 2;
	
	
	
	public AntSimulator () {
		super ("ANTS!!!!");
		setSize (GRID_SIZE*LANDSCAPE_DIMENSION, (GRID_SIZE*LANDSCAPE_DIMENSION)+getInsets().top);
		setResizable (false);
		setVisible (false);
		
		addMouseListener (new MouseListener() {
			
			@Override
			public void mouseReleased(MouseEvent e) {}
			
			@Override
			public void mousePressed(MouseEvent e) {}
			
			@Override
			public void mouseExited(MouseEvent e) {}
			
			@Override
			public void mouseEntered(MouseEvent e) {}
			
			@Override
			public void mouseClicked(MouseEvent e) {
				int x = e.getX()/GRID_SIZE;
				int y = ((e.getY()-getInsets().top)/GRID_SIZE);
				String input = "";
				while (true) {
					input = JOptionPane.showInputDialog("Direction?");
					if (input == null) return;
					if (input.length() < 1) return;
					if (input.length() == 1 && (input.charAt(0) == 'T' || input.charAt(0) == 'B' || input.charAt(0) == 'L' || input.charAt(0) == 'R')) break;
				}
				int dir = 0;
				if (input.charAt(0) == 'T') dir = 3;
				if (input.charAt(0) == 'B') dir = 1;
				if (input.charAt(0) == 'L') dir = 2;
				ants.add(new Ant (x, y, dir));
				paintSquare (x, y, dir);
			}
		});
	}
	
	private void paintAnt (Graphics g, int x, int y, int r) {
		g.setColor(Color.gray);
		int arrowBackOffset = (int)(0.25*GRID_SIZE);
		int arrowFrontOffset = (int)(0.75*GRID_SIZE);
		int arrowTopOffset = (int)(0.25*GRID_SIZE);
		int arrowBottomOffset = (int)(0.75*GRID_SIZE);
		int arrowMiddleOffset = (int)(0.5*GRID_SIZE);
		
		int realX = (x*GRID_SIZE);
		int realY = (y*GRID_SIZE)+getInsets().top;
		if (r == 0) {
			g.fillPolygon(
					new int[] {realX+arrowBackOffset, realX+arrowFrontOffset, realX+arrowBackOffset}, 
					new int[] {realY+arrowTopOffset, realY+arrowMiddleOffset, realY+arrowBottomOffset}, 3);
		} else if (r == 1) {
			g.fillPolygon(
					new int[] {realX+arrowTopOffset, realX+arrowMiddleOffset, realX+arrowBottomOffset}, 
					new int[] {realY+arrowBackOffset, realY+arrowFrontOffset, realY+arrowBackOffset}, 3);
		} else if (r == 2) {
			g.fillPolygon(
					new int[] {realX+arrowFrontOffset, realX+arrowBackOffset, realX+arrowFrontOffset}, 
					new int[] {realY+arrowTopOffset, realY+arrowMiddleOffset, realY+arrowBottomOffset}, 3);
		} else if (r == 3) {
			g.fillPolygon(
					new int[] {realX+arrowTopOffset, realX+arrowMiddleOffset, realX+arrowBottomOffset}, 
					new int[] {realY+arrowFrontOffset, realY+arrowBackOffset, realY+arrowFrontOffset}, 3);
		}
	}
	
	
	public Queue<Coord> paintQueue = new LinkedList<Coord> ();
	
	public Landscape landscape;
	
	public ArrayList<Ant> ants = new ArrayList<Ant> ();
	
	private Coord toRepaint;
	private int antDirection;
	
	@Override
	public void paint (Graphics g) {
		if (toRepaint == null) {
			g.setColor(Color.white);
			g.fillRect(0, getInsets().top, LANDSCAPE_DIMENSION*GRID_SIZE, LANDSCAPE_DIMENSION*GRID_SIZE);
			g.setColor(Color.black);
			for (int x = 0; x < LANDSCAPE_DIMENSION; x++) {
				for (int y = 0; y < LANDSCAPE_DIMENSION; y++) {
					g.drawRect(x*GRID_SIZE, (y*GRID_SIZE)+getInsets().top, GRID_SIZE, GRID_SIZE);
					if (landscape.get(x, y) == 1) {
						g.fillRect(x*GRID_SIZE, (y*GRID_SIZE)+getInsets().top, GRID_SIZE, GRID_SIZE);
					} else if (landscape.get(x, y) == 2) {
						g.setColor(Color.blue);
						g.fillRect(x*GRID_SIZE, (y*GRID_SIZE)+getInsets().top, GRID_SIZE, GRID_SIZE);
						g.setColor(Color.black);
					}
				}
			}
			
			for (Ant a : ants) {
				paintAnt(g, a.x, a.y, a.r);
			}
			return;
		}
		int v = landscape.get(toRepaint);
		if (v == 0) g.setColor(Color.white);
		if (v == 1) g.setColor(Color.black);
		if (v == 2) g.setColor(Color.blue);
		g.fillRect(toRepaint.x*GRID_SIZE, (toRepaint.y*GRID_SIZE)+getInsets().top, GRID_SIZE, GRID_SIZE);
		g.setColor(Color.black);
		g.drawRect(toRepaint.x*GRID_SIZE, (toRepaint.y*GRID_SIZE)+getInsets().top, GRID_SIZE, GRID_SIZE);
		if (antDirection != -1) {
			paintAnt (g, toRepaint.x, toRepaint.y, antDirection);
		}
		toRepaint = null;
		antDirection = -1;
	}
	
	
	private void paintSquare (int x, int y, int a) {
		toRepaint = new Coord (x, y);
		antDirection = a;
		paint (this.getGraphics());
	}
	
	
	public static void main (String[] args) {
		AntSimulator d = new AntSimulator ();
		d.displaySetupDialog();
		d.startSimulation ();
	}

	
	private void iterate () {
		System.out.println ("Started iteration");
		ArrayList<Ant> killList = new ArrayList<Ant> ();
		for (Ant a : ants) {
			switch (a.r) {
			case 0:
				a.x++;
				paintSquare (a.x-1, a.y, -1);
				break;
			case 1:
				a.y++;
				paintSquare (a.x, a.y-1, -1);
				break;
			case 2:
				a.x--;
				paintSquare (a.x+1, a.y, -1);
				break;
			case 3:
				a.y--;
				paintSquare (a.x, a.y+1, -1);
				break;
			}
			
			if (landscape.get (a.x, a.y) == 1) {
				a.r--;
			} else if (landscape.get (a.x, a.y) == 0) {
				a.r++;
			} else {
				a.r+=2;
			}
			if (a.r > 3) a.r = 0;
			if (a.r < 0) a.r = 3;
			if (a.x < 0 || a.x >= LANDSCAPE_DIMENSION) killList.add(a);
			else if (a.y < 0 || a.y >= LANDSCAPE_DIMENSION) killList.add(a);
			else {
				landscape.set(new Coord (a.x, a.y), landscape.get (a.x, a.y)+1); // TODO: Improve rule
				paintSquare (a.x, a.y, a.r);
			}
		}
		for (Ant k : killList) {
			ants.remove(k);
		}
	}
	
	public void startSimulation () {
		landscape = new Landscape (LANDSCAPE_DIMENSION);
		setVisible (true);
		setSize (GRID_SIZE*LANDSCAPE_DIMENSION, (GRID_SIZE*LANDSCAPE_DIMENSION)+getInsets().top);
		Frame f = new Frame ("Iterate");
		f.setSize(100, 150);
		f.setLayout(new GridLayout (2,1));
		Button b = new Button ("Iterate n times");
		b.addActionListener(new ActionListener () {

			@Override
			public void actionPerformed(ActionEvent e) {
				try {
					int input = Integer.parseInt(JOptionPane.showInputDialog("Enter a number of moves to calculate, or -1 to exit"));
					if (input == -1) System.exit(0);
					for (int i = 0; i < input; i++) {
						iterate ();
						System.out.println (i);
						Thread.sleep(50);
					}
				} catch (Exception ee) {
					//ee.printStackTrace();
				}
			}
			
		});
		f.add(b);
		Button b2 = new Button ("Iterate");
		b2.addActionListener(new ActionListener () {

			@Override
			public void actionPerformed(ActionEvent e) {
				iterate ();
				System.out.println ("Iterated");
			}
			
		});
		f.add(b2);
		f.setVisible(true);
		f.setResizable(false);
	}
	
	public void displaySetupDialog() {
		JTextField lSizeField = new JTextField ();
		lSizeField.setText("11");
		JTextField gSizeField = new JTextField ();
		gSizeField.setText("50");
		JTextField aField = new JTextField ();
		aField.setText("2");
		JLabel preLabel = null;
		while (true) {
			JOptionPane.showMessageDialog(this, new Object[] {
				preLabel,
				new JLabel ("Enter the size of the landscape:"),
				lSizeField,
				new JLabel ("Enter the size of each sector of the landscape:"),
				gSizeField,
				new JLabel ("Enter the number of ants to simulate:"),
				aField
			});
			try {
				LANDSCAPE_DIMENSION = Integer.parseInt(lSizeField.getText());
				GRID_SIZE = Integer.parseInt(gSizeField.getText());
				NUM_ANTS = Integer.parseInt(aField.getText());
			} catch (NumberFormatException e) { preLabel = new JLabel ("Please enter valid integers!"); continue; }
			if (LANDSCAPE_DIMENSION < 3) { preLabel = new JLabel ("Landscape size too small!"); continue; }
			if (LANDSCAPE_DIMENSION > 999) { preLabel = new JLabel ("Landscape size too large!"); continue; }
			if (GRID_SIZE < 4) { preLabel = new JLabel ("Grid size too small!"); continue; }
			if (GRID_SIZE*LANDSCAPE_DIMENSION > Toolkit.getDefaultToolkit().getScreenSize().getHeight()) { preLabel = new JLabel ("Total window size too large for screen!"); continue; }
			if (NUM_ANTS < 0) { preLabel = new JLabel ("Number of ants too small!"); continue; }
			if (NUM_ANTS >= LANDSCAPE_DIMENSION*LANDSCAPE_DIMENSION) { preLabel = new JLabel ("Number of ants too large!"); continue; }
			break;
		}
		
		for (int i = 0; i < NUM_ANTS; i++) {
			JTextField xField = new JTextField ();
			xField.setText("0");
			JTextField yField = new JTextField ();
			yField.setText("0");
			JTextField dField = new JTextField ();
			dField.setText("B");
			JLabel preLabel1 = null;
			while (true) {
				JOptionPane.showMessageDialog(this, new Object[] {
					preLabel1,
					new JLabel ("X position for ant " + i + ":"),
					xField,
					new JLabel ("Y position for ant " + i + ":"),
					yField,
					new JLabel ("Rotation for ant " + i + ":"),
					dField
				});
				try {
					if (dField.getText().length() != 1 || (dField.getText().charAt(0) != 'T' && dField.getText().charAt(0) != 'B' && dField.getText().charAt(0) != 'L' && dField.getText().charAt(0) != 'R')) { preLabel1 = new JLabel ("Direction must be 'T', 'B', 'L', or 'R'!"); continue; }
					if (Integer.parseInt(xField.getText()) < 0 || Integer.parseInt(xField.getText()) >= LANDSCAPE_DIMENSION) { preLabel1 = new JLabel ("Invalid X position!"); continue; }
					if (Integer.parseInt(yField.getText()) < 0 || Integer.parseInt(yField.getText()) >= LANDSCAPE_DIMENSION) { preLabel1 = new JLabel ("Invalid Y position!"); continue; }
				} catch (NumberFormatException e) { preLabel1 = new JLabel ("Please enter valid integers!"); continue; }
				break;
			}
			int dir = 0;
			if (dField.getText().charAt(0) == 'T') dir = 3;
			if (dField.getText().charAt(0) == 'B') dir = 1;
			if (dField.getText().charAt(0) == 'L') dir = 2;
			ants.add(new Ant (Integer.parseInt(xField.getText()), Integer.parseInt(yField.getText()), dir));
		}
	}
}
