#include <stdio.h>
#include <stdlib.h>
#include <time.h>
struct pnode{
	struct pnode* prev;
	int data;
	struct pnode* next;	
};

void push(struct pnode** ptrptr,int Data){
	struct pnode* new_node=malloc(sizeof(struct pnode));		//pointer referansi verilen pointera eklemek icin heapte yeni bir dugum olusturuyoruz.
	
	if((*ptrptr)==NULL){										//eger gelen pointer referansi NULL ise(bos ise) yeni dugumu head olarak ekliyoruz. 
		new_node->prev=NULL;									//yeni dugumun ondan onceki dugumu gosteren pointerina NULL degerini veriyoruz.
		new_node->data=Data;									//yeni dugumun verisini atiyoruz.
		new_node->next=NULL;									//yeni dugumun sonraki dugumu gosteren pointerina NULL(bos/yok) atiyoruz.
		(*ptrptr)=new_node;										//head referansi gonderilen linkedlistin head pointerina yeni dugumu atiyoruz.
	}															
		
	else{														//eger gelen head pointer referansi NULL degilse(yani listenin headi var ise)
		new_node->prev=(*ptrptr)->prev;							//yeni dugumun ondan onceki dugumu gosteren pointerina,parametre olarak verilen 
																//pointer referansinin oncekini gosteren pointerini atiyoruz.
																// Aslinda direk NULL da olabilirdi(sadece basa ekleme amacli kullanilacaksa) ama &(dugum->next)
																//seklinde kullanilabilmesi icin bu sekilde olmali.
		
		(*ptrptr)->prev=new_node;								//head pointerin onceki dugumu gosteren pointerina yeni dugumu atiyoruz.
		new_node->next=(*ptrptr);								//yeni dugumun sonraki dugumu gosteren pointerina head(ilk bastaki dugumun pointerini) atiyoruz.
		new_node->data=Data;									//yeni dugumun verisini atiyoruz.
		(*ptrptr)=new_node;										//head pointerini (bas dugum) yeni dugumu gosterecek sekilde degistiriyoruz.
	}															//&(dugum->next) kullaniminda bu durum daha farkli oluyor.Head'i degil next'i degistirmis.
																//oluyoruz. 
}


struct pnode* random_list(int length,int min,int max){			//verilen uzunlukta ve aralikta rastgele sayilari iceren bir linkedlist olusturup head pointerini cagiriciya atiyor.
	struct pnode* new_head=NULL;		 						//yeni liste icin stackde bir pnode pointeri olusturuyoruz ve degerini NULL yapiyoruz(hicbir seyi gostermiyor). 
	int numbers[length],i;										//local(stackde) uzunlugunu parametreden alan sayi dizisi olusturuyoruz.for icin de i sayisini olusturuyoruz.
	random_generator(numbers,min,max,length);					//random_generator fonksiyonuna numbers pointerini yollayip bu diziyi rastgele sayilarla dolduruyoruz.
	for(i=0;i<length;i++)						
		push(&new_head,numbers[i]);								//numbers sayi dizisindeki rastgele sayilari sirayla headini olusturdugumuz linkedlistin basina aktariyoruz.
	return new_head;											//olusturdugumuz linkedlistin head pointerini cagiriciya atiyoruz.
}

void print_nodes(struct pnode* head){							//head pointeri yollanan linkedlisti ekrana yazdiriyor.	
	struct pnode* traveler=head;								//linkedlistte gezinecek olan yerel pointer.Fonksiyon bitince otomatik olarak silinmesi icin yerel tanimliyoruz.
	int index=0;												//dugumun indexini takip etmek icin sayi olusturuyoruz.
	while(traveler!=NULL){										//dugumlerin hepsi bitene kadar(son dugumu de yazip nextine geciyor ve degeri NULL oluyor)ekrana yaziyor.
		printf("%3d.index:\t%d\n",index,traveler->data);		//indexinin sayisi 3 genislikte yaziliyor.(4 basamakli sayilara kadar hizayi kormak icin).
		traveler=traveler->next;								//gezgini bir sonraki dugume kaydiriyoruz.
		++index;												//index sayisini 1 arttiriyoruz.
	}
}


void random_generator(int* ptr,int min,int max,int count){//pointeri yollanan listenin icine verilen adet kadar,verilen araliktaki rastgele sayilarla dolduruyor.
	int i;												  //for dongusu icin sayi olusturuyoruz.
	srand(time(0));										  //her calistirdimizda yeni sayilar uretmesi icin zamani su anki ana ayarliyoruz.
	for(i=0;i<count;i++){								  //adet kadar calisacak olan donguyu olusturuyoruz.
		ptr[i]=(rand() % (max - min + 1));				  //pointeri gelen sayi dizisine sirayla rastgele sayi atiyoruz.
	}													 
}


										/*  	    |-----------------------------------|
													|									|
													|  Yapmamizi istediginiz fonksiyon  |
													|				 |					|
													|	   	   		 |					|
													|			   \ | /				|
													|				\ /					|
													|-----------------------------------|			*/


char add_next_to(struct pnode* head){//Data eklenecek sayiyi,next_to hangi sayidan sonra eklenecegini,nTh_next_to ise
																		   //eger duplicates(tekrarlar) var ise kacincisindan sonra eklenecegini ifade ediyor.
	int data,next_to,nTh_next_to;
	printf("\nEklemek istediginiz sayi:\t");
	scanf("%d",&data);
	printf("Hangi sayidan sonra eklenecek:\t");
	scanf("%d",&next_to);
	printf("Kacinci %d ' dan sonra eklenecek(ilk index=0):\t",next_to);
	scanf("%d",&nTh_next_to);
	printf("\n\n----Listenin son hali----\n\n");
	
	struct pnode* traveler=head;										  //listeyi sirayla gezecek olan yerel pointeri olusturuyoruz.ve head pointerini atiyoruz.
	int count_indexof_next_to=0;									
	while(traveler!=NULL){												  //traveler pointerini bastan sona gezdirecek donguyu olusturuyoruz.
		if (traveler->data==next_to){									  //eger travelerin gosterdigi dugumun degeri next_to degeri ile ayni ise
			if (count_indexof_next_to==nTh_next_to){					  //eger istenilen indexteki next_to degeri ise donguyu bitiriyoruz.
				break;													  //Traveler artik istenilen indexteki next_to sayisini tutan dugumu
			}															  //gosteriyor.	
			++count_indexof_next_to;									  //eger istenilen indexe gelinmemis ise index sayacini 1 arttiriyoruz.	
		}
		traveler=traveler->next;										  //traveleri bir yana kaydiriyoruz.
	}
	push(&(traveler->next),data);										  //eklemek istedigimiz sayiyi istenilen indexteki next_to sayisini tutan dugumden
																	      //sonrasina dugum olarak ekliyoruz.
	print_nodes(head);													  //ekleme islemini yaptiktan sonra listeyi tekrar ekrana yazdiriyoruz.
	char event;															  //devam edilip edilmeyecegini kontrol etmek amacli bir karakter olusturuyoruz.
	printf("Devam etmek istiyor musunuz?(e/h)\t");							
	if(getch()=='e'){													  //eger basilan tus e(evet) ise 
		printf("e");													  //ekrana e yazdiriyoruz
		return 'e';														  //'e' karakterini cagiriciya aktariyoruz.
	}
	else{																  //eger basilan tus e degil ise
		printf("h\nKapatmak icin herhangi bir tusa basin");				  //mainin sonundaki getch()'i tamamlayip kapanmasi icin kullaniciyi bilgilendiriyoruz. 									
		return 'h';														  //'h' karakterini cagiriciya aktariyoruz.
	}
		
}																		  



int main(){
	struct pnode* head=NULL;
	int length,min,max;
	char event='e';						
	/*push(&head,1);									 
	push(&head,2);
	push(&head,3);
	print_nodes(head);									 //push fonksiyonunun dogru sekilde sonraki dugumu(*next) baglayip baglamadigini kontrol ediyoruz.
	head=random_list(4);
	print_nodes(head);									 //rastgele sayilari iceren linkedlistin duzgun olusturulup olusturulmadigini kontrol ediyoruz.
	printf("%d",head->next->next->prev->data); 		   	 //push fonksiyonunun dogru sekilde onceki dugumu(*prev) baglayip baglamadigini kontrol ediyoruz.*/
	
	printf("Rastgele sayilari icerecek bagli listenin uzunlugu:\t");
	scanf("%d",&length);								//uzunluk girdisini aliyoruz.
	printf("\nRastgele sayilarin alabilecegi en kucuk deger:\t");
	scanf("%d",&min);									//rastgele uretilecek sayilarin en kucuk degerini aliyoruz.
	printf("\nRastgele sayilarin alabilecegi en buyur deger:\t");
	scanf("%d",&max);									//rastgele uretilecek sayilarin en buyuk degerini aliyoruz.
	
	head=random_list(length,min,max);					//verilen uzunlukta ve aralikta rastgele sayilari iceren listeyi olusturup heade atiyoruz.
	print_nodes(head);									//olusturulan rastgele sayilarin oldugu listeyi ekrana yazdiriyoruz.
	while(add_next_to(head)=='e'){}						//ekleme yapmak istedikce devam eden donguyu olusturuyoruz.
	getch();											//tamamen kapatmak icin bir tusa daha basilmasini istiyoruz.
	return 1;											//maindeki butun islemler duzgun calisiyorsa program bittiginde donut olarak 1 aliyoruz.
}
