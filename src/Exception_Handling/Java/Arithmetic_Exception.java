import java.io.*;
/*
throws Exception - the module is not responsible for handling the specific exceptions,
                    or you can handle it using a catch block.
*/
public class Arithmetic_Exception {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int i=10, j=0, k=0;
        k = Integer.parseInt(br.readLine());
        try{
            j = i/k;
        }
        catch(Exception e){
            System.out.println("E : " + e);
        }
        System.out.println("OP : " + j);
    }
}
