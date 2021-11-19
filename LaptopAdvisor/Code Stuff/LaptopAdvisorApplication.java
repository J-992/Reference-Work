/*
 * Names: Jaffer Razavi, Pierce Pokorny, Daniel Ling
 * Date: Jan 19, 2021
 * ICS3U
 * Mr. Fernandes
 * Title: Laptop Advisor
 * Description:
 * 		This project will assist a person who is looking to purchase a laptop
 * 		It will askthem certain questions that will halp find the best laptop
 * 		suited for their needs.  
 * 
 * Added Features: Colours, fonts, borders, 
 * 
 * Major Skills: 
 * 	arrays
 * 	Swing GUI components
 * 	File Input
 * 	GUIs
 * 	weighted decision matrixes
 * 
 * Areas of concern: none
 */

/*
 * This class runs the file input class and the user ratings class
 *
 * author - Jaffer Razavi
 */


public class LaptopAdvisorApplication {

// A list of laptops that is read from an external csv file into a ‘global’ array that is used by the rest 
// of the classes in the program
	public static Laptop[] laptopArray = new Laptop[30];
	public static User user = new User();

//used to run the File Input and User Ratings GUI
	public static void main(String[] args) {

		new LaptopAdvisorFileInput();
		new LaptopAdvisorGUIUserRatings();

	}

}
