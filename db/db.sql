CREATE SCHEMA apibigdata DEFAULT CHARACTER SET utf8;

USE apibigdata;

CREATE TABLE tweets (
	id int(10) auto_increment,
    id_tweet varchar(40),
    text_tweet text,
    created_date date,
    favorites varchar(100),
    retweets int(20),
    classification varchar(3),
    PRIMARY KEY (id)
);