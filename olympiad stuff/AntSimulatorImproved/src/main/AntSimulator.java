package main;

import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Toolkit;
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
		setSize (GRID_SIZE*LANDSCAPE_DIMENSION, GRID_SIZE*LANDSCAPE_DIMENSION);
		setResizable (false);
		setVisible (false);
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
			g.fillRect(0, 0, LANDSCAPE_DIMENSION*GRID_SIZE, LANDSCAPE_DIMENSION*GRID_SIZE);
			g.setColor(Color.black);
			for (int x = 0; x < LANDSCAPE_DIMENSION; x++) {
				for (int y = 0; y < LANDSCAPE_DIMENSION; y++) {
					g.drawRect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE);
				}
			}
			
			for (Ant a : ants) {
				g.setColor(Color.gray);
				g.fillRect((int)(((float)a.x+0.25)*GRID_SIZE), (int)(((float)a.y+0.25)*GRID_SIZE), GRID_SIZE/2, GRID_SIZE/2);
			}
			return;
		}
		g.setColor(landscape.get(toRepaint) ? Color.black : Color.white);
		g.fillRect(toRepaint.x*GRID_SIZE, toRepaint.y*GRID_SIZE, GRID_SIZE, GRID_SIZE);
		g.setColor(Color.black);
		g.drawRect(toRepaint.x*GRID_SIZE, toRepaint.y*GRID_SIZE, GRID_SIZE, GRID_SIZE);
		if (antDirection != -1) {
			g.setColor(Color.gray);
			g.fillRect((int)(((float)toRepaint.x+0.25)*GRID_SIZE), (int)(((float)toRepaint.y+0.25)*GRID_SIZE), GRID_SIZE/2, GRID_SIZE/2);
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
			if (landscape.get (a.x, a.y)) {
				a.r--;
			} else {
				a.r++;
			}
			if (a.r > 3) a.r = 0;
			if (a.r < 0) a.r = 3;
			if (a.x < 0 || a.x >= LANDSCAPE_DIMENSION) killList.add(a);
			else if (a.y < 0 || a.y >= LANDSCAPE_DIMENSION) killList.add(a);
			else {
				landscape.set(new Coord (a.x, a.y), !landscape.get (a.x, a.y));
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
		setSize (GRID_SIZE*LANDSCAPE_DIMENSION, GRID_SIZE*LANDSCAPE_DIMENSION);
		while (true) {
			try {
				int input = Integer.parseInt(JOptionPane.showInputDialog("Enter a number of moves to calculate, or -1 to exit"));
				if (input == -1) System.exit(0);
				for (int i = 0; i < input; i++) {
					iterate ();
					Thread.sleep(1);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
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
			if (NUM_ANTS < 1) { preLabel = new JLabel ("Number of ants too small!"); continue; }
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
