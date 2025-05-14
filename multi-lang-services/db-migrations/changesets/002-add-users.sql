--liquibase formatted sql
--changeset author:002-add-users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL
);

