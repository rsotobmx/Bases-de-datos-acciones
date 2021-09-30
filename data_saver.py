import pandas as pd
import os 
import numpy as np
from data_dowloader import data_dowload

#herenciaa
class data_saved(data_dowload):
    pass
    
    
    def Save_data(self):
        
        df = pd.DataFrame(self.get_data())
        
        nombre = self.symbol + '_' + self.interval + '.csv'
        
        
        
        if  nombre in os.listdir() and not df.empty :
            
            
            df2 = pd.read_csv(nombre)
            fecha_max= np.max(df2['date'])
            
            #Si la Data que viene no es nueva no la Agrega
            
            df2 = pd.concat( [df[df.index > fecha_max ] ,df2])
            df2.to_csv(nombre, header=True, index=False)
                
            
            
        elif not df.empty : 
            
            df.reset_index().to_csv(nombre, header=True, index=False)
            
