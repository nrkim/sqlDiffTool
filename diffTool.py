# -*- coding: utf-8 -*-

import ply.lex as lex
import re

states = (
    ('ccode', 'exclusive'),
    ## XML / CLR 등의 언어는 무시할수 있도록 , 다른 Lexer 이용 
)

## 예약어 Sql Server 2017
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
    'GO'               : 'GO'               ,
    

    'SEMANTICKEYPHRASETABLE': 'SEMANTICKEYPHRASETABLE'                  ,
    'SEMANTICSIMILARITYDETAILSTABLE': 'SEMANTICSIMILARITYDETAILSTABLE'  ,
    'SEMANTICSIMILARITYTABLE': 'SEMANTICSIMILARITYTABLE'
}

data_types ={
    ## 정확한 수치
    'BIT'           : 'BIT'             , ## 1, 0 또는 NULL 값을 가질 수 있는 정수 데이터 형식
    'SMALLINT'      : 'SMALLINT'        , ## 2바이트 -2^15(-32,768) ~ 2^15-1(32,767)
    'BIGINT'        : 'BIGINT'          , ## 8바이트 -2^63(-9,223,372,036,854,775,808) ~ 2^63-1(9,223,372,036,854,775,807)
    'INT'           : 'INT'             , ## 4바이트 -2^31(-2,147,483,648) ~ 2^31-1(2,147,483,647)
    'TINYINT'       : 'TINYINT'         , ## 1바이트 0 ~ 255	
    'NUMERIC'       : 'NUMERIC'         , ## numeric(자리수,소수점자리수)
    'DECIMAL'       : 'DECIMAL'         , ## decimal(자리수,소수점자리수)
    'MONEY'         : 'MONEY'           , ## 8바이트 -922,337,203,685,477.5808~922,337,203,685,477.5807(-922,337,203,685,477.58 ~ 922,337,203,685,477.58(Informatica의 경우) Informatica는 4개가 아닌 2개의 소수만 지원합니다.)
    'SMALLMONEY'    : 'SMALLMONEY'      , ## 4바이트 - 214,748.3648 - 214,748.3647	
    
    ## 근사치
    'FLOAT'         : 'FLOAT'           , ## float(n) - 1.79E+308에서 -2.23E-308, 0과 2.23E-308에서 1.79E+308	이 값은 n의 값에 따라 달라집니다.
    'REAL'          : 'REAL'            , ## real(n) - 3.40E+38에서 -1.18E - 38, 0과 1.18E-38에서 3.40E + 38	4바이트
    
    ## 날짜 및 시간
    'DATE'          : 'DATE'            , ## YYYY는 0001에서 9999 사이에 속하는 4자리 숫자로, 연도를 나타냅니다. Informatica의 경우, YYYY는 1582에서 9999까지의 범위로 제한됩니다. MM은 01에서 12 사이에 속하는 두 자리 숫자로, 지정한 연도의 월을 나타냅니다. DD는 월에 따라 01에서 31 사이에 속하는 두 자리 숫자로, 특정 월의 일을 나타냅니다.
    'DATETIME'      : 'DATETIME'        , ## 소수 자릿수 초가 있는 24시간제 기준의 시간과 결합된 날짜를 정의합니다.
    'DATETIMEOFFSET': 'DATETIMEOFFSET'  , ## 표준 시간대를 인식하며 24시간제를 기준으로 하는 시간과 결합된 날짜를 정의합니다.
    'DATETIME2'     : 'DATETIME2'       , ## 24시간제 기준의 시간과 결합된 날짜를 정의합니다. datetime2는 더 큰 날짜 범위, 더 많은 기본 소수 자릿수, 선택 항목인 사용자 지정 전체 자릿수를 갖는 기존 datetime 형식의 확장으로 볼 수 있습니다.
    'SMALLDATETIME' : 'SMALLDATETIME'   , ## 날짜와 시간을 정의합니다. 시간은 하루 24시간을 기준으로 하며 초는 항상 소수 자릿수 없이 0(:00)으로 표시됩니다.
    'TIME'          : 'TIME'            , ## 시간을 정의합니다. 시간은 표준 시간대를 인식하지 않으며 24시간제를 기준으로 합니다.
    
    ## 문자열
    'CHAR'          : 'CHAR'            , ## 고정 길이 데이터 형식입니다.
    'VARCHAR'       : 'VARCHAR'         , ## 가변 길이 데이터 형식입니다. 
    
    ## 유니코드 문자열
    'NCHAR'	        : 'NCHAR'           , ## 고정 길이 유니코드 문자열 데이터. n은 문자열 길이를 정의하며 1에서 4,000 사이여야 합니다. 저장소 크기는 n바이트의 두 배입니다. 데이터 정렬 코드 페이지에서 더블바이트 문자를 사용할 경우 저장소 크기는 계속 n바이트입니다. 문자열에 따라 n바이트의 저장소 크기가 n에 지정된 값보다 작을 수도 있습니다. nchar의 ISO 동의어는 national char와 national character입니다.
    'NVARCHAR'      : 'NVARCHAR'        , ## 가변 길이 유니코드 문자열 데이터입니다. n은 문자열 길이를 정의하며 1에서 4,000 사이가 될 수 있습니다. max는 최대 저장소 크기가 2^30-1자임을 나타냅니다. 바이트의 최대 저장소 크기는 2GB입니다. 실제 저장소 크기(바이트)는 입력된 문자 수의 두 배 + 2바이트입니다. nvarchar의 ISO 동의어는 national char varying 및 national character varying로 다양합니다.
    
    ## 이진 문자열
    'BINARY'        : 'BINARY'           , ## 고정길이 데이터 형식 열 데이터 항목의 크기가 일관적입니다.
    'VARBINARY'     : 'VARBINARY'        , ## 열 데이터 항목의 크기가 상당히 다릅니다. varbinary(max)	열 데이터 항목이 8,000바이트를 초과합니다.

    ## 중요! ntext, text 및 image 데이터 형식은 이후 버전의 SQL Server에서 제거될 예정입니다. 향후 개발 작업에서는 이 데이터 형식을 사용하지 않도록 하고 현재 이 데이터 형식을 사용하는 응용 프로그램은 수정하세요. 대신 nvarchar(max), varchar(max)및 varbinary(max) 를 사용합니다.
    'NTEXT'         : 'NTEXT'           , ## 최대 문자열 길이가 2^30 - 1(1,073,741,823)바이트인 가변 길이 유니코드 데이터입니다. 바이트 단위의 저장소 크기는 입력된 문자열 길이의 두 배입니다. ntext의 ISO 동의어는 national text입니다.
    'TEXT'          : 'TEXT'            , ## 서버의 코드 페이지에 있는 최대 문자열 길이가 2^31 - 1(2,147,483,647)인 비유니코드 가변 길이 데이터입니다. 서버 코드 페이지에서 더블바이트 문자를 사용하더라도 저장소 크기는 그대로 2,147,483,647바이트입니다. 문자열에 따라 저장소 크기가 2,147,483,647바이트보다 작을 수도 있습니다.
    'IMAGE'         : 'IMAGE'           , ## 0에서 2^31-1(2,147,483,647)바이트의 가변 길이 이진 데이터입니다.

    ## 기타 데이터 형식
    ## 'CURSOR'        : 'CURSOR'          , ## 커서에 대한 참조가 들어 있는 변수 또는 저장 프로시저 OUTPUT 매개 변수의 데이터 형식입니다. cursor 데이터 형식으로 만들어진 모든 변수는 Null을 허용합니다. cursor 데이터 형식은 CREATE TABLE 문에 있는 열에서 사용할 수 없습니다.
    'ROWVERSION'    : 'ROWVERSON'       , ## 데이터베이스 내에서 자동으로 생성된 고유 이진 숫자를 표시하는 데이터 형식입니다. 일반적으로 rowversion은 버전이 표시되는 테이블 행에 대한 메커니즘으로 사용됩니다. 저장소 크기는 8바이트입니다. rowversion 데이터 형식은 증가하는 숫자일 뿐이며 날짜 또는 시간을 보존하지 않습니다. 날짜 또는 시간을 기록하려면 datetime2 데이터 형식을 사용합니다.
    'HIERARCHYID'   : 'HIERARCHYID'     , ## hierarchyid 데이터 형식은 가변 길이의 시스템 데이터 형식입니다. hierarchyid는 계층에서의 위치를 나타내는 데 사용됩니다. hierarchyid 형식의 열은 자동으로 트리를 나타내지 않습니다. 응용 프로그램에 따라 원하는 행 간 관계가 값에 반영되도록 hierarchyid 값이 생성되어 할당됩니다.
    'UNIQUEIDENTIFIER' : 'UNIQUEIDENTIFIER' , ## 16바이트 GUID입니다.
    'SQL_VARIANT'   : 'SQL_VARIANT'     , ## SQL Server에서 지원하는 여러 가지 데이터 형식의 값을 저장하는 데이터 형식입니다.
    'GEOMETRY'      : 'GEOMETRY'        , ## 평면 공간 데이터 형식인 geometry는 SQL Server에서 CLR(공용 언어 런타임) 데이터 형식으로 구현됩니다. 이 데이터 형식은 유클리드(평면) 좌표 시스템의 데이터를 나타냅니다.
    'GEOGRAPHY'     : 'GEOGRAPHY'       , ## geography 공간 데이터 형식인 geography는 SQL Server에서 .NET CLR(공용 언어 런타임) 데이터 형식으로 구현됩니다. 이 데이터 형식은 둥근 표면 좌표 시스템의 데이터를 나타냅니다. SQL Server geography 데이터 형식은 GPS 위도 및 경도 좌표 등의 타원(둥근 표면) 데이터를 저장합니다.
    ##'TABLE_TYPE'    : 'TABLE'         , ## 사용자 정의 테이블 타입
}

system_configuration = {
    ##'SYS_DBTS'               : '@@DBTS'             , 
    ##'SYS_PARTITION'          : '$PARTITION'         , 
    'SYS_ERROR_PROCEDURE'    : 'ERROR_PROCEDURE'    ,
    ##'SYS_ERROR'              : '@@ERROR'            , 
    'SYS_ERROR_SEVERITY'     : 'ERROR_SEVERITY'     ,
    ##'SYS_IDENTITY'           : '@@IDENTITY'         ,
    'SYS_ERROR_STATE'        : 'ERROR_STATE'        , 
    'SYS_FORMATMESSAGE'      : 'FORMATMESSAGE'      ,
	##'SYS_PACK_RECEIVED'      : '@@PACK_RECEIVED'    , 
    ##'SYS_ROWCOUNT'           : '@@ROWCOUNT'         ,
    ##'SYS_TRANCOUNT'          : '@@TRANCOUNT'        ,
    'SYS_GETANSINULL'        : 'GETANSINULL'        ,
    'SYS_BINARY_CHECKSUM'    : 'BINARY_CHECKSUM'    ,
    'SYS_HOST_ID'            : 'HOST_ID'            ,
    'SYS_CHECKSUM'           : 'CHECKSUM'           ,
    'SYS_HOST_NAME'          : 'HOST_NAME'          , 
    'SYS_COMPRESS'           : 'COMPRESS'           ,
    'SYS_ISNULL'             : 'ISNULL'             , 
    'SYS_CONNECTIONPROPERTY' : 'CONNECTIONPROPERTY' ,
    'SYS_CONTEXT_INFO'       : 'CONTEXT_INFO'       , 
    'SYS_CURRENT_REQUEST_ID' : 'CURRENT_REQUEST_ID' ,
    'SYS_NEWID'              : 'NEWID'              , 
    'SYS_NEWSEQUENTIALID'    : 'NEWSEQUENTIALID'    , 
    'SYS_DECOMPRESS'         : 'DECOMPRESS'         , 
    'SYS_ROWCOUNT_BIG'       : 'ROWCOUNT_BIG'       , 
    'SYS_ERROR_LINE'         : 'ERROR_LINE'         , 
    'SYS_SESSION_CONTEXT'    : 'SESSION_CONTEXT'    , 
    'SYS_ERROR_MESSAGE'      : 'ERROR_MESSAGE'      ,
    'SYS_SESSION_ID'         : 'SESSION_ID'         , 
    'SYS_ERROR_NUMBER'       : 'ERROR_NUMBER'       , 
    'SYS_XACT_STATE'         : 'XACT_STATE'         ,
    'SYS_CURRENT_TRANSACTION_ID' : 'CURRENT_TRANSACTION_ID'                         ,
    'SYS_MIN_ACTIVE_ROWVERSION' : 'MIN_ACTIVE_ROWVERSION'                           ,
    'SYS_GET_FILESTREAM_TRANSACTION_CONTEXT' : 'GET_FILESTREAM_TRANSACTION_CONTEXT' ,

    ## 집계 
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
    
    ## Analytic
    'CUME_DIST'              : 'CUM_DIST'            ,      ## SQL Server의 경우 이 함수에서는 값 그룹 내에서 값의 누적 분포를 계산합니다. 
    'FIRST_VALUE'           : 'FIRST_VALUE'          ,      ## SQL Server 2017에서 정렬된 값 집합의 첫 번째 값을 반환합니다.
    'LAG'                   : 'LAG'                  ,      ## SQL Server 2012(11.x)부터 자체 조인을 사용하지 않고 동일한 결과 집합에 있는 이전 행의 데이터에 액세스합니다. LAG 함수를 사용하면 현재 행 앞에 나오는, 지정한 실제 오프셋에 있는 행에 액세스할 수 있습니다. SELECT 문에서 이 분석 함수를 사용하여 현재 행의 값을 이전 행의 값과 비교할 수 있습니다.
    'LAST_VALUE'            : 'LAST_VALUE'           ,      ## SQL Server 2017에서 정렬된 값 집합의 마지막 값을 반환합니다.
    'LEAD'                  : 'LEAD'                 ,      ## SQL Server 2012(11.x)부터 자체 조인을 사용하지 않고 동일한 결과 집합에 있는 다음 행의 데이터에 액세스합니다. LEAD 함수를 사용하면 현재 행 뒤에 나오는, 지정한 실제 오프셋에 있는 행에 액세스할 수 있습니다. SELECT 문에서 이 분석 함수를 사용하여 현재 행의 값을 다음 행의 값과 비교할 수 있습니다.
    'PERCENTILE_CONT'       : 'PERCENTILE_CONT'      ,      ## SQL Server에서 열 값의 연속 분포를 기반으로 백분위수를 계산합니다. 결과는 보간되며 열의 특정 값과 같지 않을 수 있습니다.
    'PERCENTILE_DISC'       : 'PERCENTILE_DISC'      ,      ## SQL Server의 전체 행 집합에 정렬된 값 또는 행 집합의 고유 파티션 내에 정렬된 값의 특정 백분위수를 계산합니다. 지정된 백분위수 값 P에 대해 PERCENTILE_DISC는 ORDER BY 절의 식 값을 정렬하고 P보다 크거나 같은 가장 작은 CUME_DIST 값(동일한 정렬 사양 기준)을 반환합니다. 예를 들어 PERCENTILE_DISC (0.5)는 식의 50번째 백분위수(즉, 중앙값)를 계산합니다. PERCENTILE_DISC는 열 값의 불연속 분포를 기반으로 백분위수를 계산하며 결과는 열의 특정 값과 같습니다.
    'PERCENT_RANK'          : 'PERCENT_RANK'         ,      ## SQL Server 2017의 행 그룹 내에서 행의 상대 순위를 계산합니다. PERCENT_RANK를 사용하여 쿼리 결과 집합 또는 파티션 내에서 값의 상대 순위를 평가할 수 있습니다. PERCENT_RANK는 CUME_DIST 함수와 유사합니다.
    
    ## 데이터 정렬 
    'COLLATIONPROPERTY'     : 'COLLATIONPROPERTY'    ,      ## 이 함수는 SQL Server 2017에서 지정된 데이터 정렬의 속성을 반환합니다.
    'TERTIARY_WEIGHTS'      : 'TERTIARY_WEIGHTS'     ,      ## 비유니코드 문자열 식의 각 문자에 대해 SQL 3차 데이터 정렬로 정의된 이 함수는 정렬 조건(weight)의 이진 문자열로 반환합니다.
    
    ## 변환
    'CAST'                  : 'CAST'                 ,      ## 이러한 함수는 한 데이터 형식의 식을 다른 데이터 형식의 식으로 변환합니다.
    ##'CONVERT'               : 'CONVERT'              ,      ## 이러한 함수는 한 데이터 형식의 식을 다른 데이터 형식의 식으로 변환합니다.
    'PARSE'                 : 'PARSE'                ,      ## SQL Server에서 요청한 데이터 형식으로 변환된 식 결과를 반환합니다.
    'TRY_CAST'              : 'TRY_CAST'             ,      ## 캐스트에 성공하면 지정한 데이터 형식으로 캐스팅된 값을 반환합니다. 그렇지 않으면 Null을 반환합니다.
    ##'TRY_CONVERT'           : 'TRY_CONVERT'          ,      ## 캐스트에 성공하면 지정한 데이터 형식으로 캐스팅된 값을 반환합니다. 그렇지 않으면 Null을 반환합니다.
    'TRY_PARSE'             : 'TRY_PARSE'            ,      ## SQL Server에서 요청한 데이터 형식으로 변환된 식 결과를 반환하거나 캐스팅에 실패한 경우 null을 반환합니다. TRY_PARSE는 문자열에서 날짜/시간 및 숫자 형식으로 변환하는 경우에만 사용하세요.

    ## 암호화
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

    'NOCOUNT'               : 'NOCOUNT',
    'ISOLATION'             : 'ISOLATION',
    'LEVEL'                 : 'LEVEL',
    'UNCOMMITTED'           : 'UNCOMMITTED',
    'LOCK_TIMEOUT'          : 'LOCK_TIMOUT',
    'XACT_ABORT'            : 'XACT_ABORT',
    'READONLY'              : 'READONLY',
}

## ##
## 토큰 
tokens = tuple(reserved_words.values()) + tuple(data_types.values()) + tuple(system_configuration.values()) + (    
    ## system global variable
    'SYS_GLOBAL_VAR'    , ## @@
    'SYS_PARTITION'     ,

    # BATCH
    'SEMI'              , ## ;
    ## 객체 이름 등 
    'SINGLE_QUETO'      , ## '         
   
    ## 사칙연산
    'PLUS'              , ## +
    'MINUS'             , ## -    
    'TIMES'             , ## *
    'DIVIDE'            , ## /
    ## 비교
    'EQUALS'            , ## =
    'LT'                , ## <
    'LE'                , ## <=
    'GT'                , ## >
    'GE'                , ## >=
    'NE'                , ## <>
    ## 괄호 Parenthesis
    'LPAREN'            , ## (
    'RPAREN'            , ## )
    'COMMA'             , ## ,
    ## 기타 
    ##'INTEGER'           , ## 23 
    ##'FLOAT_NUM'             , ## 23.1

    'LITERAL_STR'       , ## 
    'ID'                , ## TYPE 
    'COMMENT'           , ## 
    'COMMENTS'          , ## 
    'NUMBER'            ,
    'COLON'
)


## 사칙연산
t_PLUS              = r'\+'
t_MINUS             = r'-'
t_TIMES             = r'\*'
t_DIVIDE            = r'/'

## 비교
t_EQUALS            = r'='
t_LT                = r'<'
t_LE                = r'<='
t_GT                = r'>'
t_GE                = r'>='
t_NE                = r'<>'

## 괄호 Parenthesis
t_LPAREN            = r'\('
t_RPAREN            = r'\)'
t_COMMA             = r'\,'
t_COLON             = r':'

t_SINGLE_QUETO      = r'\''
t_SEMI              = r';'
t_ignore            = '[\t| +]*' ## tab  스페이스 및 한줄 짜리 주석 까지 무시 
# Ignored characters (whitespace)
t_ccode_ignore = " \t\n"

##t_INTEGER           = r'\d+'
##t_FLOAT_NUM         = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
##t_STRING            = r'\".*?\"'
##t_SYS_GLOBAL_VAR    = r'@@+'
##t_SYS_PARTITION     = r'$PARTITION'

# Match the first /*. Enter COMMENTS state.
def t_COMMENT(t):
    r'--.*'
    pass
    ##return t

def t_COMMENTS(t):
    r'/\*'
    t.lexer.code_start = t.lexer.lexpos        # Record the starting position
    t.lexer.level = 1                          # Initial brace level
    t.lexer.begin('ccode')                     # Enter 'ccode' state


# Rules for the COMMENTS state
def t_ccode_LBRACE(t):     
    r'/\*'
    t.lexer.level +=1                

def t_ccode_RBRACE(t):
    r'\*/'
    t.lexer.level -=1

    # If closing brace, return the code fragment
    if t.lexer.level == 0:
         t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
         t.type = "COMMENTS"
         t.lexer.lineno += t.value.count('\n')
         t.lexer.begin('INITIAL')
         pass           
         ##return t

# For bad characters, we just skip over it
def t_ccode_error(t):
    t.lexer.skip(1)


def t_NUMBER(t):
    r'\d+'
    return t


def t_SYS_GLOBAL_VAR(t):
    r'@@+'
    return t

def t_VAR(t):
    r'@[a-zA-Z0-9_.]+'
    return t

def t_LITERAL_STR(t):
    r'[a-zA-Z_][a-zA-Z0-9_.]*'
    upper_case_value = t.value.upper()
    t.type = reserved_words.get(upper_case_value, 'ID')
    return t

def t_newline(t):
    r'[\r]?[\n]'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character: %s" % t.value)
    ##t.lexer.skip(1)
    exit()



#########################################################
#                      T   E   S   T                    #
#########################################################


old_data = '''
'''

lexer_old = lex.lex(reflags=re.UNICODE | re.VERBOSE)
lexer_old.input(old_data)

while True:
    tok = lexer_old.token()
    if not tok: 
        break      # No more input
    print(tok)
