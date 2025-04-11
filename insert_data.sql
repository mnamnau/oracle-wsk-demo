-- Vložení testovacích dat
INSERT INTO student (jmeno, prijmeni) VALUES ('Anna', 'Nováková');
INSERT INTO student (jmeno, prijmeni) VALUES ('Petr', 'Svoboda');

INSERT INTO kurz (nazev) VALUES ('Databáze');
INSERT INTO kurz (nazev) VALUES ('Statistika');

INSERT INTO student_kurz (student_id, kurz_id) VALUES (1, 1);
INSERT INTO student_kurz (student_id, kurz_id) VALUES (1, 2);
INSERT INTO student_kurz (student_id, kurz_id) VALUES (2, 1);
INSERT INTO student (jmeno, prijmeni) VALUES ('Honza', 'Dvořák');

COMMIT;