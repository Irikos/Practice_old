/**
* Author: Irikos
* Taking back my programming!
* rewritting Linked Lists: aiming for readable code and no errors on first compile
* didn't compile on the first try due to a typo-like error, but was close
* works like a charm!
* listCount is not needed. The for(int i = 1; i < listCount; i++) can be easily replaced with while(head.getNext() != null)
*/
//import java.lang.IndexOutofBoundsException; // could make use of this.

class Node {
  private Node next;
  private Object data;
  Node() {
    data = null;
  }
  Node(Object dataValue) {
    data = dataValue;
  }

  public Object getData() {
    return data;
  }

  public void setData(Object dataValue) {
    data = dataValue;
  }
  public Node getNext() {
    return next;
  }
  public void setNext(Node nextValue) {
    next = nextValue;
  }
}

class LinkedList {
  private Node head;
  private int listCount;
  LinkedList() {
    listCount = 0;
  }
  LinkedList(Node nodeValue) {
    head = nodeValue;
    listCount = 1;
  }
  LinkedList(Object nodeDataValue) {
    head = new Node(nodeDataValue);
    listCount = 1;
  }
  void addNode(Node nodeValue) {
    if(listCount == 0)
      head = nodeValue;
    else {
      Node tempHead = head;
      for(int i = 1; i < listCount; i++) // same as while(tempHead.getNext() != null)
        tempHead = tempHead.getNext();
      tempHead.setNext(nodeValue);
    }
    listCount++;
  }
  void addNode(Object dataValue) {
    if(listCount == 0)
      head = new Node(dataValue);
    else {
      Node tempNode = new Node(dataValue);
      Node tempHead = head;
      for(int i = 1; i < listCount; i++) // same as while(tempHead.getNext() != null)
        tempHead = tempHead.getNext();
      tempHead.setNext(tempNode);
    }
    listCount++;
  }
  void addNodeAtIndex(Node nodeValue, int indexValue) {
    // check for all cases
    if(listCount < (indexValue - 1) || indexValue < 0) System.out.println("index out of bounds"); // you can add at maximum the next position after last
    else
      if(indexValue == 0 && listCount == 0) {
        head = nodeValue;
        listCount++;
      }
      else
        if(indexValue == 0 && listCount > 0) {
          nodeValue.setNext(head);
          head = nodeValue;
          listCount++;
        }
        else {
          if(indexValue > 0 && listCount > 0) {
            Node tempHead = head;
            for(int i = 1; i < indexValue; i++)
              tempHead = tempHead.getNext();
            nodeValue.setNext(tempHead.getNext());
            tempHead.setNext(nodeValue);
            listCount++;
          }
        }
  }
  void addNodeAtIndex(Object dataValue, int indexValue) {
    // check for all cases
    if(listCount < (indexValue - 1) || indexValue < 0) System.out.println("index out of bounds"); // you can add at maximum the next position after last
    else
      if(indexValue == 0 && listCount == 0) {
        head = new Node(dataValue);
        listCount++;
      }
      else
        if(indexValue == 0 && listCount > 0) {
          Node tempNode = new Node(dataValue);
          tempNode.setNext(head);
          head = tempNode;
          listCount++;
        }
        else {
          if(indexValue > 0 && listCount > 0) {
            Node tempNode = new Node(dataValue);
            Node tempHead = head;
            for(int i = 1; i < indexValue; i++)
              tempHead = tempHead.getNext();
            tempNode.setNext(tempHead.getNext());
            tempHead.setNext(tempNode);
            listCount++;
          }
        }
  }
  Node removeAtIndex(int indexValue) {
    // should throw exception here
    if(listCount == 0) {
      System.out.println("List is already empty");
      return null;
    }
    else
      if(listCount < indexValue || indexValue < 0) {
        System.out.println("index out of bounds");
        return null;
      }
      else
        /* // I think it's redundant
        if(indexValue == 0 && listCount == 1) {
          head = null;
          listCount--;
        }
        else
        */
        if(indexValue == 0 && listCount > 0) {
          Node returnNode = head;
          head = head.getNext(); // sets to null if head is the only element.
          listCount--;
          return returnNode;
        }
        else
          if(indexValue > 0 && listCount > 0) {
            Node tempHead = head;
            for(int i = 1; i < indexValue; i++)
              tempHead = tempHead.getNext();
            Node returnNode = tempHead.getNext();
            tempHead.setNext(tempHead.getNext().getNext()); // if removing last item, this is null
            listCount--;
            return returnNode;
          }
      System.out.println("If you got here, something went wrong (a uncovered case)");
      return null;
  }
  Node removeHead() {
    return removeAtIndex(0);
  }
  Node removeTail() {
    return removeAtIndex(listCount - 1);
  }
  void printTheList() {
    Node tempHead = head;
    for(int i = 1; i < listCount; i++) {
      System.out.print(tempHead.getData() + " -> ");
      tempHead = tempHead.getNext();
    }
    System.out.print(tempHead.getData());
    System.out.println();
  }

  public static void main(String arg[]) {
    Node n1 = new Node(1);
    Node n2 = new Node(2);
    Node n3 = new Node(3);
    Node n4 = new Node(4);
    Node n5 = new Node(5);
    Node n6 = new Node(6);
    LinkedList LL = new LinkedList(n1);
    LL.addNode(n2);
    LL.addNode(n3);
    LL.addNode(n4);
    LL.addNode(5);
    LL.addNodeAtIndex(-1, 0);
    LL.addNodeAtIndex(-4, 4);
    LL.addNodeAtIndex(-6, 7);
    LL.addNodeAtIndex(n6, 8);
    LL.printTheList();
    LL.removeAtIndex(1);
    LL.printTheList();
    LL.removeHead();
    LL.printTheList();
    LL.removeTail();
    LL.printTheList();
  }
}
