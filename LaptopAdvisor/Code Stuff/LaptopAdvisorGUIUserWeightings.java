import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenuBar;
import javax.swing.JPanel;
import javax.swing.border.Border;

/*
* This class is the user weightings gui class
* 	it asks the user questions to help 
* 	find the laptop bset suited for their needs
*
* author - Jaffer Razavi
*/
@SuppressWarnings("serial")
public class LaptopAdvisorGUIUserWeightings extends JFrame implements ActionListener {

	// Fields or Instance Variables

	JPanel userWeightingsPanel = new JPanel();
	JPanel reportPanel = new JPanel();
	JLabel userWeightingsLabel = new JLabel();
	JButton reportButton = new JButton("test");
	JMenuBar menubar = new JMenuBar();
	JLabel[] weightingLabelArray = new JLabel[8];
	@SuppressWarnings("rawtypes")
	JComboBox[] weightingComboBoxArray = new JComboBox[8];
	Border border = BorderFactory.createLineBorder(Color.BLACK, 15);
	Border buttonBorder = BorderFactory.createLineBorder(Color.DARK_GRAY, 5);

	// this method sets up the user weightings window
	public LaptopAdvisorGUIUserWeightings() {

		userWeightingsPanelSetup();
		frameSetup();

	}

	// This method sets up the user weightings panel
	private void userWeightingsPanelSetup() {

		// sets up panel that holds the dropdown boxes
		userWeightingsPanel.setBounds(0, 0, 1235, 500);
		userWeightingsPanel.setLayout(null);
		userWeightingsPanel.setBackground(Color.GRAY);
		userWeightingsPanel.setBorder(border);

		// sets the bounds of the text boxes
		userWeightingsLabel.setBounds(575, 25, 200, 25);
		userWeightingsPanel.add(userWeightingsLabel);

		// calls the method that creates the dropdown boxes
		setupComboBoxes();

		// sets up report button
		reportButton.setBounds(525, 515, 200, 50);
		reportButton.setBackground(Color.lightGray);
		reportButton.setBorder(buttonBorder);
		add(reportButton);

		reportButton.addActionListener(this);

		// sets up the panel that holds the report button
		reportPanel.setBounds(0, 480, 1235, 120);
		reportPanel.setBackground(Color.GRAY);
		reportPanel.setBorder(border);

		add(reportPanel);
	}

	// sets up frame
	private void frameSetup() {

		// sets up frame
		setSize(1250, 640);
		setLayout(null);
		setBackground(Color.black);
		setResizable(false);

		// creates a menubar
		setJMenuBar(menubar);

		// adds the user weightings panel to the jframe
		add(userWeightingsPanel);

		// makes the jrame visible
		setVisible(true);

	}

	@SuppressWarnings("unchecked")
	// this method sets up the dropdown boxes
	private void setupComboBoxes() {

		// weighting labels
		weightingLabelArray[0] = new JLabel("1. How important is the Brand?");
		weightingLabelArray[1] = new JLabel("2. How important is the CPU?");
		weightingLabelArray[2] = new JLabel("3. How important is the Graphics Card?");
		weightingLabelArray[3] = new JLabel("4. How important is the Screen Size?");
		weightingLabelArray[4] = new JLabel("5. How important is the Budget?");
		weightingLabelArray[5] = new JLabel("6. How important is the Screen Size?");
		weightingLabelArray[6] = new JLabel("7. How important is the Operating System");
		weightingLabelArray[7] = new JLabel("8. How important is the RAM");

		// adds half of the weighting array to this variable
		int half = weightingLabelArray.length / 2;

		// adds the dropdown boxes under the questions
		for (int index = 0; index < weightingLabelArray.length; index++) {
			
			//sets font for 
			weightingLabelArray[index].setFont(new Font("SansSerif", Font.BOLD, 12));

			// adds the dropdown boxes
			if (index < half) {
				weightingLabelArray[index].setBounds(50 + index * 300, 100, 250, 25);
			} else
				weightingLabelArray[index].setBounds(50 + (index - half) * 300, 300, 250, 25);

			userWeightingsPanel.add(weightingLabelArray[index]);

			// creates the dropdown boxes
			weightingComboBoxArray[index] = new JComboBox<Integer>();
			weightingComboBoxArray[index].addActionListener(this);
			
			//sets background of dropdown boxes
			weightingComboBoxArray[index].setForeground(Color.WHITE);
			
			//sets font colour of dropdown boxes
			weightingComboBoxArray[index].setBackground(Color.GRAY);


			if (index < half)
				weightingComboBoxArray[index].setBounds(50 + index * 300, 150, 250, 25);
			else
				weightingComboBoxArray[index].setBounds(50 + (index - half) * 300, 350, 250, 25);

			userWeightingsPanel.add(weightingComboBoxArray[index]);

			// creates options from 1-10 in the dropdown boxes
			for (int value = 0; value <= 10; value++)
				weightingComboBoxArray[index].addItem(value);

		}

	}

	//
	public void actionPerformed(ActionEvent event) {

		//
		for (int index = 0; index < weightingComboBoxArray.length; index++) {

			if (event.getSource() == weightingComboBoxArray[index]) {
				LaptopAdvisorApplication.user.getWeighting()[index] = weightingComboBoxArray[index].getSelectedIndex();
				System.out.println(LaptopAdvisorApplication.user.getWeighting()[index]);
				break;

			}

		}

		//
		if (event.getSource() == reportButton) {
			setVisible(false);
			new LaptopAdvisorGUIReport();
		}

	}

}
