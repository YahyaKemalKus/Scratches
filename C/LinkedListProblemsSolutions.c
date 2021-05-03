#include <stdio.h>
#include <stdlib.h>

/* http://cslibrary.stanford.edu/105/LinkedListProblems.pdf icerisindeki sorularin kendimce cevaplarý*/

struct node{
	int data;
	struct node* next;
};

void push(struct node** head,int Data){//listenin basina(direk &head kullanilirsa) veya (&(dugum->next) kullanilirsa dugumden sonraki yere) dugum ekliyor.
	struct node* new_node=malloc(sizeof(struct node));
	new_node->data=Data;
	new_node->next=(*head);
	(*head)=new_node;
}


void add(struct node* head,int Data){
	struct node* traveler=head;
	while(traveler->next!=NULL){
		traveler=traveler->next;
	}
	push(&(traveler->next),Data);
}


int length(struct node* head){//listenin uzunlugunu donduruyor.
	struct node* tmp=head;
	int count=0;
	while(tmp!=NULL){
		count+=1;
		tmp=tmp->next;
	}
	return count;
}

struct node* copy_list(struct node* head){
	struct node* new_head,*tail,*first_node;
	struct node* traveler=head;
	
	first_node=malloc(sizeof(struct node));
	first_node->data=traveler->data;
	first_node->next=NULL;
	new_head=first_node;
	tail=first_node;
	
	while(traveler->next!=NULL){
		traveler=traveler->next;
		struct node* new_node=malloc(sizeof(struct node));
		tail->next=new_node;
		tail=new_node;
		new_node->data=traveler->data;
		new_node->next=NULL;
	}
	return new_head;
	
}

int getNth(struct node* head,int index){//verilen indexteki veriyi donduruyor.
	struct node* tmp=head;
	int i;
	for (i=0;i<index;i++){
		tmp=tmp->next;
	}
	return tmp->data;
}

void delete_list(struct node** head){//verilen listeyi komple siliyor.
	struct node* to_del,*traveler=(*head);
	while(traveler!=NULL){
		to_del=traveler;
		traveler=traveler->next;
		free(to_del);
	}
	(*head)=NULL;
}

int pop(struct node** head){//listenin basindaki dugumu siliyor.
	struct node* new_head=(*head);
	int popped_value=(*head)->data;
	new_head=new_head->next;
	free((*head));
	(*head)=new_head;
	return popped_value;
}

void insertNth(struct node** head,int index,int Data){//verilen indexe verilen veriyi aktariyor.
	struct node* new_node,*new_head,*previous_node=(*head);
	new_node=malloc(sizeof(struct node));
	if (index==0){
		new_node->data=Data;
		new_node->next=(*head);
		(*head)=new_node;
	}
	
	else{
		int i;
		for(i=0;i<index-1;i++){
			previous_node=previous_node->next;
		}
		new_node->data=Data;
		new_node->next=previous_node->next;
		previous_node->next=new_node;
	}
	
}

void SortedInsert(struct node** head,struct node* newNode){//kucukten buyuge sirali listeye verilen dugumu sirayi bozmayacak sekilde ekliyor.
	struct node* traveler=(*head),*previous_node=(*head);//eger en kucuk sayiydan 1 buyukse default olarak 1. dugumu(head) aliyor.degilse asagida kaydiriliyor.
	int greater_than=0,i;//greater_than dugumun baglanacagi indexi ifade ediyor.
	while (traveler!=NULL){
		if (traveler->data < newNode->data){
			greater_than+=1;
		}
		traveler=traveler->next;
	}
	
	if(greater_than==0){//en kucuk sayi ise basa yazilacagindan headle degistiriyoruz.
		newNode->next=(*head);
		(*head)=newNode;
	}
	else{//degilse greater_than degerinden yola cikarak indexleme islemi yapiyoruz ve olmasi gereken yere yaziyoruz.
		for(i=0;i<greater_than-1;i++){
		previous_node=previous_node->next;
		}
		newNode->next=previous_node->next;
		previous_node->next=newNode;
	}
}


void InsertSort(struct node** head){//verilen listeyi kucukten buyuge dogru siralayor ve heade tekrar aktariyor.Onceki sirasiz listeyi siliyor.
	struct node *new_head=NULL,*traveler=(*head);
	while(traveler!=NULL){
		struct node* new_node=malloc(sizeof(struct node));
		new_node->data=traveler->data;
		SortedInsert(&new_head,new_node);
		traveler=traveler->next;
	}
	delete_list(head);
	(*head)=new_head;	
}


void append(struct node** aRef,struct node** bRef){
	struct node* a_tail=(*aRef);
	while(a_tail->next!=NULL){
		a_tail=a_tail->next;
	}
	a_tail->next=(*bRef);
	(*bRef)=NULL;
}


void frontbacksplit(struct node* source,struct node** frontRef,struct node** backRef){
	if (length(source)==1){
		(*frontRef)=source;
	}
	
	else if (length(source)==2){
		(*frontRef)=source;
		(*backRef)=source->next;
		(*frontRef)->next=NULL;
		
	}
	
	else if (length(source)==3){
		(*frontRef)=source;
		(*backRef)=source->next->next;
		(*frontRef)->next->next=NULL;
	}
	
	else if (length(source)%2==0){
		int truncated_length=length(source)/2,i;
		struct node* f_end=source;
		for (i=1;i<truncated_length;i++){
			f_end=f_end->next;
		}
		(*frontRef)=source;
		(*backRef)=f_end->next;
		f_end->next=NULL;
	}
	else if (length(source)%2==1){
		struct node* f_end=source;
		int truncated_length=(length(source)+1)/2,i;
		for (i=1;i<truncated_length;i++){
			f_end=f_end->next;
		}
		(*frontRef)=source;
		(*backRef)=f_end->next;
		f_end->next=NULL;
	}
}


void removeduplicates(struct node* head){//bunu yazmasi biraz ugrastirdi.muhtemelen daha guzel ve sade yazabilirim.
	struct node* traveler1=head,*traveler2=head,*to_del;
	
	while(traveler1->next!=NULL){
		while(traveler2->next->next!=NULL){
			if (traveler1->data==traveler2->next->data){	
				to_del=traveler2->next;
				traveler2->next=traveler2->next->next;
				free(to_del);		
			}
			else{
				traveler2=traveler2->next;
			}
		}
	traveler1=traveler1->next;
	traveler2=traveler1;
	}
	
	traveler2=head;
	traveler1=head;
	while(traveler1->next->next!=NULL){
		traveler1=traveler1->next;
	}
	
	while(traveler2->next!=NULL){//yukarda son dugum kontrol edilemedigi icin burada ediliyor.
		if(traveler2->data==traveler1->next->data){
			to_del=traveler1->next;
			traveler1->next=NULL;
			free(to_del);
			break;
		}
		traveler2=traveler2->next;
	}
}


void movenode(struct node** destRef,struct node** sourceRef){//kaynak liste bos olmamali.
	struct node* to_move=(*sourceRef);
	(*sourceRef)=(*sourceRef)->next;
	to_move->next=(*destRef);
	(*destRef)=to_move;
}

void alternatingsplit(struct node* source,struct node** aRef,struct node** bRef){
	movenode(aRef,&source);
	movenode(bRef,&source);
	struct node* traveler=source;
	int odd_even=0;
	while(traveler!=NULL){
		if (odd_even%2==0){
			add((*aRef),traveler->data);
		}
		else{
			add((*bRef),traveler->data);
		}
		++odd_even;
		traveler=traveler->next;
	}
	
}


struct node* shufflemerge(struct node* a,struct node* b){//listeler ayni uzunlukta olmali
	int turn=1;//sirayla eklediginden turn sayisi sirayi belirliyor.
	struct node* new_head=NULL;//yeni liste icin head olusturuyoruz.
	movenode(&new_head,&a);//a listesinin headini yeni listenin headi ypaiyoruz.
	struct node* traveler_a=a,*traveler_b=b;//a ve b listesinde gezinecek pointerlari tanimliyoruz.
	while(traveler_b!=NULL){//ikinci eklenecek listenin son elemani eklenene kadar devam edecek dongu.
		if(turn%2==0){//sirayi belirleyecek kosul
			add(new_head,traveler_a->data);//yeni listenin sonuna a listesinin en basindaki dugumu atiyoruz
			traveler_a=traveler_a->next;//a listesinin bir yanina kayiyoruz.
			++turn;//sirayi 1 arttiriyoruz yani sira b listesine gecmis oluyor.
		}
		else{
			add(new_head,traveler_b->data);//yeni listenin sonuna b listesinin en basindaki dugumu atiyoruz
			traveler_b=traveler_b->next;//b listesinin bir yanina kayiyoruz.
			++turn;
		}
	}
	return new_head;
}


struct node* sortedmerge(struct node* a,struct node* b){
	struct node* new_head=NULL;//yeni liste icin head olusturuyoruz.
	movenode(&new_head,&a);//a listesinin headini yeni listenin headi yapiyoruz.
	append(&new_head,&a);//yeni listeye a listesini ekliyoruz.
	append(&new_head,&b);//yeni listeye b listesini ekliyoruz.
	removeduplicates(new_head);//tekrar eden verileri siliyoruz.
	InsertSort(&new_head);//yeni listeyi kucukten buyuge siraliyoruz.
	return new_head;//yeni listeyi cagiriciya aktariyoruz.
}


struct node* sortedintersect(struct node* a,struct node* b){//a ve b listesinden yeni siralanmis bir liste olusturuyor.a ve b degismiyor.
	struct node* new_head=NULL,*tmp_a,*tmp_b;
	tmp_a=copy_list(a);
	tmp_b=copy_list(b);
	InsertSort(&tmp_a);
	InsertSort(&tmp_b);
	new_head=sortedmerge(tmp_a,tmp_b);
	return new_head;
}

void reverse(struct node** head){
	struct node* 	traveler=(*head),*next_node=NULL,*prev_node=NULL;
	while(traveler!=NULL){
		next_node=traveler->next;
		traveler->next=prev_node;
		prev_node=traveler;
		traveler=next_node;
	}
	(*head)=prev_node;
}

void print_nodes(struct node* head){
	struct node* traveler=head;
	while(traveler!=NULL){
		printf("%d\n",traveler->data);
		traveler=traveler->next;
	}
	printf("END");
}


main(){
	struct node* head=NULL;
	struct node* head2=NULL,*head3=NULL,*head4=NULL;
	push(&head,2);
	push(&head,4);
	push(&head,6);
	push(&head2,1);
	push(&head2,3);
	push(&head2,5);												//push			 	tamam
	//insertNth(&head,0,5);										//insertNth      	tamam
	//delete_list(&head);										//delete_list    	tamam
	//printf("%d",length(head));								//length  	   	 	tamam
	//printf("%d",getNth(head,1));								//getNth 	  	 	tamam
	//print_nodes(head);										//print_nodes	 	tamam
	//printf("%d",pop(&head));									//pop 		  	 	tamam

	//struct node* new_node=malloc(sizeof(struct node));
	//new_node->data=1;
	//SortedInsert(&head,new_node);								//SortedInsert	 	tamam
	//InsertSort(&head);										//InsertSort  	 	tamam
	//append(&head,&head2);										//append      	 	tamam
	//frontbacksplit(head,&head3,&head4);						//frontbacksplit    tamam
	//removeduplicates(head);									//removeduplicates  tamam
	//movenode(&head,&head2);									//movenode 			tamam
	//alternatingsplit(head,&head3,&head4);						//alternatingsplit  tamam
	//head3=shufflemerge(head,head2);							//shufflemerge		tamam
	//head3=sortedmerge(head,head2);							//sortedmerge 		tamam
	//head3=sortedintersect(head,head2);						//sortedintersect   tamam
    //reverse(&head);											//reverse 			tamam
	
}
