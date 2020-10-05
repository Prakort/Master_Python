public class book {
  String name;
  String author;
  int page;
  int counter = 0;

  public book() {
  }

  public void setName(String name) {
    if (name.length() > 0)
      this.name = name;

  }

  public static void main(String[] args) {
    book b1 = new book();
    b1.name = "";
    b1.name = " hell wold! ";

  }
}
