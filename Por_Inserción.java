public class Por_Inserción
 {
    public Por_Inserción() 
    {
        // Constructor vacío
    }

    public static void main(String[] args) 
    {
        insertionSort(new int[] { 5, 3, 6, 2, 10 });
    }

    public static void insertionSort(int[] arr) 
    {
        double temp;
        int i, j;
        int n = arr.length;
        for (i = 1; i < n; i++) 
        {
            temp = arr[i];
            for (j=i;(j>0) && (arr[j-1]>temp);j--)
            {
                arr[j] = arr[j-1];
            }
        }

        // Imprimir el arreglo ordenado
        for (int num : arr) 
        {
            System.out.print(num + " ");
        }
    }
    
}
