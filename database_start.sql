-- *************** SqlDBM: PostgreSQL ****************;
-- ***************************************************;

CREATE DATABASE "desafio-4i";

-- ************************************** "user"

CREATE TABLE "user"
(
 "id"              serial NOT NULL,
 cpf             varchar(11) NOT NULL,
 hashed_password text NOT NULL,
 full_name       varchar(200) NOT NULL,
 birthday        date NULL,
 cep             varchar(8) NULL,
 street          varchar(200) NULL,
 neighborhood    varchar(200) NULL,
 city            varchar(200) NULL,
 "state"           varchar(50) NULL,
 CONSTRAINT PK_user PRIMARY KEY ( "id" )
);







