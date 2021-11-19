import javax.swing.*;

//template class that holds each cell
public class Cell extends JLabel {

	// fields
	private int row;
	private int column;

	// constructor
	public Cell(int row, int column) {

		this.row = row;
		this.column = column;
	}

	// default constructor
	public Cell() {

	}

	// getters and setters
	public int getRow() {
		return row;
	}

	public void setRow(int row) {
		this.row = row;
	}

	public int getColumn() {
		return column;
	}

	public void setColumn(int column) {
		this.column = column;
	}

	// toString method
	@Override
	public String toString() {
		return "Cell [row=" + row + ", column=" + column + "]";
	}

}
