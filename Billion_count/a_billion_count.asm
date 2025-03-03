section .data
	fmt db "Count from 0 to 1.000.000.000 completed!", 0xA, 0

section .text
	global main
	extern printf

main:
	mov ecx, 0

.loop:
	cmp ecx, 1000000000
	jge .done
	
	inc ecx
	jmp .loop

.done:
	push dword fmt
	call printf
	add esp, 4

	mov eax, 0
	ret
