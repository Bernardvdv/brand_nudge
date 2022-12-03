CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateBatchID`(IN BatchID nvarchar(30))
BEGIN
INSERT INTO `brandnudge`.`audit`
(`BatchID`,
`NumberOfInserts`,
`DateTimeInserted`)
VALUES(BatchID,
(SELECT COUNT(id) from products where ProductsBatchID = BatchID),
CURRENT_TIMESTAMP()); 
END