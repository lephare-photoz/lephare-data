c       gfortran  -O5 -Wall -ffixed-line-length-132 bin_ised.f public_utilities.a -o bin_ised
c 
	PROGRAM BIN_ISED

c	Converts *.ised file from ASCII to BINARY format

c	Array declarations
	logical stelib
	character id*80,id2*80,id3*80,name*256

c	Maximum number of wavelength points
	PARAMETER (imw=12000)
	real w(imw),h(imw),tb(0:500),f(100)

c	Array declaration for IMF data
	parameter (imf=10)
	real xx(imf),lm(imf),um(imf),baux(imf),cc(imf),cn(imf),taupar(4)

c       Ask for file name if not enterd in command line
	j=iargc()
	if (j.eq.0) then
c		call copyright(6)
		write (6,'(x,a,$)') 'BC model *.ised in ASCII file = '
		read (5,'(a)',end=10) name
	else
		call getarg(1,name)
	endif

c	Read basic parameters from input file
	open  (2,file=name,form='formatted',status='old',err=3)
	read (2,*) nsteps,(tb(i),i=1,nsteps)
	read (2,*) ml,mu,iseg,(xx(i),lm(i),um(i),baux(i),
     &            cn(i),cc(i),i=1,iseg)
     	read (2,*) totm,totn,avs,jo,tau,tau1,tau2,tau3,tau4,iop,stelib
	read (2,'(a)') id
	read (2,'(a)') id2
	read (2,'(a)') id3
	write (6,*) nsteps,' time steps'

c	Write basic parameters to output file
	name=name(1:largo(name)-10) // 'ised'
	open (1,file=name,form='unformatted',status='unknown')
	write (1)       nsteps,(tb(i),i=1,nsteps),
     &	     ml,mu,iseg,(xx(i),lm(i),um(i),baux(i),cn(i),cc(i),i=1,iseg),
     &	  totm,totn,avs,jo,tau,id,tau1,tau2,tau3,tau4,id2,id3,iop,stelib

c	Read wavelength scale from input file and write to binary file
	read (2,*) inw,(w(i),i=1,inw)
	write (6,*) inw,' wavelength points per record'
	write (1)  inw,(w(i),i=1,inw)

c	Read sed's from ASCII file and write to binary file
	do n=1,nsteps
	read  (2,*) ik,(h(i),i=1,ik),ix,(f(i),i=1,ix)
	write (1)   ik,(h(i),i=1,ik),ix,(f(i),i=1,ix)
	enddo
c	Add 12 records after the sed's.
	do n=1,+10
	read  (2,*) ik,(h(i),i=1,ik)
	write (1)   ik,(h(i),i=1,ik)
	enddo
	write (6,*) ix,' fitting function fluxes per record'

c	Close files
	close (1)
	close (2)
	stop
c	goto 1
3       write (6,'(3a)') 'File ',name(1:largo(name)),' not found'
c	goto 1
10	end


	FUNCTION LARGO(A)
c	Returns significant length of string a
	character*(*) a
	largo=0
	do i=1,len(a)
	if (a(i:i).ne.' ') largo=i
	enddo
	return
	end
	FUNCTION MARGO(A)
c	Returns max(1,largo(a)) to avoid error in DEC fortran
	character*(*) a
	margo=max(1,largo(a))
	return
	end
	FUNCTION NARGO(A)
c	Returns position where first dot occurs
	character*(*) a
	nargo=largo(a)
	do i=1,nargo
	if (a(i:i).eq.'.') then
		nargo=i-1
		return
	endif
	enddo
	return
	end
