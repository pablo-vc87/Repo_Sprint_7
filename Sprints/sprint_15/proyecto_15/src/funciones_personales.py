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