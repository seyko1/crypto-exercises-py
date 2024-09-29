main:
  add r30 r30 #-1
  mov !r30 r31
  
  mov r2 #1312 
  mov @1312 #72 
  mov @1313 #101 
  mov @1314 #108 
  mov @1315 #108
  mov @1316 #111
  mov @1317 #32 
  mov @1318 #119 
  mov @1319 #111 
  mov @1320 #114 
  mov @1321 #108 
  mov @1322 #100 
  mov @1323 #33 
  mov @1324 #0 

  mov r2 #1312
  cal print

  mov r31 !r30
  add r30 r30 #1
  ret

print:
  mov r8 #0

print_loop:
  beq end_print !r2,r8 #0
  prc !r2,r8
  add r8 r8 #1
  jmp print_loop

end_print:
  prc #10
  ret