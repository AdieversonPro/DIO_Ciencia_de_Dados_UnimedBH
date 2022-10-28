# Desafio <img src="https://hermes.digitalinnovation.one/assets/diome/logo.svg" width="100" height="50"> de Projeto - Análise de dados com Python e Pandas

#### DESCRIÇÃO DO DESAFIO

* Neste Labs será apresentada a biblioteca Pandas, uma biblioteca Python de código aberto para análise de dados. Ela dá ao Python a capacidade de trabalhar com dados do tipo planilha;
* Permitindo carregar;
* Manipular 
* Combinar dados rapidamente, entre outras funções.

Neste desafio foi utilizado um dataset publico que foi encontrado no site: https://archive.ics.uci.edu/ml/index.php, site este que contém vários datasets para estudos, conhecido também como **MACHINE LEARNING REPOSITORY**, pois os datasets são para testes em machine learning, foi escolhido um dataset que traz informações de câncer de cervical.

<center><strong><span style="font-size:32px">FERRRAMENTAS UTILIZADAS</span></strong></center>

<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="100" height="150">  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" width="150" height="150">        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png" width="100" height="150">  <img src="https://matplotlib.org/stable/_static/images/logo2.svg" width="150" height="150"></p> 

- Python como linguagem base de analise de dados
- Biblioteca Pandas para auxiliar na utilização de dados;
- Biblioteca matplotlib para visualização de dados;
- Jupyter Notebook para criação de scripts em python.



###### <span style="font-size:14px; color: green">INFORMAÇÕES DO DATASET</span>

1. Informações coletadas do Hospital Universitário de Caracas, da cidade de Caracas na Venezuela;
2. Contém informações de 858 pacientes do hospital;
   1. Hábitos e Registros médicos.
3. São 858 linhas e 36 Colunas;
4. Contém Valores Nulos;
5. Criadores;
   1. Kelwin Fernandes - INESC TEC & FEUP, Porto, Portugal;
   2. Jaime S. Cardoso - INESC TEC & FEUP, Porto, Portugal;
   3. Jessica fernandes - Universidad Central de Venezuela, Caracas, Venezuela.

###### <span style="font-size:14px; color: green">COLUNAS DO DATASET </span>

| Nome CSV                            | Tipo CSV | Nome Alterado                   | Tipo Alterado |
| :---------------------------------- | :------: | ------------------------------- | ------------- |
| Age                                 |   int    | IDADE                           | int           |
| Number of sexual partners           |   int    | QTD_PARC_SEXUAIS                | int           |
| First sexual intercourse age        |   int    | IDADE_1_ATO_SEXUAL              | int           |
| Num of pregnancies                  |   int    | QTD_GRAVIDEZ                    | int           |
| Smokes                              |   bool   | FUMA?                           | bool          |
| Smokes years                        |   bool   | TEMPO_FUMA(ANOS)                | int           |
| Smokes packs/year                   |   bool   | PCT_CIGARRO_ANO                 | float         |
| Hormonal Contraceptives             |   bool   | ANTI_CONCEPCIONAL               | bool          |
| Hormonal Contraceptives years       |   int    | ANTI_CONCEPCIONAL_ANOS          | int           |
| IUD                                 |   bool   | DIU                             | bool          |
| IUD years                           |   int    | DIU_ANOS                        | int           |
| STDs                                |   bool   | DSTs                            | bool          |
| STD snumber                         |   int    | QTD_DSTs                        | int           |
| STDs: condylomatosis                |   bool   | condilomatose                   | bool          |
| STDs: cervical condylomatosis       |   bool   | cervical_condilomatose          | bool          |
| STDs: vaginal condylomatosis        |   bool   | condilomatose_vaginal           | bool          |
| STDs: vulvo-perineal condylomatosis |   bool   | vulvoperineal_condilomatose     | bool          |
| STDs: syphilis                      |   bool   | sífilis                         | bool          |
| STDs: pelvic inflammatory disease   |   bool   | doença_inflamatória_pélvica     | bool          |
| STDs: genital herpes                |   bool   | herpes_genital                  | bool          |
| STDs: molluscum contagiosum         |   bool   | molusco_contagioso              | bool          |
| STDs: AIDS                          |   bool   | AIDS                            | bool          |
| STDs: HIV                           |   bool   | HIV                             | bool          |
| STDs: Hepatitis B                   |   bool   | hepatite_b                      | bool          |
| STDs: HPV                           |   bool   | HPV                             | bool          |
| STDs: Number of diagnosis           |   int    | QTD_DIAGNOSTICOS                | int           |
| STDs: Time since first diagnosis    |   int    | TEMPO(ANOS)_DIAGNOSTICOS        | int           |
| STDs:Time since last diagnosis      |   int    | TEMPO(ANOS)_ULTIMO_DIAGNOSTICOS | int           |
| Dx: Cancer                          |   bool   | EXM_DX_CANCER                   | bool          |
| Dx: CIN                             |   bool   | EXM_DX_CIN                      | bool          |
| Dx: HPV                             |   bool   | EXM_DX_HPV                      | bool          |
| Dx                                  |   bool   | EXM_DX                          | bool          |
| Hinselmann: targetvariable          |   bool   | Hinselmann                      | bool          |
| Schiller: targetvariable            |   bool   | Schiller                        | bool          |
| Cytology: targetvariable            |   bool   | Citologia                       | bool          |

<p align="center">
    <img src="https://hermes.digitalinnovation.one/tracks/342f7392-a8b5-421f-bea9-d29f1fd8aae9.png" height="200"></p>