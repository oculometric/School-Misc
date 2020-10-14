package main;

import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

import javax.imageio.ImageIO;
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
	public static int NUM_PHEROMONES = 4;
	
	
	public AntSimulator () {
		super ("ANTS!!!!");
		setSize (GRID_SIZE*LANDSCAPE_DIMENSION, GRID_SIZE*LANDSCAPE_DIMENSION);
		setResizable (false);
		setVisible (false);
	}
	
	public Queue<Coord> paintQueue = new LinkedList<Coord> ();
	
	public PheromoneMap pheromoneMap;
	
	public ArrayList<Ant> ants = new ArrayList<Ant> ();
	
	private Coord toRepaint;
	private int antDirection;
	
	private Color forCoord (Coord c) {
		int value = pheromoneMap.get(c);
		float f = (float)value/(float)NUM_PHEROMONES;
		Color col = Color.getHSBColor(f, 0.5f, 0.8f);
		return col;
	}
	
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
			
			return;
		}
		g.setColor(forCoord (toRepaint));
		g.fillRect(toRepaint.x*GRID_SIZE, toRepaint.y*GRID_SIZE, GRID_SIZE, GRID_SIZE);
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
			
			if (a.x < 0 || a.x >= LANDSCAPE_DIMENSION) killList.add(a);
			else if (a.y < 0 || a.y >= LANDSCAPE_DIMENSION) killList.add(a);
			else {
				pheromoneAnalysis (a);
				paintSquare (a.x, a.y, a.r);
			}
		}
		for (Ant k : killList) {
			ants.remove(k);
		}
	}
	
	private int pheromoneData (int offset, Coord origin, int rotation) {
		Coord pointToFetch = origin;
		int realOffset = offset + rotation*2;
		realOffset = realOffset % 8;
		
		switch (realOffset) {
		case 0: return pheromoneMap.get(pointToFetch.x+1, pointToFetch.y);
		case 1: return pheromoneMap.get(pointToFetch.x+1, pointToFetch.y+1);
		case 2: return pheromoneMap.get(pointToFetch.x, pointToFetch.y+1);
		case 3: return pheromoneMap.get(pointToFetch.x-1, pointToFetch.y+1);
		case 4: return pheromoneMap.get(pointToFetch.x-1, pointToFetch.y);
		case 5: return pheromoneMap.get(pointToFetch.x-1, pointToFetch.y-1);
		case 6: return pheromoneMap.get(pointToFetch.x, pointToFetch.y-1);
		case 7: return pheromoneMap.get(pointToFetch.x+1, pointToFetch.y-1);
		}
		return 0;
	}
	
	private void pheromoneAnalysis(Ant a) {
		int pheroID = 0;
		pheroID += pheromoneMap.get(a.x, a.y);
		Coord coord = a.getCoord();
		pheroID += pheromoneData (0, coord, a.r);
		pheroID += pheromoneData (1, coord, a.r);
		pheroID += pheromoneData (2, coord, a.r);
		pheroID += pheromoneData (3, coord, a.r);
		pheroID += pheromoneData (4, coord, a.r);
		pheroID += pheromoneData (5, coord, a.r);
		pheroID += pheromoneData (6, coord, a.r);
		pheroID += pheromoneData (7, coord, a.r);
		
		if (pheroID < NUM_PHEROMONES*3) pheromoneMap.set(coord, pheromoneMap.get(coord) + pheroID%3 + 1);
		else pheromoneMap.set(coord, pheromoneMap.get(coord) - pheroID%3 - 1);
		//pheromoneMap.set(coord, a.id*(pheroID+1));
		// TODO: EDIT RULES
		if (pheroID % 5 == 0) {
			a.r--;
		} else if (pheroID % 5 == 1) {
			a.r++;
		} else if (pheroID % 5 == 2) {
			a.r+=2;
		}
		a.r += 4;
		a.r = a.r % 4;
		
		img.setRGB(a.x, a.y, forCoord (coord).getRGB());
	}

	public BufferedImage img;
	
	public void startSimulation () {
		pheromoneMap = new PheromoneMap (LANDSCAPE_DIMENSION);
		setVisible (true);
		setSize (GRID_SIZE*LANDSCAPE_DIMENSION, GRID_SIZE*LANDSCAPE_DIMENSION);
		img = new BufferedImage (LANDSCAPE_DIMENSION, LANDSCAPE_DIMENSION, BufferedImage.TYPE_INT_RGB);
		while (ants.size() > 0) {
			try {
				iterate ();
				Thread.sleep(1);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		try {
		    File outputfile = new File("antsoutput.png");
		    ImageIO.write(img, "png", outputfile);
		} catch (IOException e) {
		    e.printStackTrace();
		}
	}
	
	public void displaySetupDialog() {
		JTextField lSizeField = new JTextField ();
		lSizeField.setText("100");
		JTextField gSizeField = new JTextField ();
		gSizeField.setText("8");
		JTextField aField = new JTextField ();
		aField.setText("8");
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
			if (LANDSCAPE_DIMENSION > 9999) { preLabel = new JLabel ("Landscape size too large!"); continue; }
			if (GRID_SIZE < 1) { preLabel = new JLabel ("Grid size too small!"); continue; }
			if (GRID_SIZE*LANDSCAPE_DIMENSION > Toolkit.getDefaultToolkit().getScreenSize().getHeight()) { preLabel = new JLabel ("Total window size too large for screen!"); continue; }
			if (NUM_ANTS < 1) { preLabel = new JLabel ("Number of ants too small!"); continue; }
			if (NUM_ANTS >= LANDSCAPE_DIMENSION*LANDSCAPE_DIMENSION) { preLabel = new JLabel ("Number of ants too large!"); continue; }
			break;
		}
		Random r = new Random ();
		for (int i = 0; i < NUM_ANTS; i++) {
//			JTextField xField = new JTextField ();
//			xField.setText("0");
//			JTextField yField = new JTextField ();
//			yField.setText("0");
//			JTextField dField = new JTextField ();
//			dField.setText("B");
//			JLabel preLabel1 = null;
//			while (true) {
//				JOptionPane.showMessageDialog(this, new Object[] {
//					preLabel1,
//					new JLabel ("X position for ant " + i + ":"),
//					xField,
//					new JLabel ("Y position for ant " + i + ":"),
//					yField,
//					new JLabel ("Rotation for ant " + i + ":"),
//					dField
//				});
//				try {
//					if (dField.getText().length() != 1 || (dField.getText().charAt(0) != 'T' && dField.getText().charAt(0) != 'B' && dField.getText().charAt(0) != 'L' && dField.getText().charAt(0) != 'R')) { preLabel1 = new JLabel ("Direction must be 'T', 'B', 'L', or 'R'!"); continue; }
//					if (Integer.parseInt(xField.getText()) < 0 || Integer.parseInt(xField.getText()) >= LANDSCAPE_DIMENSION) { preLabel1 = new JLabel ("Invalid X position!"); continue; }
//					if (Integer.parseInt(yField.getText()) < 0 || Integer.parseInt(yField.getText()) >= LANDSCAPE_DIMENSION) { preLabel1 = new JLabel ("Invalid Y position!"); continue; }
//				} catch (NumberFormatException e) { preLabel1 = new JLabel ("Please enter valid integers!"); continue; }
//				break;
//			}
//			int dir = 0;
//			if (dField.getText().charAt(0) == 'T') dir = 3;
//			if (dField.getText().charAt(0) == 'B') dir = 1;
//			if (dField.getText().charAt(0) == 'L') dir = 2;
//			ants.add(new Ant (Integer.parseInt(xField.getText()), Integer.parseInt(yField.getText()), dir));
			ants.add(new Ant (r.nextInt(LANDSCAPE_DIMENSION-2)+1, r.nextInt(LANDSCAPE_DIMENSION-2)+1, r.nextInt(4)));
		
		}
	}
}
