int main() {
    
    int i = 0;
    int b = 0;
    for (; i < 10; i++) {
        int a = i ^ 2;
        b += a;
    }
    return b;
}
