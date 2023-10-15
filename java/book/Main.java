import java.util.Scanner;

/* The following program accepts the following information about a book:
*   - Author first and last name
*   - Book title
*   - Book summary
* The program uses a series of getter and setter methods to get and provide this information.
* The getter and setter methods are defined in Book.java. */

public class Main {

    public static void main(String[] args) {
        // Create new book object.
        Book book = new Book();
        // Get user input and use setter methods to gather information about the book object.
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is the author's last name?");
        String newLastName = scanner.nextLine();
        book.setLastName(newLastName);
        System.out.println("What is the author's first name?");
        String newFirstName = scanner.nextLine();
        book.setFirstName(newFirstName);
        System.out.println("What is the title of the author's book?");
        String newTitle = scanner.nextLine();
        book.setTitle(newTitle);
        System.out.println("What is the summary of the author's book?");
        String newSummary = scanner.nextLine();
        book.setSummary(newSummary);
        scanner.close();
        // Get the gathered information with getter methods and print the book information.
        System.out.println("You entered:\nAuthor: " + book.getFirstName() + " " + book.getLastName());
        System.out.println("Title: " + book.getTitle());
        System.out.println("Summary: " + book.getSummary());
        }
    }
