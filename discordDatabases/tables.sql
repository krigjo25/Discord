CREATE OR REPLACE TABLE welcome (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                welcome VARCHAR(255) NOT NULL,

CREATE OR REPLACE TABLE abcent (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                abcent VARCHAR(255) NOT NULL,



CREATE OR REPLACE TABLE  afkMessages (
                                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                        memberName VARCHAR(255) NOT NULL,
                                        afkReason VARCHAR(255));