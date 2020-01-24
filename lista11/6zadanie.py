class CiagArytmetyczny:

    def __init__( self, a1, r, n ):
        self.a1 = a1
        self.r = r
        self.n = n
        self.ciag = [ a1 + r * i for i in range( n+1 ) ]
        self.iterator = 0
    
    def __iter__( self ):
        self.iterator = 0
        return iter( self.ciag )
    
    def __next__( self ):
        self.iterator += 1
        return self.ciag[ self.iterator - 1 ]
    
    def __len__( self ):
        return len( self.ciag )
    
    def SaveToFile( self, nazwa ):
        with open( nazwa + ".txt", "w" ) as f:
            for An in self:
                f.write( str( An ) + "\n" )


a = CiagArytmetyczny( 2, 1, 5)
iter(a)
print( "a1:", next(a) )
print( "a2:", next(a) )
print( "a3:", next(a) )
print( "a4:", next(a) )
print( "a5:", next(a) )
print( "a6:", next(a) )
print( "len( a ):", len( a ) )
a.SaveToFile( "ciag" )
