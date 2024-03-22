pro  convert_ascii

  restore,'sed_z1_U1.save'
  plot ,LAMBDA,MOD_TOT_Z1, color = 255,xrange=[0.5,200]
  openw,1,'sed_z1_U1.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z1[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1

  restore,'sed_z2_U2.save'
  plot ,LAMBDA,MOD_TOT_Z2, color = 255,xrange=[0.5,200]
  openw,1,'sed_z2_U2.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z2[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1


  restore,'sed_z3_U3.save'
  plot ,LAMBDA,MOD_TOT_Z3, color = 255,xrange=[0.5,200]
  openw,1,'sed_z3_U3.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z3[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1


  restore,'sed_z4_U4.save'
  plot ,LAMBDA,MOD_TOT_Z4, color = 255,xrange=[0.5,200]
  openw,1,'sed_z4_U4.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z4[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1


  restore,'sed_z5_U5.save'
  plot ,LAMBDA,MOD_TOT_Z5, color = 255,xrange=[0.5,200]
  openw,1,'sed_z5_U5.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z5[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1

  restore,'sed_z6_U6.save'
  plot ,LAMBDA,MOD_TOT_Z6, color = 255,xrange=[0.5,200]
  openw,1,'sed_z6_U6.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z6[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1

  restore,'sed_z7_U7.save'
  plot ,LAMBDA,MOD_TOT_Z7, color = 255,xrange=[0.5,200]
  openw,1,'sed_z7_U7.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z7[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1


  restore,'sed_z8_U8.save'
  plot ,LAMBDA,MOD_TOT_Z8, color = 255,xrange=[0.5,200]
  openw,1,'sed_z8_U8.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z8[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1


  restore,'sed_z9_U9.save'
  plot ,LAMBDA,MOD_TOT_Z9, color = 255,xrange=[0.5,200]
  openw,1,'sed_z9_U9.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_Z9[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1

  restore,'sb_U.save'
  plot ,LAMBDA,MOD_TOT_SB, color = 255,xrange=[0.5,200]
  openw,1,'sb_U.dat'
  for k=0,(size(lambda))[1]-1 do begin
    printf,1,LAMBDA[k]*10000,MOD_TOT_SB[k],format='(F15.5 ,1x, F15.5)' 
   endfor
  close,1

end
