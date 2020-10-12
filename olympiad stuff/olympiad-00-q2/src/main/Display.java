package main;

import java.awt.Frame;

import javax.swing.JFormattedTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

import java.awt.Graphics;
import java.awt.Toolkit;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Display extends Frame {
	public int GRID_SIZE = 50;
	public int LANDSCAPE_DIMENSION = 11;
	public int NUM_ANTS = 2;
	
	
	
	public Display () {
		super ("ANTS!!!!");
		setSize (GRID_SIZE*LANDSCAPE_DIMENSION, GRID_SIZE*LANDSCAPE_DIMENSION);
		setResizable (false);
		setVisible (false);
		landscape = new Landscape (LANDSCAPE_DIMENSION);
	}
	
	public Queue<Coord> paintQueue = new LinkedList<Coord> ();
	
	public Landscape landscape;
	
	public ArrayList<Ant> ants = new ArrayList<Ant> ();
	
	@Override
	public void paint (Graphics g) {
		
	}
	
	
	public static void main (String[] args) {
		Display d = new Display ();
		d.displaySetupDialog();
	}

	
	public void displaySetupDialog() {
		JFormattedTextField lSizeField = new JFormattedTextField (NumberFormat.getNumberInstance());
		lSizeField.setValue(11);
		JFormattedTextField gSizeField = new JFormattedTextField (NumberFormat.getNumberInstance());
		gSizeField.setValue(50);
		JFormattedTextField aField = new JFormattedTextField (NumberFormat.getNumberInstance());
		aField.setValue(2);
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
			LANDSCAPE_DIMENSION = (int)lSizeField.getValue();
			GRID_SIZE = (int)gSizeField.getValue();
			NUM_ANTS = (int)aField.getValue();
			if (LANDSCAPE_DIMENSION < 3) { preLabel = new JLabel ("Landscape size too small!"); continue; }
			if (LANDSCAPE_DIMENSION > 999) { preLabel = new JLabel ("Landscape size too large!"); continue; }
			if (GRID_SIZE < 10) { preLabel = new JLabel ("Grid size too small!"); continue; }
			if (GRID_SIZE*LANDSCAPE_DIMENSION > Toolkit.getDefaultToolkit().getScreenSize().getHeight()) { preLabel = new JLabel ("Total window size too large for screen!"); continue; }
			if (NUM_ANTS < 1) { preLabel = new JLabel ("Number of ants too small!"); continue; }
			if (NUM_ANTS >= LANDSCAPE_DIMENSION*LANDSCAPE_DIMENSION) { preLabel = new JLabel ("Number of ants too large!"); continue; }
			break;
		}
		
		for (int i = 0; i < NUM_ANTS; i++) {
			JFormattedTextField xField = new JFormattedTextField (NumberFormat.getNumberInstance());
			JFormattedTextField yField = new JFormattedTextField (NumberFormat.getNumberInstance());
			JTextField dField = new JTextField ();
			JLabel preLabel1 = null;
			while (true) {
				JOptionPane.showMessageDialog(this, new Object[] {
					preLabel,
					new JLabel ("X position for ant " + i + ":"),
					xField,
					new JLabel ("Y position for ant " + i + ":"),
					yField,
					new JLabel ("Rotation for ant " + i + ":"),
					dField
				});
				if (dField.getText().length() > 0 || (dField.getText().charAt(0) != 'T' && dField.getText().charAt(0) != 'B' && dField.getText().charAt(0) != 'L' && dField.getText().charAt(0) != 'R')) { preLabel = new JLabel ("Direction must be 'T', 'B', 'L', or 'R'!"); continue; }
				if ((int)xField.getValue() < 0 || (int)xField.getValue() >= LANDSCAPE_DIMENSION) { preLabel = new JLabel ("Invalid X position!"); continue; }
				if ((int)yField.getValue() < 0 || (int)yField.getValue() >= LANDSCAPE_DIMENSION) { preLabel = new JLabel ("Invalid Y position!"); continue; }
				break;
			}
			int dir = dField.getText();
			ants.add(new Ant ((int)xField.getValue(), (int)yField.getValue(), dir));
		}
		
		// TODO: Get more input
	}
}
