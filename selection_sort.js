a = [50,32,2,77,25]
array_len = a.length;
for(i=0; i<array_len;i++)
{   
  var min = i;
  for(j=i+1; j< array_len;j++)
  {
	if(a[j]<a[min])
	{
		min=j;
	}
  }
  if(i!=j)
  {
   var temp = a[i];
   a[i] =a[min];
   a[min] =temp;
   }
}
console.log(a);