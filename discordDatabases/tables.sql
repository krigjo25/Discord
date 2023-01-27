CREATE OR REPLACE TABLE welcome (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                welcome VARCHAR(255) NOT NULL);

CREATE OR REPLACE TABLE abcent (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                abcent VARCHAR(255) NOT NULL);


CREATE OR REPLACE TABLE  afkMessages (
                                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                        memberName VARCHAR(255) NOT NULL,
                                        afkReason VARCHAR(255));

#   Jumble Game
CREATE OR REPLACE TABLE categories (
                                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                        categories VARCHAR(255) NOT NULL,
                                        sub VARCHAR(255),
                                        sub1 VARCHAR(255),
                                        sub2 VARCHAR(255),
                                        sub3 VARCHAR(255),
                                        sub4 VARCHAR(255),
                                        sub5 VARCHAR(255),
                                        sub6 VARCHAR(255),
                                        sub7 VARCHAR(255),
                                        sub8 VARCHAR(255),
                                        sub9 VARCHAR(255),
                                        sub10 VARCHAR(255));
CREATE OR REPLACE TABLE waltdisney (
                                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                        characters VARCHAR(255) NOT NULL,
                                        roles VARCHAR(255) NOT NULL,
                                        animationname VARCHAR(255) NOT NULL);