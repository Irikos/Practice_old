package hello;

public class Greeting {
  private final long id;
  private final String content;
  private final int seconds;
  private final String myDate;

  public Greeting(long id, String content, int seconds, String myDate) {
    this.id = id;
    this.content = content;
    this.seconds = seconds;
    this.myDate = myDate;
  }

  public long getId() {
    return this.id;
  }

  public String getContent() {
    return this.content;
  }

  public int getSeconds() {
    return this.seconds;
  }

  public String getMyDate() {
    return this.myDate;
  }

}
