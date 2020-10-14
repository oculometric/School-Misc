package main;

import java.util.Random;

public class Ant {
	int x;
	int y;
	int r;
	
	public Ant (int xx, int yy, int rr) {
		x = xx;
		y = yy;
		r = rr;
		id = (new Random()).nextInt (100);
	}
	
	public Coord getCoord () {
		return new Coord (x, y);
	}
	
	public int id;
}
