# -*- coding: utf-8 -*-

import ply.lex as lex

## 모든 토큰 정리 
tokens = (    
    
    ## type 
    'BIGINT'            ,               
    'INT'               ,

    # BATCH
    'GO'                ,

    ## 객체 이름 등 
    'LITERAL_STR'       ,   ## 
    
    'LPAREN'            ,   ## (
    'RPAREN'            ,   ## )            
    'SINGLE_QUETO'      ,   ## '         
    'COMMA'
    
    ## 예약어 
    'ID'                ,   ##       
    'ADD'               ,                  
    'EXTERNAL'          ,             
    'PROCEDURE'         ,            
    'ALL'               , 
    'FETCH'             ,                
    'PUBLIC'            ,               
    'ALTER'             ,                
    'FILE'              ,
    'RAISERROR'         ,            
    'AND'               ,                  
    'FILLFACTOR'        ,           
    'READ'              ,
    'ANY'               ,                  
    'FOR'               ,                  
    'READTEXT'          ,             
    'AS'                ,
    'FOREIGN'           ,              
    'RECONFIGURE'       ,          
    'ASC'               ,                  
    'FREETEXT'          ,
    'REFERENCES'        ,           
    'AUTHORIZATION'     ,        
    'FREETEXTTABLE'     ,        
    'BACKUP'            ,
    'FROM'              ,                 
    'RESTORE'           ,              
    'BEGIN'             ,                
    'FULL'              ,
    'RESTRICT'          ,             
    'BETWEEN'           ,              
    'FUNCTION'          ,             
    'RETURN'            ,
    'BREAK'             ,                
    'GOTO'              ,                 
    'REVERT'            ,               
    'BROWSE'            ,
    'GRANT'             ,                
    'REVOKE'            ,               
    'BULK'              ,                 
    'GROUP'             ,
    'RIGHT'             ,                
    'BY'                ,                   
    'HAVING'            ,               
    'ROLLBACK'          ,
    'CASCADE'           ,              
    'HOLDLOCK'          ,             
    'ROWCOUNT'          ,             
    'CASE'              ,
    'IDENTITY'          ,             
    'ROWGUIDCOL'        ,           
    'CHECK'             ,                    
    'IDENTITY_INSERT'   ,
    'RULE'              ,                 
    'CHECKPOINT'        ,           
    'IDENTITYCOL'       ,          
    'SAVE'              ,
    'CLOSE'             ,                
    'IF'                ,                   
    'SCHEMA'            ,               
    'CLUSTERED'         ,
    'IN'                ,                   
    'SECURITYAUDIT'     ,        
    'COALESCE'          ,             
    'INDEX'             ,
    'SELECT'            ,               
    'COLLATE'           ,              
    'INNER'             ,                
    'COLUMN'            ,
    'INSERT'            ,               
    'COMMIT'            ,               
    'INTERSECT'         ,            
    'COMPUTE'           ,
    'INTO'              ,                 
    'SESSION_USER'      ,         
    'CONSTRAINT'        ,           
    'IS'                ,
    'SET'               ,                  
    'CONTAINS'          ,             
    'JOIN'              ,                 
    'SETUSER'           ,
    'CONTAINSTABLE'     ,        
    'KEY'               ,                  
    'SHUTDOWN'          ,             
    'CONTINUE'          ,
    'KILL'              ,                           
    'SOME'              ,                 
    'CONVERT'           ,              
    'LEFT'              ,
    'STATISTICS'        ,           
    'CREATE'            ,               
    'LIKE'              ,                 
    'SYSTEM_USER'       ,  
    'CROSS'             ,                
    'LINENO'            ,               
    'TABLE'             ,                
    'CURRENT'           ,
    'LOAD'              ,                 
    'TABLESAMPLE'       ,          
    'CURRENT_DATE'      ,         
    'MERGE'             ,
    'TEXTSIZE'          ,             
    'CURRENT_TIME'      ,          
    'NATIONAL'          ,             
    'THEN'              ,
    'CURRENT_TIMESTAMP' ,    
    'NOCHECK'           ,              
    'TO'                ,                   
    'CURRENT_USER'      ,
    'NONCLUSTERED'      ,         
    'CURSOR'            ,               
    'NOT'               ,                  
    'TRAN'              ,
    'DATABASE'          ,             
    'NULL'              ,                 
    'TRANSACTION'       ,          
    'DBCC'              ,
    'NULLIF'            ,               
    'TRIGGER'           ,              
    'DEALLOCATE'        ,           
    'OF'                ,
    'TRUNCATE'          ,             
    'DECLARE'           ,                
    'OFF'               ,                  
    'TRY_CONVERT'       ,
    'DEFAULT'           ,              
    'OFFSETS'           ,              
    'TSEQUAL'           ,              
    'DELETE'            ,
    'ON'                ,                   
    'UNION'             ,                
    'DENY'              ,                 
    'OPEN'              ,
    'UNIQUE'            ,               
    'DESC'              ,                 
    'OPENDATASOURCE'    ,       
    'UNPIVOT'           ,
    'DISK'              ,                 
    'OPENQUERY'         ,            
    'UPDATE'            ,               
    'DISTINCT'          ,
    'OPENROWSET'        ,           
    'UPDATETEXT'        ,           
    'DISTRIBUTED'       ,          
    'OPENXML'           ,
    'USE'               ,                  
    'DOUBLE'            ,               
    'OPTION'            ,                  
    'USER'              ,
    'DROP'              ,                 
    'OR'                ,                   
    'VALUES'            ,               
    'DUMP'              ,
    'ORDER'             ,                
    'VARYING'           ,                
    'ELSE'              ,                 
    'OUTER'             ,
    'VIEW'              ,                 
    'END'               ,                  
    'OVER'              ,                 
    'WAITFOR'           ,
    'ERRLVL'            ,               
    'PERCENT'           ,              
    'WHEN'              ,                 
    'ESCAPE'            ,
    'PIVOT'             ,                
    'WHERE'             ,                
    'EXCEPT'            ,               
    'PLAN'              ,
    'WHILE'             ,                
    'EXEC'              ,                 
    'PRECISION'         ,            
    'PRIMARY'           ,              
    'WITHIN'            ,               
    'EXISTS'            ,               
    'PRINT'             ,                
    'WRITETEXT'         ,            
    'EXIT'              ,                 
    'PROC'              ,     
)

reserved_words = {
    'ADD'	           : 'ADD'	            ,
    'EXTERNAL'	       : 'EXTERNAL'	        ,
    'PROCEDURE'        : 'PROCEDURE'        ,   
    'FETCH'	           : 'FETCH'	        ,    
    'PUBLIC'           : 'PUBLIC'           ,   
    'ALTER'	           : 'ALTER'	        ,    
    'FILE'	           : 'FILE'	            ,
    'RAISERROR'        : 'RAISERROR'        ,   
    'AND'	           : 'AND'	            ,    
    'FILLFACTOR'       : 'FILLFACTOR'       ,   
    'READ'             : 'READ'             ,   
    'ANY'	           : 'ANY'	            ,    
    'FOR'	           : 'FOR'	            ,    
    'READTEXT'         : 'READTEXT'         ,   
    'AS'               : 'AS'               ,   
    'FOREIGN'          : 'FOREIGN'	        ,    
    'RECONFIGURE'      : 'RECONFIGURE'      ,   
    'ASC'	           : 'ASC'	            ,    
    'FREETEXT'	       : 'FREETEXT'	        ,
    'REFERENCES'       : 'REFERENCES'       ,   
    'AUTHORIZATION'	   : 'AUTHORIZATION'	,    
    'FREETEXTTABLE'	   : 'FREETEXTTABLE'	,    
    'BACKUP'           : 'BACKUP'           ,   
    'FROM'	           : 'FROM'	            ,
    'RESTORE'          : 'RESTORE'          ,   
    'BEGIN'	           : 'BEGIN'	        ,    
    'FULL'	           : 'FULL'	            ,
    'RESTRICT'         : 'RESTRICT'         ,   
    'BETWEEN'	       : 'BETWEEN'	        ,    
    'FUNCTION'	       : 'FUNCTION'	        ,
    'RETURN'           : 'RETURN'           ,   
    'BREAK'            : 'BREAK'            ,   
    'GOTO'	           : 'GOTO'	            ,
    'REVERT'           : 'REVERT'           ,   
    'BROWSE'           : 'BROWSE'           ,   	
    'GRANT'	           : 'GRANT'	        ,    
    'REVOKE'           : 'REVOKE'           ,   
    'BULK'	           : 'BULK'	            ,
    'GROUP'	           : 'GROUP'	        ,    
    'RIGHT'            : 'RIGHT'            ,   
    'BY'               : 'BY'               ,       
    'HAVING'	       : 'HAVING'	        ,    
    'ROLLBACK'         : 'ROLLBACK'         ,   
    'CASCADE'	       : 'CASCADE'	        ,    
    'HOLDLOCK'	       : 'HOLDLOCK'	        ,
    'ROWCOUNT'         : 'ROWCOUNT'         ,   
    'CASE'             : 'CASE'             ,   
    'IDENTITY'	       : 'IDENTITY'	        ,
    'ROWGUIDCOL'       : 'ROWGUIDCOL'       ,   
    'CHECK'	           : 'CHECK'	        ,    
    'IDENTITY_INSERT'  : 'IDENTITY_INSERT'	,    
    'RULE'             : 'RULE'             ,   
    'CHECKPOINT'	   : 'CHECKPOINT'	    ,    
    'IDENTITYCOL'	   : 'IDENTITYCOL'	    ,    
    'SAVE'             : 'SAVE'             ,   
    'CLOSE'	           : 'CLOSE'	        ,    
    'IF'               : 'IF'               ,   
    'SCHEMA'           : 'SCHEMA'           ,   
    'CLUSTERED'	       : 'CLUSTERED'	    ,    
    'IN'	           : 'IN'	            ,    
    'SECURITYAUDIT'    : 'SECURITYAUDIT'    ,   
    'COALESCE'	       : 'COALESCE'	        ,
    'INDEX'	           : 'INDEX'	        ,    
    'SELECT'           : 'SELECT'           ,   
    'COLLATE'	       : 'COLLATE'	        ,    
    'INNER'	           : 'INNER'	        ,    
    'COLUMN'           : 'COLUMN'           ,   
    'INSERT'	       : 'INSERT'	        ,    
    'COMMIT'	       : 'COMMIT'	        ,    
    'INTERSECT'	       : 'INTERSECT'	    ,    
    'COMPUTE'	       : 'COMPUTE'	        ,    
    'INTO'	           : 'INTO'	            ,
    'SESSION_USER'     : 'SESSION_USER'     ,   
    'CONSTRAINT'	   : 'CONSTRAINT'	    ,    
    'IS'	           : 'IS'	            ,    
    'SET'              : 'SET'              ,   
    'CONTAINS'	       : 'CONTAINS'	        ,
    'JOIN'	           : 'JOIN'	            ,
    'SETUSER'          : 'SETUSER'          ,   
    'CONTAINSTABLE'	   : 'CONTAINSTABLE'	,    
    'KEY'	           : 'KEY'	            ,    
    'SHUTDOWN'         : 'SHUTDOWN'         ,   
    'CONTINUE'	       : 'CONTINUE'	        ,
    'KILL'	           : 'KILL'	            ,
    'SOME'             : 'SOME'             ,   
    'CONVERT'	       : 'CONVERT'	        ,    
    'LEFT'	           : 'LEFT'	            ,
    'STATISTICS'       : 'STATISTICS'       ,   
    'CREATE'	       : 'CREATE'	        ,    
    'LIKE'	           : 'LIKE'	            ,
    'SYSTEM_USER'      : 'SYSTEM_USER'      ,   
    'CROSS'	           : 'CROSS'	        ,    
    'LINENO'	       : 'LINENO'	        ,    
    'TABLE'            : 'TABLE'            ,   
    'CURRENT'	       : 'CURRENT'	        ,    
    'LOAD'	           : 'LOAD'	            ,
    'TABLESAMPLE'      : 'TABLESAMPLE'      ,   
    'CURRENT_DATE'	   : 'CURRENT_DATE'	    ,
    'MERGE'	           : 'MERGE'	        ,    
    'TEXTSIZE'         : 'TEXTSIZE'         ,   
    'CURRENT_TIME'	   : 'CURRENT_TIME'	    ,
    'NATIONAL'	       : 'NATIONAL'	        ,
    'THEN'             : 'THEN'             ,   
    'CURRENT_TIMESTAMP': 'CURRENT_TIMESTAMP',   
    'NOCHECK'	       : 'NOCHECK'	        ,    
    'TO'               : 'TO'               ,   
    'CURRENT_USER'	   : 'CURRENT_USER'	    ,
    'NONCLUSTERED'     : 'NONCLUSTERED'     ,   
    'CURSOR'	       : 'CURSOR'	        ,    
    'NOT'	           : 'NOT'	            ,    
    'TRAN'             : 'TRAN'             ,   
    'DATABASE'	       : 'DATABASE'	        ,
    'NULL'	           : 'NULL'	            ,
    'TRANSACTION'      : 'TRANSACTION'      ,   
    'DBCC'	           : 'DBCC'	            ,
    'NULLIF'	       : 'NULLIF'	        ,    
    'TRIGGER'          : 'TRIGGER'          ,   
    'DEALLOCATE'	   : 'DEALLOCATE'	    ,    
    'OF'	           : 'OF'	            ,    
    'TRUNCATE'         : 'TRUNCATE'         ,   
    'DECLARE'	       : 'DECLARE'	        ,    
    'OFF'	           : 'OFF'	            ,    
    'TRY_CONVERT'      : 'TRY_CONVERT'      ,   
    'DEFAULT'	       : 'DEFAULT'	        ,    
    'OFFSETS'	       : 'OFFSETS'	        ,    
    'TSEQUAL'          : 'TSEQUAL'          ,   
    'DELETE'           : 'DELETE'           ,          
    'ON'               : 'ON'               ,   
    'UNION'            : 'UNION'            ,   
    'DENY'	           : 'DENY'	            ,
    'OPEN'	           : 'OPEN'	            ,
    'UNIQUE'           : 'UNIQUE'           ,   
    'DESC'	           : 'DESC'	            ,
    'OPENDATASOURCE'   : 'OPENDATASOURCE'   ,   
    'UNPIVOT'          : 'UNPIVOT'          ,   
    'DISK'	           : 'DISK'	            ,
    'OPENQUERY'	       : 'OPENQUERY'	    ,    
    'UPDATE'           : 'UPDATE'           ,   
    'DISTINCT'	       : 'DISTINCT'	        ,
    'OPENROWSET'	   : 'OPENROWSET'	    ,    
    'UPDATETEXT'       : 'UPDATETEXT'       ,   
    'DISTRIBUTED'	   : 'DISTRIBUTED'	    ,    
    'OPENXML'	       : 'OPENXML'	        ,    
    'USE'              : 'USE'              ,   
    'DOUBLE'           : 'DOUBLE'           ,   
    'OPTION'	       : 'OPTION'	        ,    
    'USER'             : 'USER'             ,   
    'DROP'	           : 'DROP'	            ,
    'OR'               : 'OR'               ,   
    'VALUES'           : 'VALUES'           ,   
    'DUMP'             : 'DUMP'             ,   	
    'ORDER'	           : 'ORDER'	        ,    
    'VARYING'          : 'VARYING'          ,   
    'ELSE'	           : 'ELSE'	            ,   
    'OUTER'	           : 'OUTER'	        ,    
    'VIEW'             : 'VIEW'             ,   
    'END'	           : 'END'	            ,    
    'OVER'	           : 'OVER'	            ,
    'WAITFOR'          : 'WAITFOR'          ,   
    'ERRLVL'	       : 'ERRLVL'	        ,    
    'PERCENT'          : 'PERCENT'          ,   	
    'WHEN'             : 'WHEN'             ,   
    'ESCAPE'	       : 'ESCAPE'	        ,    
    'PIVOT'            : 'PIVOT'            ,   
    'WHERE'            : 'WHERE'            ,   
    'EXCEPT'	       : 'EXCEPT'	        ,    
    'PLAN'	           : 'PLAN'	            ,
    'WHILE'            : 'WHILE'            ,   
    'EXEC'	           : 'EXEC'	            ,
    'PRECISION'        : 'PRECISION'        ,    
    'PRIMARY'	       : 'PRIMARY'	        ,    
    'WITHIN'           : 'WITHIN'           ,   
    'EXISTS'	       : 'EXISTS'	        ,    
    'PRINT'	           : 'PRINT'	        ,    
    'WRITETEXT'        : 'WRITETEXT'        ,   
    'EXIT'	           : 'EXIT'	            ,
    'PROC'             : 'PROC'             ,   
    'SEMANTICKEYPHRASETABLE': 'SEMANTICKEYPHRASETABLE'                  ,
    'SEMANTICSIMILARITYDETAILSTABLE': 'SEMANTICSIMILARITYDETAILSTABLE'  ,
    'SEMANTICSIMILARITYTABLE': 'SEMANTICSIMILARITYTABLE'
}

'''
system_function = {
    ## 1. 집계 
    'APPROX_COUNT_DISTINCT' : 'APPROX_COUNT_DISTINCT',      ## 이 함수는 그룹에 있는 고유한 null이 아닌 값의 대략적인 개수를 반환합니다.
    'AVG'                   : 'AVG'                  ,      ## 이 기능은 그룹에 속한 값의 평균을 반환합니다. Null 값을 무시합니다.
    'CHECKSUM_AGG'          : 'CHECKSUM_AGG'         ,      ## 이 함수는 그룹에 있는 값의 체크섬을 반환합니다. CHECKSUM_AGG는 Null 값을 무시합니다. OVER 절은 CHECKSUM_AGG 다음에 올 수 있습니다.
    'COUNT'                 : 'COUNT'                ,      ## 이 함수는 그룹에 있는 항목의 수를 반환합니다. COUNT은 COUNT_BIG 함수처럼 작동합니다. 이러한 함수는 해당 반환 값의 데이터 형식만이 다릅니다. COUNT은 항상 int 데이터 형식 값을 반환합니다. COUNT_BIG은 항상 bigint 데이터 형식 값을 반환합니다.
    'COUNT_BIG'             : 'COUNT_BIG'            ,      ## 이 함수는 그룹에 있는 항목의 수를 반환합니다. COUNT_BIG은 COUNT 함수처럼 작동합니다. 이러한 함수는 해당 반환 값의 데이터 형식만이 다릅니다. COUNT_BIG은 항상 bigint 데이터 형식 값을 반환합니다. COUNT은 항상 int 데이터 형식 값을 반환합니다.
    'GROUPING'              : 'GROUPING'             ,      ## GROUP BY 목록에 지정된 열 식이 집계되었는지 여부를 나타냅니다. GROUPING은 집계된 경우 결과 집합에 1을 반환하고 집계되지 않은 경우 0을 반환합니다. GROUP BY 절이 지정된 경우 GROUPING은 SELECT <select> 목록, HAVING 및 ORDER BY 절에만 사용할 수 있습니다.
    'GROUPING_ID'           : 'GROUPING_ID'          ,      ## 그룹 수준을 계산하는 함수입니다. GROUP BY 절이 지정된 경우 GROUPING_ID는 SELECT <select> 목록, HAVING 및 ORDER BY 절에만 사용할 수 있습니다.
    'MAX'                   : 'MAX'                  ,      ## 식의 최대값을 반환합니다.
    'MIN'                   : 'MIN'                  ,      ## 식의 최소값을 반환합니다. OVER 절이 뒤에 올 수도 있습니다.    
    'STDEV'                 : 'STDEV'                ,      ## 지정한 식의 모든 값에 대한 통계적 표준 편차를 반환합니다.
    'STDEVP'                : 'STDEVP'               ,      ## 지정한 식에 있는 모든 값의 모집단에 대한 통계적 표준 편차를 반환합니다.
    'SUM'                   : 'SUM'                  ,      ## 식의 모든 값 또는 DISTINCT 값의 합계를 반환합니다. SUM은 숫자 열에서만 사용할 수 있습니다. Null 값은 무시됩니다.
    'VAR'                   : 'VAR'                  ,      ## 지정한 식에 있는 모든 값의 통계적 분산을 반환합니다. OVER 절이 뒤에 올 수도 있습니다.
    'VARP'                  : 'VARP'                 ,      ## 지정한 식에 있는 모든 값의 모집단에 대한 통계적 분산을 반환합니다.
    
    ## 2. Analytic
    'CUME_DIST'              : 'CUM_DIST'            ,      ## SQL Server의 경우 이 함수에서는 값 그룹 내에서 값의 누적 분포를 계산합니다. 
    'FIRST_VALUE'           : 'FIRST_VALUE'          ,      ## SQL Server 2017에서 정렬된 값 집합의 첫 번째 값을 반환합니다.
    'LAG'                   : 'LAG'                  ,      ## SQL Server 2012(11.x)부터 자체 조인을 사용하지 않고 동일한 결과 집합에 있는 이전 행의 데이터에 액세스합니다. LAG 함수를 사용하면 현재 행 앞에 나오는, 지정한 실제 오프셋에 있는 행에 액세스할 수 있습니다. SELECT 문에서 이 분석 함수를 사용하여 현재 행의 값을 이전 행의 값과 비교할 수 있습니다.
    'LAST_VALUE'            : 'LAST_VALUE'           ,      ## SQL Server 2017에서 정렬된 값 집합의 마지막 값을 반환합니다.
    'LEAD'                  : 'LEAD'                 ,      ## SQL Server 2012(11.x)부터 자체 조인을 사용하지 않고 동일한 결과 집합에 있는 다음 행의 데이터에 액세스합니다. LEAD 함수를 사용하면 현재 행 뒤에 나오는, 지정한 실제 오프셋에 있는 행에 액세스할 수 있습니다. SELECT 문에서 이 분석 함수를 사용하여 현재 행의 값을 다음 행의 값과 비교할 수 있습니다.
    'PERCENTILE_CONT'       : 'PERCENTILE_CONT'      ,      ## SQL Server에서 열 값의 연속 분포를 기반으로 백분위수를 계산합니다. 결과는 보간되며 열의 특정 값과 같지 않을 수 있습니다.
    'PERCENTILE_DISC'       : 'PERCENTILE_DISC'      ,      ## SQL Server의 전체 행 집합에 정렬된 값 또는 행 집합의 고유 파티션 내에 정렬된 값의 특정 백분위수를 계산합니다. 지정된 백분위수 값 P에 대해 PERCENTILE_DISC는 ORDER BY 절의 식 값을 정렬하고 P보다 크거나 같은 가장 작은 CUME_DIST 값(동일한 정렬 사양 기준)을 반환합니다. 예를 들어 PERCENTILE_DISC (0.5)는 식의 50번째 백분위수(즉, 중앙값)를 계산합니다. PERCENTILE_DISC는 열 값의 불연속 분포를 기반으로 백분위수를 계산하며 결과는 열의 특정 값과 같습니다.
    'PERCENT_RANK'          : 'PERCENT_RANK'         ,      ## SQL Server 2017의 행 그룹 내에서 행의 상대 순위를 계산합니다. PERCENT_RANK를 사용하여 쿼리 결과 집합 또는 파티션 내에서 값의 상대 순위를 평가할 수 있습니다. PERCENT_RANK는 CUME_DIST 함수와 유사합니다.
    
    ## 3. 데이터 정렬 
    'COLLATIONPROPERTY'     : 'COLLATIONPROPERTY'    ,      ## 이 함수는 SQL Server 2017에서 지정된 데이터 정렬의 속성을 반환합니다.
    'TERTIARY_WEIGHTS'      : 'TERTIARY_WEIGHTS'     ,      ## 비유니코드 문자열 식의 각 문자에 대해 SQL 3차 데이터 정렬로 정의된 이 함수는 정렬 조건(weight)의 이진 문자열로 반환합니다.
    
    ## 4. 변환
    'CAST'                  : 'CAST'                 ,      ## 이러한 함수는 한 데이터 형식의 식을 다른 데이터 형식의 식으로 변환합니다.
    'CONVERT'               : 'CONVERT'              ,      ## 이러한 함수는 한 데이터 형식의 식을 다른 데이터 형식의 식으로 변환합니다.
    'PARSE'                 : 'PARSE'                ,      ## SQL Server에서 요청한 데이터 형식으로 변환된 식 결과를 반환합니다.
    'TRY_CAST'              : 'TRY_CAST'             ,      ## 캐스트에 성공하면 지정한 데이터 형식으로 캐스팅된 값을 반환합니다. 그렇지 않으면 Null을 반환합니다.
    'TRY_CONVERT'           : 'TRY_CONVERT'          ,      ## 캐스트에 성공하면 지정한 데이터 형식으로 캐스팅된 값을 반환합니다. 그렇지 않으면 Null을 반환합니다.
    'TRY_PARSE'             : 'TRY_PARSE'            ,      ## SQL Server에서 요청한 데이터 형식으로 변환된 식 결과를 반환하거나 캐스팅에 실패한 경우 null을 반환합니다. TRY_PARSE는 문자열에서 날짜/시간 및 숫자 형식으로 변환하는 경우에만 사용하세요.

    ## 5. 암호화
    'ASYMKEY_ID'            : 'ASYMKEY_ID'           ,      ## 비대칭 키의 ID를 반환합니다.
    'ASYMKEYPROPERTY'       : 'ASYMKEYPROPERTY'      ,      ## 이 함수는 비대칭 키의 속성을 반환합니다.
    'CERTPROPERTY'          : 'CERTPROPERTY'         ,      ## 지정된 인증서 속성 값을 반환합니다.
    'CERT_ID'               : 'CERT_ID'              ,      ## 이 함수는 인증서의 ID 값을 반환합니다.
    'CRYPT_GEN_RANDOM'      : 'CRYPT_GEN_RANDOM'     ,      ## 이 함수는 CAPI(Crypto API)에서 임의로 생성된 암호화 수를 반환합니다. CRYPT_GEN_RANDOM은 지정된 수의 바이트 길이로 16진수를 반환합니다.
    'DECRYPTBYASYMKEY'      : 'DECRYPTBYASYMKEY'     ,      ## 이 함수는 대칭 키를 사용하여 암호화된 데이터의 암호를 해독합니다.
    'DECRYPTBYCERT'         : 'DECRYPTBYCERT'        ,      ## 이 함수는 인증서의 개인 키를 사용하여 암호화된 데이터의 암호를 해독합니다.
    'DECRYPTBYKEY'          : 'DECRYPTBYKEY'         ,      ## 이 함수는 대칭 키를 사용하여 데이터의 암호를 해독합니다.
    'DECRYPTBYKEYAUTOASYMKEY' : 'DECRYPTBYKEYAUTOASYMKEY',  ## 이 함수는 암호화된 데이터를 암호 해독합니다. 이렇게 하려면 먼저 별도 비대칭 키로 대칭 키를 암호 해독한 다음, 첫 번째 "단계"에서 추출한 대칭 키로 암호화된 데이터를 암호 해독합니다.
    'DECRYPTBYKEYAUTOCERT'  : 'DECRYPTBYKEYAUTOCERT' , 

}'''

system_configuration = {
    '@@DBTS'      : '@@DBTS'     , 
}


t_LPAREN            = r'\('
t_RPAREN            = r'\)'
t_COMMA             = r'\,'
t_SINGLE_QUETO      = r'\''

def t_LITERAL_STR(t):
    r'[a-zA-Z_][a-zA-Z0-9_.]+'
    upper_case_value = t.value.upper()
    t.type = reserved_words.get(upper_case_value, 'ID')
    return t

def t_newline(t):
    r'[\r]?[\n]'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t+'

def t_error(t):
    print("Illegal character: %s" % t.value)
    exit()


#########################################################
#                      T   E   S   T                    #
#########################################################


old_data = '''
IF OBJECT_ID('PaGamePublic.uspRegPackingPathInfo') IS NOT NULL
 BEGIN
    DROP PROCEDURE PaGamePublic.uspRegPackingPathInfo
 END
GO
CREATE PROCEDURE PaGamePublic.uspRegPackingPathInfo
    @packInfoList            PaGamePublic.TblPackingPathInfo_Bulk     READONLY
AS
/*!  
* brief  패킹 경로 정보 추가  
*/  
 BEGIN
    SET NOCOUNT ON                  -- COUNT-set결과를생성하지말아라.
    SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
    SET LOCK_TIMEOUT 3000           -- 함부로변경금지, 변경필요시DBA와협의.
    SET XACT_ABORT ON

    DECLARE @rv  INT = 0  

    BEGIN TRAN uspRegPackingPathInfoTEST_tx1
    /***************************************************************************
    ** 작업시작(이하에만기술)
    ***************************************************************************/


    INSERT INTO TblPackingPathInfo(_ip,_pathName, _imageIdx)  
    SELECT _ip,_pathName, _imageIdx  
        FROM @packInfoList A
            LEFT OUTER JOIN TblPackingPathInfo B
            ON A._ip = B._ip AND A._pathName = B._pathName
        WHERE B._ip IS NULL

    IF (0 <> @@ERROR)
     BEGIN
        SET @rv = -1
        GOTO LABEL_END
     END

    /***************************************************************************
    ** 작업종료(이상에만기술)
    ***************************************************************************/

LABEL_END:
    IF(0 = @rv)
     BEGIN
        COMMIT TRAN
     END
    ELSE
     BEGIN
        ROLLBACK TRAN
     END

    RETURN(@rv)
 END
GO
'''

lexer_old = lex.lex()
lexer_old.input(old_data)

while True:
    tok = lexer_old.token()
    if not tok: 
        break      # No more input
    print(tok)