--liquibase formatted sql
--changeset author:001-init
CREATE TABLE example (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

