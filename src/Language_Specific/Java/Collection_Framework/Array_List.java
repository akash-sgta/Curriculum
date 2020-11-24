import java.util.*;
import java.util.Iterator;

public class Array_List{
    public static void main(String[] args){
        List <String> list = new ArrayList <String>();
        // ArrayList <String> list = new ArrayList <String>(); also works
        // <...> are generics

        list.add("One");
        list.add("Two");
        list.add("Three");
        list.add("Four");
        list.add("Five");


        Iterator <String> itr;

        itr = list.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
        System.out.println("-----------");

        System.out.println(list.get(2));
        System.out.println("-----------");
        
        list.set(0, "Changes");

        itr = list.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
        System.out.println("-----------");

        list.remove(0);
        itr = list.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
        System.out.println("-----------");

        System.out.println(list);
        System.out.println("-----------");

        list.clear();
    }
}