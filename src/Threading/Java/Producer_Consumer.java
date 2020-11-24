import java.lang.Math;

class Product{
    private int product = 0;

    public int get_product(){
        return this.product;
    }

    public synchronized void get_product(String name, int query){
        int val = 0, starve = 0, stock = this.product;
        if(this.product <= query){
            val = this.product;
            starve = query-this.product;
            this.product = 0;
        }else{
            val = query;
            this.product = this.product-query;
        }
        System.out.println(name+" : Require-"+query+" | Stock-"+stock+" | Get-"+val+" | Starve-"+starve);
    }

    public synchronized void put_product(String name, int query){
        this.product = this.product + query;
        System.out.println(name+" : Add-"+query+" | Stock-"+this.product);
    }
}

class Producer extends Thread{
    
    private String name;
    private Product p_ref;

    public Producer(Product p_ref, String name){
        this.p_ref = p_ref;
        this.name = name;
    }

    public void run(){
        int i, f;
        for(i=0; i<10; i++){
            f = (int)(Math.random()*10) + 1;
            this.p_ref.put_product(this.name,f);
        }
    }
}

class Consumer extends Thread{
    
    private String name ;
    private Product p_ref;

    public Consumer(Product p_ref, String name){
        this.p_ref = p_ref;
        this.name = name;
    }

    public void run(){
        int i, f;
        for(i=0; i<10; i++){
            f = (int)(Math.random()*10) + 5;
            this.p_ref.get_product(this.name,f);
        }
    }
}

public class Producer_Consumer{

    public static void main(String[] args)throws Exception{
        Product product_ref = new Product();
        Producer producer_ref = new Producer(product_ref, "Producer");
        Consumer consumer_ref = new Consumer(product_ref, "Consumer");

        System.out.println("Products : "+product_ref.get_product());

        producer_ref.start();
        consumer_ref.start();
        /*
        In case of implements Runnable;
        Eg:
        Producer p_ref = new Producer(...);  implements Runnable
        Thread t = new Thread(p_ref); other wise it would be a part of main thread
        t.start();
        */
        producer_ref.join();
        consumer_ref.join();

        System.out.println("Products : "+product_ref.get_product());
    }
}