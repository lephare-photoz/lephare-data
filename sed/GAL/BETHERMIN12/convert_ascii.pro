pro  convert_ascii

  restore,'SED_z.save'
    
  ;Liste de templates de Matthieu
  openw,2,'BETHERMIN_MOD.list'
  
  ;Boucle sur chaque redshift
  for i=0,209 do begin
  
    ;Genere un fichier avec le redshift *100 dans le nom
    redname=nint(Z_GRIDS[i]*100)
    name = 'sed_z' + strn(redname) +  '_MS.dat'
    openw,1,name
  
    ;Recupere le lambda et le flux, ramene en rest-frame
    dist_lum=lumdist(Z_GRIDS[i],h0=71,Omega_m=0.2660, Lambda0 =0.7334,/silent)
    ;lambda in rest-frame and angstrom
    lamb=LAMBDA_GRIDS/(1+Z_GRIDS[i])*10000
    ;surface of the sphere at z and 10 pc
    spherez =4.*3.1415926*(dist_lum*dist_lum*1.e12)*3.0857^2.*1.e36     ;surface sphere a z en cm2 ;  3.0857^2.*1.e36 to go from pc2 to cm2 
    sphere10=4.*3.1415926*100.*3.0857^2.  ;surface sphere a 10 pc en cm2. Enleve le 1.e36 pour des raisons numeriques. Je le remet apres.
    ; Flux de Jansky en erg/s/cm2/Hz
    flux=SNU_GRIDS_MS[*,i]*1.e-23
    ; FLux en erg/s/cm2/Hz a 10pc
    flux=flux*spherez/sphere10
    ; En erg/s/cm2/A a 10pc
    ;remet ic le 10^-36 manquant
    flux=flux*300000000.*1.e10/lamb^2/(1+Z_GRIDS[i])*1.e-36
 
    plot ,lamb,flux, color = 255,xrange=[0.5,2000000]   ;,yrange=[1.e-30,1.e-16]  
    ;Le stocke dans un fichier
    for k=0,(size(lamb))[1]-1 do begin
     printf,1,lamb[k],flux[k]
    endfor
    wait,0.2

    ;Check normalisation
    oo=where(lamb gt 80000. and lamb lt 10000000.)
    lamb2 = lamb[oo] 
    flux2 = flux[oo]
    result=int_tabulated(lamb2,flux2)
    print,"Norma en Lsol du Flambda ",result/(3.826*1.e33)*sphere10*1.e36
  
    ;List of models
    full_name='BETHERMIN12/'+name+'   LW   '+ strn(Z_GRIDS[i])
    if(Z_GRIDS[i] le 6)then begin
      printf,2,full_name
    endif

    close,1  

  endfor
  
  
  close,2


  ;Template de bethermin en rest-frame (a mon avis, Magdis) Lnu en Lsol
  ;restore,'SEDs_evolving_ms_v2.save'
  ;
  ;;;Boucle sur chaque U
  ;for i=0,8 do begin
  ;
  ; oo=where(LAMBDA gt 8. and LAMBDA lt 1000.)
  ; lambda2= LAMBDA[oo]
  ; flux2=SED_ARR[i,oo]*3.839*1.e33
  ;
  ; result=int_tabulated(lambda2,flux2/lambda2) /(3.839*1.e33)           ;integrale ramenee en Lsol
  ;
  ; print,"RESULT ",result
  ;endfor 


end
