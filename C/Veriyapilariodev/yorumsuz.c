#include <stdio.h>
#include <stdlib.h>
#include <time.h>
struct pnode{
	struct pnode* prev;
	int data;
	struct pnode* next;	
};


void push(struct pnode** ptrptr, int Data){
	struct pnode* new_node = malloc(sizeof(struct pnode));
	
	if((*ptrptr) == NULL){
		new_node->prev = NULL;
		new_node->data = Data;
		new_node->next = NULL;
		(*ptrptr) = new_node;
	}
									
	else{													
		new_node->prev = (*ptrptr)->prev;
		(*ptrptr)->prev = new_node;
		new_node->next = (*ptrptr);
		new_node->data = Data;
		(*ptrptr) = new_node;
	}
}


struct pnode* random_list(int length,int min,int max){
	struct pnode* new_head = NULL;
	int numbers[length], i;
	random_generator(numbers, min, max, length);
	for(i = 0 ; i<length ; i++)
		push(&new_head, numbers[i]);
	return new_head;
}


void print_nodes(struct pnode* head){
	struct pnode* traveler = head;
	int index = 0;
	
	while(traveler != NULL){
		printf("%3d.index:\t%d\n", index, traveler->data);
		traveler = traveler->next;
		++index;
	}
}


void random_generator(int* ptr, int min, int max, int count){
	int i;
	srand(time(0));
	
	for(i=0 ; i<count ; i++){
		ptr[i] = (rand() % (max - min + 1));
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


char add_next_to(struct pnode* head){
	int data, next_to, nTh_next_to;
	
	printf("\nEklemek istediginiz sayi:\t");
	scanf("%d", &data);
	printf("Hangi sayidan sonra eklenecek:\t");
	scanf("%d", &next_to);
	printf("Kacinci %d ' dan sonra eklenecek(ilk index=0):\t",next_to);
	scanf("%d", &nTh_next_to);
	printf("\n\n----Listenin son hali----\n\n");
	
	struct pnode* traveler = head;
	int count_indexof_next_to = 0;
	
	while(traveler != NULL){
		if (traveler->data == next_to){
			if (count_indexof_next_to == nTh_next_to){
				break;
			}
			++count_indexof_next_to;
		}
		traveler = traveler->next;
	}
	push(&(traveler->next), data);
	print_nodes(head);
	
	char event;
	printf("Devam etmek istiyor musunuz?(e/h)\t");							
	
	if(getch() == 'e'){
		printf("e");
		return 'e';
	}
	
	else{
		printf("h\nKapatmak icin herhangi bir tusa basin");
		return 'h';
	}
}																		  


int main(){
	struct pnode* head=NULL;
	int length,min,max;
	char event = 'e';
	
	printf("Rastgele sayilari icerecek bagli listenin uzunlugu:\t");
	scanf("%d",&length);
	printf("\nRastgele sayilarin alabilecegi en kucuk deger:\t");
	scanf("%d",&min);
	printf("\nRastgele sayilarin alabilecegi en buyur deger:\t");
	scanf("%d",&max);
	
	head=random_list(length,min,max);
	print_nodes(head);
	
	while(add_next_to(head) == 'e'){}
	getch();
	return 1;
}
