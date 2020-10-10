class Test<T>{
    T obj;
    public Test(T obj){
        this.obj = obj;
    }
    public T getObj(){
        return this.obj;
    }
}

public class Generics_ {
    public static void main(String[] args){
        
        Test <String> obj1 = new Test <String>("OggaBogga");
        System.out.println(obj1.getObj());
        System.out.println("-----------");
        
        Test <Boolean> obj2 = new Test <Boolean>(false);
        System.out.println(obj2.getObj());
    }
}
