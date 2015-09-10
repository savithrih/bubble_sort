// var a=[2,5,3,1,15]
function bubble_sort(a)
{ 
var temp =0;
for(j=0; j< a.length; j++)
{  
	for(i=0; i< a.length; i++)
	{
	if(a[i]>a[i+1])
	{
	temp = a[i];
	a[i]=a[i+1];
	a[i+1]=temp;
    }
   }
}
}
bubble_sort(a=[2,5,3,1,15])
console.log(a);