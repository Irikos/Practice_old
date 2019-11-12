package hello;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Quote {
  private String type;
  private Value value;

  public Quote() {

  }

  public Value getValue() {
    return this.value;
  }

  public void setValue(Value value) {
    this.value = value;
  }

  public String getType() {
    return this.type;
  }

  public void setType(String type) {
    this.type = type;
  }

  @Override
  public String toString() {
    return "Quote{" + "type = '" + type + "\'" + ", value = " + value + "}";
  }
}
