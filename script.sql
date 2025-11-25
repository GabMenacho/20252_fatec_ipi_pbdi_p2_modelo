CREATE DATABASE p2_video_game_sales

CREATE TABLE dim_tempo (
    data_key INTEGER PRIMARY KEY,
    ano INTEGER
);
 
CREATE TABLE dim_plataforma (
    plataforma_key INTEGER PRIMARY KEY,
    nome VARCHAR(50)
);
 
CREATE TABLE dim_genero (
    genero_key INTEGER PRIMARY KEY,
    genero VARCHAR(50)
);
 
CREATE TABLE dim_editora (
    editora_key INTEGER PRIMARY KEY,
    edtora VARCHAR(100)
);
 
CREATE TABLE dim_jogo (
    jogo_key INTEGER PRIMARY KEY,
    nome VARCHAR(255),
    rank INTEGER
);



