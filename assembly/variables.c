
int main() {
    int e = 55;
    int d = 44;     
    int c = 33;
    int b = 22;
    int a = 11;
    int g;
/*
//g = (a-234)+(b-4332)+(c-12)+(d-12344)+(e-444)+(f-234);
mov rax, [a]
add rax, 234
mov rbx, rax

mov rax, [b]
sub rax, 4332

add rbx, rax

mov rax, [c]
sub rax, 12

add rbx, rax

*/

//g = (29 * a) * (29 * b);

g = (29 / a) * ((29 / b) * ((29 / c) * ((29 / d) * (29 / e))));
//g = (29 / d) * ((a*b) + c*(29-b));
/*
mov rax, 25
sub rax, [b]
mov rbx, rax

mov rax, [a]
imul [b]
add rbx, rax
*/


    //g  = a + 34*(b + 33*(c + 32*(d + 31)* (12+a))* (15+b)) * (c+23);

    //(34*a) * (35*b) * (36*c) * (
    
    return g;
}

















