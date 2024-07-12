import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.*;
import java.util.concurrent.TimeUnit;

import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.*;
import javax.swing.Timer;

/*
 * Name: Jaffer Razavi
 * 
 * Date: January 26, 2021
 * Purpose: To create an maze game, where the user has to collect coins
 * Extra features:
 * 		 1 - Music
 * 		 2 - Coin sound effect
 * 		 3 - Accurate timer (down to ms)
 * 		 4 - Maze is a different colour
 * 		 5 - icon rotates depending on the direction it moves in
 * 		 6 - When the game starts, there is a start menu
 * 		 7 - When the game ends, there is an end message
 * 		 8 - enhanced labels for timer and scoreboard
 * 		 9 - a random number of coins between 10 and 20 will spawn
 * 		 10 - the total number of coins is shown
 * Areas of concern: 
 * 		 1 - the program kinda glitches at the end 
 * 		 2 - the music wont stop unless the program is closed
*/


//this class has all the code for the GUI
@SuppressWarnings("serial")
public class MazeRaceGUI extends JFrame implements KeyListener, ActionListener {

	// fields (global variables)

	// constants
	private final int CELL_SIZE = 25; // the width of each cell
	private final int NUM_CELLS_WIDTH = 27; // the number of cells wide in the maze
	private final int NUM_CELLS_HEIGHT = 27; // number of cells high in the maze

	private int NUM_COINS = (int) (Math.random() * (20 - 10 + 1) + 10); //

	// set up timer
	public static final int MSECS = 1000;
	public static final int SECS = 60;
	public static final int MIN = 60;
	// mins:secs:millisecs
	private static final String TIME_FORMAT = "%02d:%02d.%3d";
	// delays the start of the timer
	private static final int TIMER_DELAY = 15;

	// images
	private final ImageIcon WALL = new ImageIcon("images/bluecell.jpg");
	private final ImageIcon OUT_OF_BOUNDS = new ImageIcon("images/black square.png");
	private final ImageIcon PATH = new ImageIcon("images/grey square.png");
	private final ImageIcon COIN = new ImageIcon("images/gold coin.gif");

	// variables
	private JPanel mazePanel = new JPanel(new GridBagLayout());
	private GridBagConstraints gridConstraints = new GridBagConstraints();
	private Cell[][] maze = new Cell[NUM_CELLS_WIDTH][NUM_CELLS_HEIGHT];

	// player object image
	private Player player = new Player("images/sonic1.gif");

	// counters
	private int numCoinsCollected = 0;

	// timer and scoreboard
	private JPanel scoreboardPanel = new JPanel(null);
	private Timer gameTimer = new Timer(TIMER_DELAY, this);
	private JLabel timeField = new JLabel("0");
	private long startTime;
	private JLabel scoreLabel = new JLabel("0");
	JLabel[] scoreTotal = new JLabel[2];
	private JLabel timeDisplay = new JLabel("TIME:");
	private JLabel scoreDisplay = new JLabel("SCORE:");

	// constructor method
	public MazeRaceGUI() {

		startMenu();
		makeSound();
		scoreboardPanelSetup();
		mazePanelSetup();
		frameSetup();

	}

	// makes background sound
	public void makeSound() {
		File bMusic = new File("backgroundmusic.wav");

		try {
			Clip dododo = AudioSystem.getClip();
			dododo.open(AudioSystem.getAudioInputStream(bMusic));
			dododo.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// start window
	private void startMenu() {

		Object[] options = { "START" };
		JOptionPane.showOptionDialog(null, "Welcome to Maze Race \nPress start to continue", "Maze Game",
				JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, options, options[0]);
	}

	// sets up scoreboard and timer
	private void scoreboardPanelSetup() {

		// set up scoreboard
		scoreboardPanel.setLayout(null);
		scoreboardPanel.setBounds(0, 0, CELL_SIZE * NUM_CELLS_WIDTH, 50);

		scoreTotal[0] = new JLabel("/");
		scoreTotal[1] = new JLabel(Integer.toString(NUM_COINS));

		// places score
		for (int index = 0; index < scoreTotal.length; index++) {
			scoreTotal[index].setBounds(150 + 20 * index, 30, 100, 20);

			scoreboardPanel.add(scoreTotal[index]);
		}

		// sets bounds of objects/fields
		scoreLabel.setBounds(140, 30, 100, 20); // ADJUST LATER
		timeField.setBounds(140, 10, 100, 20); // ADJUST LATER
		timeDisplay.setBounds(30, 10, 100, 20); // ADJUST LATER
		scoreDisplay.setBounds(30, 30, 100, 20); // ADJUST LATER

		// add stuff to scoreboard
		scoreboardPanel.add(timeField);
		scoreboardPanel.add(scoreLabel);
		scoreboardPanel.add(timeDisplay);
		scoreboardPanel.add(scoreDisplay);

	}

	// sets up maze panel
	private void mazePanelSetup() {

		// sets the bounds of the maze
		mazePanel.setBounds(0, 50, CELL_SIZE * NUM_CELLS_WIDTH, CELL_SIZE * NUM_CELLS_HEIGHT); // ADJUST LATER

		// calls method that loads up the maze file
		loadMaze();
		placeCoins();
		placePlayer();
	}

	// loads the maztefrom the txt file
	private void loadMaze() {

		int row = 0; //
		char[] line; //

		//
		try {

			Scanner input = new Scanner(new File("maze.txt"));

			//
			while (input.hasNext()) {

				line = input.nextLine().toCharArray();// seperates each line into seperate characters

				// goes through one char at a time and fillw it with a cell
				for (int column = 0; column < line.length; column++)
					fillCell(line[column], row, column);

				// increments row by 1
				row++;

			}

			// closes scanner
			input.close();

		} catch (FileNotFoundException error) {
			System.out.println("File error + error");
		}

	}

	// places coins
	private void placeCoins() {

		//
		for (int coin = 1; coin <= NUM_COINS; coin++) {

			Cell cell = findEmptyCell(); // finds empty cell

			maze[cell.getRow()][cell.getColumn()].setIcon(COIN);

		}
	}

	// this method plates the player object
	private void placePlayer() {

		Cell cell = findEmptyCell();

		//
		player.setRow(cell.getRow());
		player.setColumn(cell.getColumn());

		//
		maze[cell.getRow()][cell.getColumn()].setIcon(player.getIcon());

	}

	// this method finds an empty cell
	private Cell findEmptyCell() {

		Cell cell = new Cell(); // creates empty cell

		//
		do {

			cell.setRow((int) (Math.random() * 24) + 2);
			cell.setColumn((int) (Math.random() * 24) + 2);

		} while (maze[cell.getRow()][cell.getColumn()].getIcon() != PATH);

		return cell;

	}

	// converts the text file to cells
	private void fillCell(char character, int row, int column) {

		//
		maze[row][column] = new Cell(row, column);

		// replaces the txt maze file with coloured cells
		if (character == 'W')
			maze[row][column].setIcon(WALL);
		else if (character == '.')
			maze[row][column].setIcon(PATH);
		else if (character == 'X')
			maze[row][column].setIcon(OUT_OF_BOUNDS);

		//
		gridConstraints.gridx = column;
		gridConstraints.gridy = row;
		mazePanel.add(maze[row][column], gridConstraints);
	}

	// sets up frame
	private void frameSetup() {

		// sets up the maze panel/frame
		setTitle("Maze Race");
		setSize(mazePanel.getWidth() + 15, mazePanel.getHeight() + scoreboardPanel.getHeight() + 38); // ADJUST LATER
		setLayout(null);

		// adds both panels to the JFrame
		add(scoreboardPanel);
		add(mazePanel);

		// detects key input
		addKeyListener(this);

		// exits window when its closed
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setResizable(false);
		setVisible(true);

		// starts the game timer on key pressed
		gameTimer.start();

	}

	// when an action occurs, the timer increases
	@Override
	public void actionPerformed(ActionEvent event) {

		if (startTime == 0L) {
			startTime = System.currentTimeMillis();
		} else {

			// takes the current time in milliseconds
			long currentTime = System.currentTimeMillis();
			int diffTime = (int) (currentTime - startTime);

			int mSecs = diffTime % MSECS;
			diffTime /= MSECS;

			int sec = diffTime % SECS;
			diffTime /= SECS;

			int min = diffTime % MIN;
			diffTime /= MIN;

			// sets the value of the time
			String time = String.format(TIME_FORMAT, min, sec, mSecs);

			// sets the time
			timeField.setText(time);

		}

	}

	// this method gets key input
	@Override
	public void keyPressed(KeyEvent key) {

		// checks to see if player is moving upwards
		if (key.getKeyCode() == KeyEvent.VK_W && maze[player.getRow() - 1][player.getColumn() + 0].getIcon() != WALL) { // up

			player.setIcon(new ImageIcon("images/sonic0.gif"));
			movePlayer(-1, 0);

		} else if (key.getKeyCode() == KeyEvent.VK_D
				&& maze[player.getRow() + 0][player.getColumn() + 1].getIcon() != WALL) { // right

			player.setIcon(new ImageIcon("images/sonic1.gif"));
			movePlayer(0, 1);

		} else if (key.getKeyCode() == KeyEvent.VK_S
				&& maze[player.getRow() + 1][player.getColumn() + 0].getIcon() != WALL) { // down

			player.setIcon(new ImageIcon("images/sonic2.gif"));
			movePlayer(1, 0);

		} else if (key.getKeyCode() == KeyEvent.VK_A
				&& maze[player.getRow() + 0][player.getColumn() - 1].getIcon() != WALL) { // left

			player.setIcon(new ImageIcon("images/sonic3.gif"));
			movePlayer(0, -1);

		}

	}

	// this method moves the player
	private void movePlayer(int dRow, int dColumn) {

		// removes the position of the player
		maze[player.getRow()][player.getColumn()].setIcon(PATH);

		// checks to see were the player is moving
		if (maze[player.getRow() + dRow][player.getColumn() + dColumn].getIcon() == COIN) {

			// plays coin sound
			coinSound();

			// sets the text of the score
			numCoinsCollected++;
			scoreLabel.setText(Integer.toString(numCoinsCollected));

			// once the number of coins collected reaches hte number of coins in total, the
			// user wins
			if (numCoinsCollected == NUM_COINS) {

				gameTimer.stop();

				// 1 second delay before the winner window is shown
				try {
					TimeUnit.SECONDS.sleep(1);
				} catch (InterruptedException e) {
				}

				// makes sure timer runs only once
				winnerFrame(); // CHANGE TO IMAGE POPPING UP THAT SAYS WINNER

			}
		}

		//
		player.move(dRow, dColumn);
		maze[player.getRow()][player.getColumn()].setIcon(player.getIcon());

	}

	// playes coin sound
	public void coinSound() {
		File coinSound = new File("coinp.wav");

		try {
			Clip coinClink = AudioSystem.getClip();
			coinClink.open(AudioSystem.getAudioInputStream(coinSound));
			coinClink.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// shows a message that the player won
	private void winnerFrame() {
		JOptionPane.showInternalMessageDialog(null, "information", "information", JOptionPane.INFORMATION_MESSAGE);
	}

	// NOT USED
	@Override
	public void keyTyped(KeyEvent e) {
		// NOT USED
	}

	// NOT USED
	@Override
	public void keyReleased(KeyEvent e) {
		// NOT USED
	}

}