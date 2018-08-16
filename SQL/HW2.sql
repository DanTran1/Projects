CREATE TABLE users
(
    user_id NUMBER PRIMARY KEY,
    email_address VARCHAR2(254) NOT NULL UNIQUE,
    first_name VARCHAR2(10) NOT NULL,
    last_name VARCHAR2(10) NOT NULL
);

CREATE TABLE product
(
    product_id NUMBER PRIMARY KEY,
    product_name VARCHAR2(254) NOT NULL
);

CREATE TABLE downloads
(
    download_id NUMBER PRIMARY KEY,
    user_id NUMBER REFERENCES users(user_id),
    download_date DATE DEFAULT SYSDATE,
    filename VARCHAR2(254) NOT NULL,
    product_id NUMBER REFERENCES product(product_id)
);

CREATE SEQUENCE user_id_seq; 
CREATE SEQUENCE product_id_seq;
CREATE SEQUENCE download_id_seq;

CREATE INDEX user_id_ix
    ON downloads (user_id);
    
CREATE INDEX product_id_ix
    ON downloads (product_id);
    
INSERT INTO users
VALUES (user_id_seq.NEXTVAL,'johnsmith@gmail','John','Smith');

INSERT INTO users
VALUES (user_id_seq.NEXTVAL,'janedoe@yahoo.com','Jane','Doe');

INSERT INTO product
VALUES (product_id_seq.NEXTVAL,'Local Music Vol 1');

INSERT INTO product
VALUES (product_id_seq.NEXTVAL,'Local Music Vol 2');

INSERT INTO downloads
VALUES (download_id_seq.NEXTVAL, 
       (SELECT user_id FROM users WHERE email_address = 'johnsmith@gmail'),
        SYSDATE,
        'pedals_are_falling.mp3',
       (SELECT product_id
        FROM product
        WHERE product_name = 'Local Music Vol 1'));

INSERT INTO downloads
VALUES (download_id_seq.NEXTVAL, 
       (SELECT user_id FROM users WHERE email_address = 'janedoe@yahoo.com'),
        SYSDATE,
        'turn_signal.mp3',
       (SELECT product_id
        FROM product
        WHERE product_name = 'Local Music Vol 1'));

INSERT INTO downloads
VALUES (download_id_seq.NEXTVAL, 
       (SELECT user_id FROM users WHERE email_address = 'janedoe@yahoo.com'),
        SYSDATE,
        'one_horse_town.mp3',
       (SELECT product_id
        FROM product
        WHERE product_name = 'Local Music Vol 2'));

ALTER TABLE product
ADD product_price DECIMAL(3,2) DEFAULT 9.99 NOT NULL;

ALTER TABLE product
ADD product_added_date DATE;

ALTER TABLE users
MODIFY first_name VARCHAR2(20);

INSERT INTO users
VALUES (user_id_seq.NEXTVAL,'tran.tamdanv@utexas.edu','ThisIsNotMyFirstName','Tran');

