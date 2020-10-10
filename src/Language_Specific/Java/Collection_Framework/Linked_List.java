import java.util.*;

public class Linked_List {
    public static void main(String[] args){

        LinkedList <String> list = new LinkedList<String>();
        
        list.add("One");
        list.add("Two");
        list.add("Three");
        list.add("Four");
        list.add("Five");

        System.out.println(list);
        System.out.println("-----------");

        list.addFirst("First");
        System.out.println(list);
        System.out.println("-----------");

        list.addLast("Last");
        System.out.println(list);
        System.out.println("-----------");

        list.removeLast();
        System.out.println(list);
        System.out.println("-----------");

        list.removeFirst();
        System.out.println(list);
        System.out.println("-----------");

        System.out.println(list.getFirst());
        System.out.println("-----------");

        System.out.println(list.getLast());
        System.out.println("-----------");
    }
}
