def Ec_Parametrica(p,v,t=1,ver=0):
	'''Retornaecuacionparametricadadopuntoyvector.
	x=x0−t.vx
	y=y0−t.vy
	Parametros:
	p−−−puntoPdelarecta
	v−−−vector
	t−−−parametropordefecto1
	ver−−−verecuacion0:no,1si
	'''
	if ver==0:
		x=p[0]+(t∗v[0])
		y=p[1]+(t∗v[1])
		return[x,y]
	else:
		s_x=''x=''+str(p[0])+''+(''+str(v[0])+'')t''
		s_y=''y=''+str(p[1])+''+(''+str(v[1])+'')t''
		com=''parat=''+str(t)
	return[s_x,s_y,com]
	