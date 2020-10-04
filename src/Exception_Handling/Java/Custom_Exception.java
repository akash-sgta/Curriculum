class Custom extends Exception{

    public Custom(String message){
        super(message);
    }
}
/*
throw new Exception("...") - explicitly throw an exception to be either handled or passed.
*/
public class Custom_Exception {
    public static void main(String[] args){
        try{
            throw new Custom("Custom Error");
        }
        catch(Exception e){
            System.out.println("E : " + e);
        }
    }
}
