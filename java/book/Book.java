import java.util.Scanner;
public class Book {

    // Declare private variables that the getter and setter methods will use.
    private String lastName;
    private String firstName;
    private String title;
    private String summary;

    // Define getter methods.
    public String getLastName() {
        return lastName;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getTitle() {
        return title;
    }

    public String getSummary() {
        return summary;
    }

    // Define setter methods.
    public void setLastName(String newLastName) {
        this.lastName = newLastName;
    }

    public void setFirstName(String newFirstName) {
        this.firstName = newFirstName;
    }

    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    public void setSummary(String newSummary) {
        this.summary = newSummary;
    }

}
