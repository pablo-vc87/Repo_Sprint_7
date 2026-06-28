import pandas as pd

def mostrar_nan(df, columna=None, mostrar=False, num_filas=10):
    """
    Imprime la cantidad de valores Nan por columna del DataFrame
    Muestra las filas completas que contienen valores NaN
    
    Parámetros:
    df: DataFrame a analizar
    columna: nombre de columna específica (opcional)
    num_filas: cuántas filas mostrar (por defecto 10)
    """
    name = str(df)
    lista= df.columns

    #Para una sola columna:
    if columna:  
        filas_nan = df[df[columna].isna()] #crea DF de puros valores NaN
        if mostrar:
            print(f"\nFilas con NaN en '{columna}': {len(filas_nan)} encontradas") # imprime nombre de la columna y cantidad de NaN
        if not filas_nan.empty: # Si el DF filas_nan tiene algo adentro
            if mostrar:
                print("\nPrimeras", min(num_filas, len(filas_nan)), "filas completas conteniendo NaN para: ", "'",columna,"'")
                print(filas_nan.head(num_filas))
                print('-'*50) #separador visual
    else:
        filas_nan =df[df.isna().any(axis=1)]
        if mostrar:
            # 1. Mostrar total de filas con NaN
            print(f"\nTotal de filas con NaN: {len(filas_nan)}")
    
            # 2. Mostrar NaN por cada columna del DataFrame ORIGINAL
            print(f"\nCantidad de NaN por columna:")
            for column in df.columns:  # df.columns, no filas_nan.columns
                nan_count = df[column].isna().sum()  # Contar NaN en cada columna
                print(f"  {column}: {nan_count}")
    
            # 3. Mostrar las primeras filas con NaN
            if not filas_nan.empty:
                print(f"\nPrimeras {min(num_filas, len(filas_nan))} filas con NaN:")
                print(filas_nan.head(num_filas))
                print('-'*50)
    return filas_nan

#=============================================
def mostrar_dupli(df, columna=None, num_filas=10):
    """
    Imprime la cantidad de filas duplicadas del DataFrame
    Muestra las filas completas que están duplicadas
    
    Parámetros:
    df: DataFrame a analizar
    columna: nombre de columna específica para buscar duplicados (opcional)
    num_filas: cuántas filas mostrar (por defecto 10)
    """
    
    print(f"\nEl dataframe tiene {df.duplicated().sum()} filas completamente duplicadas")
    print('-'*50)
    # Para una sola columna:
    if columna:  
        filas_duplicadas = df[df.duplicated(subset=[columna], keep=False)]
        print(f"\nFilas con valores duplicados en '{columna}': {len(filas_duplicadas)} encontradas")
        print('-'*50)
        if not filas_duplicadas.empty:
            print(f"\nPrimeras {min(num_filas, len(filas_duplicadas))} filas completas con duplicados en: '{columna}'")
            print(filas_duplicadas.head(num_filas))
            print('-'*50)
    else:        
        # Para duplicados completos (todas las columnas)
        filas_duplicadas = df[df.duplicated(keep=False)]
        print(f"\nFilas completamente duplicadas: {len(filas_duplicadas)} encontradas")
        print('-'*50)
        if not filas_duplicadas.empty:
            print(f"\nPrimeras {min(num_filas, len(filas_duplicadas))} filas completamente duplicadas:")
            print(filas_duplicadas.sort_values('user_id').head(num_filas))
            print('-'*50)
    return filas_duplicadas
#======================================
def afina_datos(df):
    """
    Recibe un dataframe:
    Cambia el formato de la columna 'date'a datetime
    y trunca el formato hasta horas.
    Rellena valores ausentes con el inmediato anterior 
    para cada columna del dataframe.
    Devuelve el dataframe con formatos en fecha 
    sin valores ausentes
    """
    df['date'] = pd.to_datetime(df['date']).dt.floor('H')
    df.ffill(inplace=True)
    return df