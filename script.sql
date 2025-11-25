-- Active: 1710242554065@@127.0.0.1@5432@p2_video_game_sales
CREATE DATABASE p2_video_game_sales


DROP TABLE IF EXISTS dim_tempo;
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

drop table dim_editora;
CREATE TABLE dim_editora (
    editora_key INTEGER PRIMARY KEY,
    editora VARCHAR(100)
);


DROP TABLE IF EXISTS dim_jogo;
CREATE TABLE dim_jogo (
    jogo_key INTEGER PRIMARY KEY,
    nome VARCHAR(255),
    rank INTEGER
);

DROP TABLE IF EXISTS fato_vendas;

CREATE TABLE fato_vendas(
    venda_key SERIAL PRIMARY KEY,
    jogo_key INTEGER REFERENCES dim_jogo(jogo_key),
    ano_key INTEGER REFERENCES dim_tempo(data_key),
    plataforma_key INTEGER REFERENCES dim_plataforma(plataforma_key),
    genero_key INTEGER REFERENCES dim_genero(genero_key),
    editora_key INTEGER REFERENCES dim_editora(editora_key),
    vendas_na NUMERIC(10,2),
    vendas_eu NUMERIC(10,2),
    vendas_jp NUMERIC(10,2),
    vendas_outras NUMERIC(10,2),
    vendas_global NUMERIC(10,2)
);

SELECT * FROM dim_jogo;
