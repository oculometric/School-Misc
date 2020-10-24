package main;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Panel;

public class DisplayPanel extends Panel {
	AntSimulator parent;
	
	public DisplayPanel (AntSimulator p) {
		super ();
		parent = p;
	}
	
	private void paintAnt (Graphics g, int x, int y, int r) {
		g.setColor(Color.gray);
		int arrowBackOffset = (int)(0.25*parent.GRID_SIZE);
		int arrowFrontOffset = (int)(0.75*parent.GRID_SIZE);
		int arrowTopOffset = (int)(0.25*parent.GRID_SIZE);
		int arrowBottomOffset = (int)(0.75*parent.GRID_SIZE);
		int arrowMiddleOffset = (int)(0.5*parent.GRID_SIZE);
		
		int realX = (x*parent.GRID_SIZE);
		int realY = (y*parent.GRID_SIZE)+getInsets().top;
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
	
	@Override
	public void paint (Graphics g) {
		if (parent.toRepaint == null) {
			g.setColor(Color.white);
			g.fillRect(0, getInsets().top, parent.LANDSCAPE_DIMENSION*parent.GRID_SIZE, parent.LANDSCAPE_DIMENSION*parent.GRID_SIZE);
			g.setColor(Color.black);
			for (int x = 0; x < parent.LANDSCAPE_DIMENSION; x++) {
				for (int y = 0; y < parent.LANDSCAPE_DIMENSION; y++) {
					g.drawRect(x*parent.GRID_SIZE, (y*parent.GRID_SIZE)+getInsets().top, parent.GRID_SIZE, parent.GRID_SIZE);
					if (parent.landscape.get(x, y) == 1) {
						g.fillRect(x*parent.GRID_SIZE, (y*parent.GRID_SIZE)+getInsets().top, parent.GRID_SIZE, parent.GRID_SIZE);
					} else if (parent.landscape.get(x, y) == 2) {
						g.setColor(Color.blue);
						g.fillRect(x*parent.GRID_SIZE, (y*parent.GRID_SIZE)+getInsets().top, parent.GRID_SIZE, parent.GRID_SIZE);
						g.setColor(Color.black);
					}
				}
			}
			
			for (Ant a : parent.ants) {
				paintAnt(g, a.x, a.y, a.r);
			}
			return;
		}
		int v = parent.landscape.get(parent.toRepaint);
		if (v == 0) g.setColor(Color.white);
		if (v == 1) g.setColor(Color.black);
		if (v == 2) g.setColor(Color.blue);
		g.fillRect(parent.toRepaint.x*parent.GRID_SIZE, (parent.toRepaint.y*parent.GRID_SIZE)+getInsets().top, parent.GRID_SIZE, parent.GRID_SIZE);
		g.setColor(Color.black);
		g.drawRect(parent.toRepaint.x*parent.GRID_SIZE, (parent.toRepaint.y*parent.GRID_SIZE)+getInsets().top, parent.GRID_SIZE, parent.GRID_SIZE);
		if (parent.antDirection != -1) {
			paintAnt (g, parent.toRepaint.x, parent.toRepaint.y, parent.antDirection);
		}
		parent.toRepaint = null;
		parent.antDirection = -1;
	}
}
