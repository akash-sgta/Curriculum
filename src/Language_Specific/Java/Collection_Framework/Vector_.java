import java.util.*;

public class Vector_ {
    public static void main(String[] args){
        
        Vector <String> v = new Vector<String>(3, 2);
        // initial size 3
        // increment with 2
        v.addElement("One");
        v.addElement("Two");
        v.addElement("Three");
        v.addElement("Four");
        v.addElement("Five");

        System.out.println(v.capacity());
        System.out.println("-----------");

        v.addElement("Six");
        System.out.println(v.capacity());
        System.out.println("-----------");

        System.out.println(v);
        System.out.println("-----------");

        Iterator <String> itr;

        itr = v.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
        System.out.println("-----------");

    }
}
