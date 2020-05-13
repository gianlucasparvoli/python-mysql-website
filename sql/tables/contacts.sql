
DROP TABLE IF EXISTS contacts;


create table contacts (
    id INT NOT NULL AUTO_INCREMENT,
    fullname VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    Primary key (id)
);