
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;

public class LaptopAdviserGUIUserRatings extends JFrame implements ActionListener{

	//create the JPanels
	JPanel userRatingsPanel0 = new JPanel();
	JPanel userRatingsPanel1 = new JPanel();
	JPanel userRatingsPanel2 = new JPanel();
	JPanel userRatingsPanel3 = new JPanel();

	//create the JLabels for the titles 
	JLabel title = new JLabel("USER RATINGS");
	JLabel brandLabel = new JLabel("Which brand do you prefer?");
	JLabel budgetLabel = new JLabel("What is your budget?");
	JLabel displayLabel = new JLabel("What screen size?");
	JLabel softwareLabel = new JLabel("Which operating system?");

	//create the button to take the user to the weighting's panel
	JButton weightingsButton = new JButton("Weighting's Panel");

	//create the radio buttons for the options
	JRadioButton[] brandRadioButtonArray = new JRadioButton[8];
	JRadioButton[] budgetRadioButtonArray = new JRadioButton[4];
	JRadioButton[] displayRadioButtonArray = new JRadioButton[4];
	JRadioButton[] softwareRadioButtonArray = new JRadioButton[6];

	//creating the button groups to account for the multiple buttons
	ButtonGroup budgetButtonGroup = new ButtonGroup();
	ButtonGroup brandButtonGroup = new ButtonGroup();
	ButtonGroup displayButtonGroup = new ButtonGroup();
	ButtonGroup softwareButtonGroup = new ButtonGroup();

	// This method...
	public LaptopAdviserGUIUserRatings() {

		userRatingsPanelSetup();
		frameSetup();

	}

//This method...
	private void userRatingsPanelSetup() {

		//set the bounds for the Jpanels
		userRatingsPanel0.setBounds(100, 50, 230, 300);
		userRatingsPanel0.setLayout(null);
		userRatingsPanel1.setBounds(350, 50, 230, 300);
		userRatingsPanel1.setLayout(null);
		userRatingsPanel2.setBounds(650, 50, 230, 300);
		userRatingsPanel2.setLayout(null);
		userRatingsPanel3.setBounds(950, 50, 230, 300);
		userRatingsPanel3.setLayout(null);

		//Set the bounds and size for the title
		title.setBounds(605, 25, 500, 20);
		title.setFont(new Font("Serif", Font.BOLD, 18));
		title.setForeground(Color.blue);
		add(title);

		//Setting the bounds and size for the option titles
		brandLabel.setBounds(180, 110, 175, 20);
		add(brandLabel);
		budgetLabel.setBounds(430,110, 175, 20);
		add(budgetLabel);
		displayLabel.setBounds(700, 110, 175, 20);
		add(displayLabel);
		softwareLabel.setBounds(1000, 110, 175, 20);
		add(softwareLabel);

		//allows for there to be various buttons for each label
		setupRadioButtons();

		//setting up the size and coordinates for the weightings panel button
		weightingsButton.setBounds(575, 575, 200, 50);
		add(weightingsButton);
		weightingsButton.addActionListener(this);

	}

	private void frameSetup() {

		//sets up the JFram
		setSize(1280,720);
		setLayout(null);

		// adds the Jpanels
		add(userRatingsPanel0);
		add(userRatingsPanel1);
		add(userRatingsPanel2);
		add(userRatingsPanel3);

		setVisible(true);

	}

	private void setupRadioButtons() {

		//sets up the radio buttons for brand
		brandRadioButtonArray[0] = new JRadioButton("HP");
		brandRadioButtonArray[1] = new JRadioButton("Dell");
		brandRadioButtonArray[2] = new JRadioButton("Apple");
		brandRadioButtonArray[3] = new JRadioButton("Lenovo");
		brandRadioButtonArray[4] = new JRadioButton("Asus");
		brandRadioButtonArray[4] = new JRadioButton("Kano");
		brandRadioButtonArray[5] = new JRadioButton("Microsoft");
		brandRadioButtonArray[6] = new JRadioButton("Acer");
		brandRadioButtonArray[7] = new JRadioButton("MSI");

		for (int index = 0; index < brandRadioButtonArray.length; index++) {
			brandButtonGroup.add(brandRadioButtonArray[index]);
			brandRadioButtonArray[index].setBounds(75, 100 + index * 25, 300, 25);
			userRatingsPanel0.add(brandRadioButtonArray[index]);
			brandRadioButtonArray[index].addActionListener(this);
		}

		//sets up the radio buttons for brand
		budgetRadioButtonArray[0] = new JRadioButton("Less than $500");
		budgetRadioButtonArray[1] = new JRadioButton("$500 to less than $1000");
		budgetRadioButtonArray[2] = new JRadioButton("$1000 to less than $2000");
		budgetRadioButtonArray[3] = new JRadioButton("$2000 or more");

		for (int index = 0; index < budgetRadioButtonArray.length; index++) {
			budgetButtonGroup.add(budgetRadioButtonArray[index]);
			budgetRadioButtonArray[index].setBounds(75, 100 + index * 25, 300, 25);
			userRatingsPanel1.add(budgetRadioButtonArray[index]);
			budgetRadioButtonArray[index].addActionListener(this);
		}

		//sets up radio buttons for display
		displayRadioButtonArray[0] = new JRadioButton("Less than 14 inches");
		displayRadioButtonArray[1] = new JRadioButton("14 inches");
		displayRadioButtonArray[2] = new JRadioButton("15.6 inches");
		displayRadioButtonArray[3] = new JRadioButton("16 inches or more");

		for (int index = 0; index < displayRadioButtonArray.length; index++) {
			displayButtonGroup.add(displayRadioButtonArray[index]);
			displayRadioButtonArray[index].setBounds(75, 100 + index * 25, 300, 25);
			userRatingsPanel2.add(displayRadioButtonArray[index]);
			displayRadioButtonArray[index].addActionListener(this);
		}

		//sets up radio buttons for software
		softwareRadioButtonArray[0] = new JRadioButton("Windows 10 home");
		softwareRadioButtonArray[1] = new JRadioButton("Windows 10 pro");
		softwareRadioButtonArray[2] = new JRadioButton("Windows 10 S");
		softwareRadioButtonArray[3] = new JRadioButton("Chrome OS");
		softwareRadioButtonArray[4] = new JRadioButton("Mac OS");
		softwareRadioButtonArray[5] = new JRadioButton("null");
		for (int index = 0; index < softwareRadioButtonArray.length; index++) {
			softwareButtonGroup.add(softwareRadioButtonArray[index]);
			softwareRadioButtonArray[index].setBounds(75, 100 + index * 25, 300, 25);
			userRatingsPanel3.add(softwareRadioButtonArray[index]);
			softwareRadioButtonArray[index].addActionListener(this);
		}
	}

	//creates methods for each of the radio buttons to rate various specs and features of the computers 
	//in the csv file
	public void actionPerformed(ActionEvent event) {

		for (int index = 0; index < brandRadioButtonArray.length; index++)
			if (event.getSource() == brandRadioButtonArray[index])
				setBrandRating(index);

		for (int index = 0; index < budgetRadioButtonArray.length; index++)
			if (event.getSource() == budgetRadioButtonArray[index])
				setBudgetRating(index);

		for (int index = 0; index < displayRadioButtonArray.length; index++)
			if (event.getSource() == displayRadioButtonArray[index])
				setDisplayRating(index);

		for (int index = 0; index < softwareRadioButtonArray.length; index++)
			if (event.getSource() == softwareRadioButtonArray[index])
				setSoftwareRating(index);

		if (event.getSource() == weightingsButton) {
			setVisible(false);
			new LaptopAdvisorGUIUserWeightings();
		}

	}

	// method for brand rating
	private void setBrandRating(int choice) {

		for (int index = 0; index < LaptopAdvisorApplication.laptopArray.length; index++) {

			// HP
			if (choice == 0) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("HP"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;
			}

			// Dell
			if (choice == 1) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("Dell"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;
			}
			// Apple
			if (choice == 2) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("Apple"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;
			}
			// Lenovo
			if (choice == 3) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("Lenovo"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;

			}

			// Asus
			if (choice == 4) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("Asus"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;

			}

			//Kano
			if (choice == 5) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("Kano"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;
			}
			
			//Microsoft
			if (choice == 6) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("Microsoft"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;
			}
			
			//Acer
			if (choice == 7) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("Acer"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;
			}

			//MSI
			if (choice == 8) {
				if (LaptopAdvisorApplication.laptopArray[index].getBrand().equals("MSI"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[4] = 5;
			}

		}

	}

	//method for budget rating
	private void setBudgetRating(int choice) {

		//
		for (int index = 0; index < LaptopAdvisorApplication.laptopArray.length; index++) {

			// low budget is best
			if (choice == 0) {
				if (LaptopAdvisorApplication.laptopArray[index].getPrice() < 500)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getPrice() < 1000)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 0;
			}

			// $500 to less than $1000
			if (choice == 1) {
				if (LaptopAdvisorApplication.laptopArray[index].getPrice() > 500
						&& LaptopAdvisorApplication.laptopArray[index].getPrice() < 1000)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getPrice() > 1000
						&& LaptopAdvisorApplication.laptopArray[index].getPrice() < 2000
						|| LaptopAdvisorApplication.laptopArray[index].getPrice() < 500)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 0;
			}

			// $1000 - $2000
			if (choice == 2) {
				if (LaptopAdvisorApplication.laptopArray[index].getPrice() > 1000
						&& LaptopAdvisorApplication.laptopArray[index].getPrice() < 2000)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getPrice() < 1000
						&& LaptopAdvisorApplication.laptopArray[index].getPrice() > 500
						|| LaptopAdvisorApplication.laptopArray[index].getPrice() > 2000)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 0;
			}

			// $2000 +
			if (choice == 3) {
				if (LaptopAdvisorApplication.laptopArray[index].getPrice() > 2000)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getPrice() > 500
						&& LaptopAdvisorApplication.laptopArray[index].getPrice() < 2000)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 0;
			}

		}

	}

	//method for display rating
	private void setDisplayRating(int choice) {

		for (int index = 0; index < LaptopAdvisorApplication.laptopArray.length; index++) {

			// less than 14
			if (choice == 0) {
				if (LaptopAdvisorApplication.laptopArray[index].getDisplay() < 14)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getDisplay() == 14)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 10;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 5;
			}

			// 14 inches
			if (choice == 1) {
				if (LaptopAdvisorApplication.laptopArray[index].getDisplay() == 14)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getDisplay() == 15.6)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 10;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 5;
			}

			// 15.6 inches
			if (choice == 2) {
				if (LaptopAdvisorApplication.laptopArray[index].getDisplay() == 15.6)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getDisplay() == 14
						|| LaptopAdvisorApplication.laptopArray[index].getDisplay() == 16)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 10;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 5;
			}

			// 16 inches or more
			if (choice == 3) {
				if (LaptopAdvisorApplication.laptopArray[index].getDisplay() >= 16)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 20;
				else if (LaptopAdvisorApplication.laptopArray[index].getDisplay() == 15.6)
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 10;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[6] = 5;
			}

		}

	}

	//method for software rating
	private void setSoftwareRating(int choice) {

		for (int index = 0; index < LaptopAdvisorApplication.laptopArray.length; index++) {

			// windows 10 home
			if (choice == 0) {
				if (LaptopAdvisorApplication.laptopArray[index].getSoftware().contains("Windows 10 Home"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
			}

			// windows 10 pro
			if (choice == 1) {
				if (LaptopAdvisorApplication.laptopArray[index].getSoftware().contains("Windows 10 Pro"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
			}

			// windows 10 S
			if (choice == 2) {
				if (LaptopAdvisorApplication.laptopArray[index].getSoftware().contains("Windows 10 S"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
			}
			// Chrome OS
			if (choice == 3) {
				if (LaptopAdvisorApplication.laptopArray[index].getSoftware().contains("Chrome OS"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
			}
			
			//MacOS
			if (choice == 4) {
				if (LaptopAdvisorApplication.laptopArray[index].getSoftware().contains("MacOs"))
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 20;
				else
					LaptopAdvisorApplication.laptopArray[index].getRatings()[5] = 5;
		}
			
		}
		
	}
	
}



