package main;

import java.util.ArrayList;

public class Landscape {

	private ArrayList<ArrayList<Boolean>> data;
	
	public Landscape(int dim) {
		data = new ArrayList<ArrayList<Boolean>> ();
		for (int i = 0; i < dim; i++) {
			data.add(new ArrayList<Boolean>());
			for (int j = 0; j < dim; j++) {
				data.get(i).add(false);
			}
		}
	}
	
	synchronized void set (Coord c, boolean b) {
		try {
			data.get(c.y).set(c.x, b);
		} catch (Exception e) {}
	}
	
	synchronized boolean get (Coord c) {
		try {
			return data.get(c.y).get(c.x);
		} catch (Exception e) {}
		return false;
	}

	synchronized boolean get(int x, int y) {
		try {
			return data.get(y).get(x);
		} catch (Exception e) {}
		return false;
	}

}
