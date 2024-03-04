public class Por_Selección 
{
    public Por_Selección() 
    {
        // Constructor vacío
    }

    public static void main(String[] args) 
    {
        selectionOrder(new int[] { 5, 3, 6, 2, 10 });
    }

    public static void selectionOrder(int[] arr) 
    {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) 
        {
            int min = i;
            for (int j = i + 1; j < n; j++) 
            {
                if (arr[j] < arr[min]) {
                    min = j;
                }
            }
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }

        // Imprimir el arreglo ordenado
        for (int num : arr) 
        {
            System.out.print(num + " ");
        }
    }
}
