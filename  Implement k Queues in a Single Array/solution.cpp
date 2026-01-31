class kQueues {
    
        int current = 0; // store current free index where element can be store
        vector<int>ans;
        vector<int>rear;
        vector<int>front;
        vector<int>next; // store next free index of current in ans vector and 
                         // also store next front index after pop from queue.
  
  public:
    kQueues(int n, int k) {
        // Initialize your data members
        
        ans.resize(n);
        rear.resize(n);
        front.resize(n);
        next.resize(n);
        
        for(int i=0;i<n;i++){
            ans[i] = 0;
            rear[i] = -1;
            front[i] = -1;
            next[i]=i+1;
        }
        next[n-1] = -1;
        
    }

    void enqueue(int x, int i) {
        // enqueue element x into queue i
        if(current==-1)return;
        if(rear[i]==-1){
            
            rear[i] = current;
            front[i] = current;
            int temp = current;
            
            current = next[current];
            ans[temp] = x;
            return;
        }
        
        int temp = current;
        current = next[current];
        ans[temp] = x;
        
        next[rear[i]] = temp; // current rear index should store before rear moves so that front get know where it will move
        rear[i] = temp;
        return;
        
    }

    int dequeue(int i) {
        // dequeue element from queue i
        if(rear[i]==-1)return -1;
        
        if(rear[i]==front[i]){
            int value = ans[front[i]];
            
            int temp = current;
            current = front[i];
            next[current] = temp;
            
            front[i]=rear[i] = -1;
            return value;
        }
        
         int value = ans[front[i]];
         int temp1 = front[i];
         front[i] = next[front[i]];
         
         int temp2 = current;
         current = temp1;
         next[current] = temp2;
         
         return value;
        
        
    }

    bool isEmpty(int i) {
        // check if queue i is empty
        if(rear[i]==-1)return 1;
        return 0;
    }

    bool isFull() {
        // check if array is full
        if(current == -1)return 1;
        return 0;
    }
};