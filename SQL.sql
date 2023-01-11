--
-- Database: `pes1ug20cs461_blood_bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `461_person`
--

CREATE TABLE 461_PERSON (
    pid char(5), 
    fname varchar(15) NOT NULL, 
    lname varchar(15) NOT NULL,
    DOB date,
    `address` varchar(50),
    sex char,
    phone int,
    height decimal(5,2),
    `weight` decimal(5,2),
    can_donate char NOT NULL,
    last_donation date
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_person`
--
LOAD DATA INFILE 'D:/Tanvi/PES/Sem5/301_DBMS/Project/Person.csv'
INTO TABLE 461_PERSON 
COLUMNS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
ESCAPED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;


-- --------------------------------------------------------

--
-- Table structure for table `461_donation`
--

CREATE TABLE 461_DONATION (
    did char(5),
    date_donated date NOT NULL,
    type_donated varchar(20) NOT NULL,
    quantity decimal(5,2) NOT NULL,
    blood_group varchar(3) DEFAULT NULL,
    pid char(5) DEFAULT NULL,
    eid char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_donation`
--

INSERT INTO 461_DONATION VALUES ("D_35", "2020-04-17", "Blood",400, "O+", "P_48","E_18");
INSERT INTO 461_DONATION VALUES ("D_47","2021-02-11","Plasma",470,"B-","P_32","E_18");
INSERT INTO 461_DONATION VALUES ("D_80","2021-07-26","Blood",320,"A+","P_74","E_99");
INSERT INTO 461_DONATION VALUES ("D_83","2019-08-05","Platelets",450,"AB-","P_20","E_98");
INSERT INTO 461_DONATION VALUES ("D_90","2022-09-23","Blood",470,"B-","P_32","E_83");

-- --------------------------------------------------------


--
-- Table structure for table `461_employee`
--

CREATE TABLE 461_EMPLOYEE (
    eid char(5) DEFAULT NULL,
    `name` varchar(15) NOT NULL,
    designation varchar(20) DEFAULT NULL,
    date_of_joining date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_employee`
--
INSERT INTO 461_EMPLOYEE (`eid`,`name`,`designation`,`date_of_joining`)VALUES
("E_98","Bev","Nurse","2019-04-28"),
("E_18","Kelwin","Sr Nurse", "2018-01-02"),
("E_99","Gwenni","Nurse","2019-09-20"),
("E_43","Andriette","Jr Nurse",	"2020-08-12"),
("E_83","Stevy","Jr Nurse","2020-11-15");



-- --------------------------------------------------------
--
-- Table structure for table `461_receive`
--

CREATE TABLE 461_RECEIVE (
    rid char(5),
    date_received date NOT NULL,
    type_received varchar(20) NOT NULL,
    blood_group char DEFAULT NULL,
    quantity_received decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_receive`
--
INSERT INTO 461_RECEIVE VALUES ("R_35",	"2019-07-20","Platelets","A-",465);
INSERT INTO 461_RECEIVE VALUES ("R_47",	"2022-07-19","Blood",	"AB+",470);
INSERT INTO 461_RECEIVE VALUES ("R_48",	"2018-10-04","Blood",	"O+",430);
INSERT INTO 461_RECEIVE VALUES ("R_72",	"2021-03-10","Plasma",	"B-",300);
INSERT INTO 461_RECEIVE VALUES ("R_81",	"2020-05-02","Blood","O+",390);

-- --------------------------------------------------------
--
-- Table structure for table `461_payment`
--

CREATE TABLE 461_PAYMENT (
    rid char(5) DEFAULT NULL,
    transaction_id int(11) NOT NULL,
    bank varchar(20) DEFAULT NULL,
    date_trans date NOT NULL,
    account_no varchar(20) DEFAULT NULL,
    amount decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_payment`
--

INSERT INTO 461_PAYMENT VALUES ("R_35",	"809276","UNION BANK","2019-07-20","62752161050",600);
INSERT INTO 461_PAYMENT VALUES ("R_47",	"678756","KOTAK","2022-07-19","25117151590",700);
INSERT INTO 461_PAYMENT VALUES ("R_48",	"421678","SBI",	"2018-10-04","31867857630",675);
INSERT INTO 461_PAYMENT VALUES ("R_72",	"324304","ICICI","2021-03-10","36223120970",800);
INSERT INTO 461_PAYMENT VALUES ("R_81","977538","UION BANK","2020-05-02","67240893420",950);

-- --------------------------------------------------------


--
-- Table structure for table `461_stock`
--

CREATE TABLE 461_STOCK (
    `sid` char(5),
    `type` varchar(20) NOT NULL,
    `blood_group` varchar(3) DEFAULT NULL,
    `left` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_stock`
--

INSERT INTO 461_STOCK VALUES ("S_01","Blood","O+",10);
INSERT INTO 461_STOCK VALUES ("S_02","Plasma","B-",170);
INSERT INTO 461_STOCK VALUES ("S_03","Blood","A+",320);
INSERT INTO 461_STOCK VALUES ("S_04","Platelets","AB-",450);
INSERT INTO 461_STOCK VALUES ("S_05","Blood","O-",470);

-- --------------------------------------------------------

--
-- Table structure for table `461_receives`
--

CREATE TABLE 461_RECEIVES (
    rid char(5) DEFAULT NULL,
    pid char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_receives`
--

INSERT INTO 461_RECEIVES VALUES ("R_35","P_48");
INSERT INTO 461_RECEIVES VALUES ("R_47","P_09");
INSERT INTO 461_RECEIVES VALUES ("R_48","P_52");
INSERT INTO 461_RECEIVES VALUES ("R_72","P_13");
INSERT INTO 461_RECEIVES VALUES ("R_81","P_54");

-- --------------------------------------------------------

--
-- Table structure for table `461_decrements`
--

CREATE TABLE 461_DECREMENTS (
    rid char(5) DEFAULT NULL,
    `sid` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_decrements`
--

INSERT INTO 461_DECREMENTS VALUES ("R_72", "S_02");
INSERT INTO 461_DECREMENTS VALUES ("R_81", "S_01");

-- --------------------------------------------------------
--
-- Table structure for table `461_increments`
--

CREATE TABLE 461_INCREMENTS (
    did char(5) DEFAULT NULL,
    `sid` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `461_increments`
--

INSERT INTO 461_INCREMENTS VALUES ("D_35","S_01");
INSERT INTO 461_INCREMENTS VALUES ("D_47","S_02");
INSERT INTO 461_INCREMENTS VALUES ("D_80","S_03");
INSERT INTO 461_INCREMENTS VALUES ("D_83","S_04");
INSERT INTO 461_INCREMENTS VALUES ("D_90","S_05");

-- --------------------------------------------------------
--
-- Indexes for dumped tables
--

ALTER TABLE `461_PERSON`
    ADD CONSTRAINT `pk_person` PRIMARY KEY (`pid`);

ALTER TABLE `461_DONATION`
    ADD CONSTRAINT `pk_donation` PRIMARY KEY (`did`);

ALTER TABLE `461_EMPLOYEE`
    ADD CONSTRAINT `pk_employee` PRIMARY KEY (`eid`);

ALTER TABLE `461_RECEIVE`
    ADD CONSTRAINT `pk_receive` PRIMARY KEY (`rid`);

ALTER TABLE `461_STOCK`
    ADD CONSTRAINT `pk_stock` PRIMARY KEY (`sid`);

ALTER TABLE `461_PAYMENT`
    ADD CONSTRAINT `pk_payment` PRIMARY KEY (`transaction_id`);

-- --------------------------------------------------------

--
-- Foreign Key Constraints for dumped tables
--

ALTER TABLE `461_donation`
    ADD CONSTRAINT `fk_donation_person` FOREIGN KEY (`pid`) REFERENCES `461_person` (`pid`),
    ADD CONSTRAINT `fk_donation_employee` FOREIGN KEY (`eid`) REFERENCES `461_employee` (`eid`);

ALTER TABLE `461_payment`
    ADD CONSTRAINT `fk_payment_receive` FOREIGN KEY (`rid`) REFERENCES `461_receive` (`rid`);

ALTER TABLE `461_becomes`
    ADD CONSTRAINT `fk_becomes_receive` FOREIGN KEY (`rid`) REFERENCES `461_receive` (`rid`),
    ADD CONSTRAINT `fk_becomes_person` FOREIGN KEY (`pid`) REFERENCES `461_person` (`pid`);

ALTER TABLE `461_decrements`
    ADD CONSTRAINT `fk_decrements_receive` FOREIGN KEY (`rid`) REFERENCES `461_receive` (`rid`),
    ADD CONSTRAINT `fk_decrements_stock` FOREIGN KEY (`sid`) REFERENCES `461_stock` (`sid`);


ALTER TABLE `461_increments`
    ADD CONSTRAINT `fk_increments_donation` FOREIGN KEY (`did`) REFERENCES `461_donation` (`did`),
    ADD CONSTRAINT `fk_increments_stock` FOREIGN KEY (`sid`) REFERENCES `461_stock` (`sid`);

--
-- Check Constraints
--

ALTER TABLE 461_Person
    ADD CONSTRAINT check_gender CHECK (sex = 'M' OR sex = 'F'),
    ADD CONSTRAINT check_can_donate CHECK (can_donate = 'Y' OR can_donate = 'N')

INSERT INTO 461_PERSON VALUES("P_10","Lakshmi","Swamy","2008-07-17","M G Road",'GIRL',8378296214,144,48,'N',NULL)

ALTER TABLE 461_Person
    ALTER can_donate SET DEFAULT 'N';

INSERT INTO 461_PERSON VALUES("P_02","Ravi","Shankar","2010-09-30","M G Road",'F',8378692214,152,58,DEFAULT,NULL)

ALTER TABLE 461_PERSON
    ADD CONSTRAINT `chk_no` CHECK (phone like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');

-- Update --
UPDATE 461_PERSON
SET 
    last_donation = NULL 
WHERE
    last_donation = 0000-00-00;

-- Delete No SS-- 
DELETE from 461_PERSON WHERE pid = 'P_02';
DELETE from 461_PERSON WHERE pid = 'P_10';

-- --------------------------------------------------------

-- JOIN QUERIES --
--Q1
SELECT 461_donation.pid, did, fname, lname, quantity 
FROM 461_DONATION join 461_PERSON on 461_donation.pid=461_person.pid 
WHERE 461_donation.quantity>(SELECT AVG(461_donation.quantity) FROM 461_donation);
--Q2
SELECT P.fname, P.lname, P.address, D.type_donated, D.blood_group
FROM 461_Person as P LEFT OUTER JOIN 461_DONATION as D ON P.pid=D.pid;
--Q3
SELECT E.eid, E.name, E.designation, E.date_of_joining, D.did
FROM 461_EMPLOYEE as E join 461_DONATION as D ON E.eid=D.eid;
--Q4
SELECT 461_person.pid, rid, fname, lname, sex, height, `weight` 
FROM 461_BECOMES right outer join 461_PERSON on 461_PERSON.pid=461_BECOMES.pid;
-- --------------------------------------------------------

-- AGGREGATE FUNCTIONS --
--Q1 
SELECT D.eid, E.name, count(*) as number_of_donations_taken
FROM 461_DONATION D, 
    461_EMPLOYEE E
WHERE D.eid = E.eid
GROUP BY (D.eid);
--Q2
SELECT avg(quantity)
FROM 461_DONATION D;
--Q3
SELECT max(amount) as Max_Cost, min(amount) as Min_Cost, avg(amount) as Average_Cost
FROM 461_PAYMENT;
--Q4
SELECT blood_group,sum(`left`)
FROM 461_STOCK 
GROUP BY(blood_group);
-- --------------------------------------------------------

-- SET OPERATION --
--Q1
SELECT P.pid, P.fname, P.lname
FROM 461_person P,
    461_donation D
WHERE P.pid = D.pid
UNION 
SELECT P.pid, P.fname, P.lname
FROM 461_person P,
    461_becomes B
WHERE P.pid = B.pid
;
--Q2
SELECT P1.pid, P1.fname, P1.lname
FROM 461_person P1,
    461_donation D
WHERE P1.pid = D.pid and
EXISTS ( 
SELECT P2.pid, P2.fname, P2.lname
FROM 461_person P2,
    461_becomes B
WHERE P2.pid = B.pid and P1.pid = P2.pid
);
--Q3
SELECT P1.pid, P1.fname, P1.lname
FROM 461_person P1,
    461_donation D
WHERE P1.pid = D.pid and
NOT EXISTS ( 
SELECT P2.pid, P2.fname, P2.lname
FROM 461_person P2,
    461_becomes B
WHERE P2.pid = B.pid and P1.pid = P2.pid
);
--Q4
SELECT P1.pid, P1.fname, P1.lname
FROM 461_person P1
WHERE P1.pid not in ( 
SELECT P.pid
FROM 461_person P,
    461_donation D
WHERE P.pid = D.pid
UNION 
SELECT P.pid
FROM 461_person P,
    461_becomes B
WHERE P.pid = B.pid
);
-- --------------------------------------------------------
--function to print universal donor on entring blood group
DELIMITER $$
CREATE FUNCTION 461_donor_type(blood_group varchar(3))
RETURNS varchar(150)
DETERMINISTIC
BEGIN
DECLARE value varchar(150);
IF blood_group like "O-" then
SET value = "Universal Donor";
END IF;
IF blood_group like "AB+" then
SET value = "Universal Receiver";
END IF;
IF blood_group like "O+" then
SET value = "Donor for all Positive Blood Groups";
ELSE
SET value = "Rare Blood Group";
END IF;
RETURN value;
END $$
DELIMITER;

WITH dude as 
(SELECT blood_group 
FROM 461_donation
)
SELECT blood_group,461_donor_type(blood_group) as Result FROM dude;

-- FUNCTION --
DELIMITER $$
CREATE FUNCTION 461_donate_age(dob date)
RETURNS varchar(150)
DETERMINISTIC
BEGIN
DECLARE value varchar(150);
IF ((year(curdate()) - year(dob)) > 18 and (year(curdate()) - year(dob)) < 65) then
SET value = "Based on their age person CAN donate blood";
ELSE
SET value = "Based on their age person CANNOT donate blood";
END IF;
RETURN value;
END $$
DELIMITER;

WITH dude as 
(SELECT pid, dob 
FROM 461_person
)
SELECT pid, dob, 461_donate_age(dob) as Decision FROM dude;

-- --------------------------------------------------------

-- PROCEDURE --
DELIMITER $$
CREATE PROCEDURE 461_amt_chk(
IN bg varchar(5),IN amt int, OUT msg varchar(50))
BEGIN
DECLARE `left` int;
UPDATE 461_STOCK
SET `left` = amt
WHERE blood_group= bg;
SET msg='Amount Updated';
END;$$
DELIMITER ;

CALL 461_amt_chk('O+',200,@A);
SELECT @A;
SELECT * FROM 461_stock;

-- --------------------------------------------------------
-- TRIGGER --
--TRIGGER TO UPDATE THE STOCK TABLE WHEN A DONATION IS MADE

DELIMITER $$
CREATE TRIGGER 461_stock_update
AFTER INSERT
ON 461_DONATION FOR EACH ROW
BEGIN
UPDATE 461_STOCK
SET `left` = `left` + new.quantity
WHERE blood_group= new.blood_group;
END $$
DELIMITER ;

--trigger to update stock when blood is removed from stock
DELIMITER $$
CREATE TRIGGER 461_stock_update2
AFTER INSERT
ON 461_RECEIVE FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
declare count int;
SET error_msg = ('Required amount of blood is not available');
IF (select `left` from 461_stock where blood_group = new.blood_group) < new.quantity_received THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
IF (select `left` from 461_stock where blood_group = new.blood_group) > new.quantity_received THEN
UPDATE 461_STOCK
SET `left` = `left` - new.quantity_received
WHERE blood_group= new.blood_group;
END IF;
END $$
DELIMITER ;

-- --------------------------------------------------------
-- CURSOR --
DELIMITER $$
CREATE PROCEDURE 461_donation_cnt(IN pid char(5), OUT count int)
BEGIN
DECLARE done INT DEFAULT FALSE;
DECLARE cur1 CURSOR FOR SELECT count(*) FROM 461_DONATION where 461_DONATION.pid=pid;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
OPEN cur1;
read_loop: LOOP
FETCH cur1 INTO count;
IF done THEN
LEAVE read_loop;
END IF;
END LOOP;
CLOSE cur1;
END $$
DELIMITER ;

CALL 461_donation_count('P_32',@A);
SELECT @A;

-- --------------------------------------------------------
