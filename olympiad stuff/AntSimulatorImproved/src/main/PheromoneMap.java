package main;

import java.util.ArrayList;

public class PheromoneMap {

	private ArrayList<ArrayList<Integer>> data;
	
	public PheromoneMap(int dim) {
		data = new ArrayList<ArrayList<Integer>> ();
		for (int i = 0; i < dim; i++) {
			data.add(new ArrayList<Integer>());
			for (int j = 0; j < dim; j++) {
				data.get(i).add(0);
			}
		}
	}
	
	synchronized void set (Coord c, int b) {
		try {
			data.get(c.y).set(c.x, b % AntSimulator.NUM_PHEROMONES);
		} catch (Exception e) {}
	}
	
	synchronized int get (Coord c) {
		try {
			return data.get(c.y).get(c.x);
		} catch (Exception e) {}
		return 0;
	}

	synchronized int get(int x, int y) {
		try {
			return data.get(y).get(x);
		} catch (Exception e) {}
		return 0;
	}

}
