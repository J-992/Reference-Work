import javax.swing.*;

//This class is to make the player move
public class Player extends Cell {

	//
	public Player(String fileName) {

		setIcon(new ImageIcon(fileName));

	}

	//
	public void move(int dRow, int dColumn) {

		setRow(getRow() + dRow);
		setColumn(getColumn() + dColumn);

	}

}
