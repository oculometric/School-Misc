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
		data.get(c.y).set(c.x, b);
	}
	
	synchronized boolean get (Coord c) {
		return data.get(c.y).get(c.x);
	}

}
