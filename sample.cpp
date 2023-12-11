#include<stdio.h>

//set 

class SampleClass {
   public:
     int x = 0;
     
     SampleClass() {
        // constructor
     }

     void getAllData() {
       return x++;
     }
};
/* 
 * compiles to
 * struct SampleClass {
 *    int x = 0;    
 * }
 *
 * void SampleClassCons(SampleClass* this) {}
 * void SampleClassgetAllData(SampleClass* this) {
 *   return x++;
 * }
 * 
 * */
