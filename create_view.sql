CREATE OR REPLACE VIEW v_studenti_kurzy AS
SELECT
    s.student_id,
    s.jmeno,
    s.prijmeni,
    k.nazev AS kurz
FROM
    student s
    JOIN student_kurz sk ON s.student_id = sk.student_id
    JOIN kurz k ON sk.kurz_id = k.kurz_id;
