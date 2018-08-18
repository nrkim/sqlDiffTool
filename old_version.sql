-- USE GAMEDB
-- GO

IF OBJECT_ID(N'PaGamePrivate.TblCatchTroller') IS NOT NULL
 BEGIN
    DROP TABLE PaGamePrivate.TblCatchTroller
 END
GO
CREATE TABLE PaGamePrivate.TblCatchTroller
(
    _userNo     BIGINT
    , _count    INT 
)
GO