SELECT * FROM sensores;

-- =========================================
-- ANALISES DOS DADOS DOS SENSORES
-- =========================================

-- Total de registros
SELECT COUNT(*) AS total_registros
FROM sensores;

-- Média da umidade quando irrigou
SELECT ROUND(AVG(umidade / 100), 2) AS media_umidade
FROM sensores
WHERE status = 'LIGADA';

-- Menor umidade registrada
SELECT ROUND(MIN(umidade / 100), 2) AS minimo_umidade
FROM sensores;

-- Maior umidade registrada
SELECT ROUND(MAX(umidade / 100), 2) AS maximo_umidade
FROM sensores;

-- Média do pH quando irrigou
SELECT ROUND(AVG(ph / 100), 2) AS media_ph
FROM sensores
WHERE status = 'LIGADA';

-- Menor pH registrado
SELECT ROUND(MIN(ph / 100), 2) AS minimo_ph
FROM sensores;

-- Maior pH registrado
SELECT ROUND(MAX(ph / 100), 2) AS maximo_ph
FROM sensores;

-- Total de vezes que a bomba ligou
SELECT COUNT(*) AS total_ligada
FROM sensores
WHERE status = 'LIGADA';

-- Total de vezes que a bomba desligou
SELECT COUNT(*) AS total_desligada
FROM sensores
WHERE status = 'DESLIGADA';

-- Comparativo entre ligada e desligada
SELECT status,
       COUNT(*) AS total
FROM sensores
GROUP BY status;

-- Motivos mais frequentes
SELECT motivo,
       COUNT(*) AS quantidade
FROM sensores
GROUP BY motivo
ORDER BY quantidade DESC;

-- Registros com irrigação ligada
SELECT *
FROM sensores
WHERE status = 'LIGADA';

-- Registros com irrigação desligada
SELECT *
FROM sensores
WHERE status = 'DESLIGADA';

-- Registros com pH fora do ideal
SELECT *
FROM sensores
WHERE motivo = 'pH fora ideal';

-- Registros com solo molhado
SELECT *
FROM sensores
WHERE motivo = 'Solo molhado';

-- Registros com falta de adubo
SELECT *
FROM sensores
WHERE motivo = 'Falta adubo';

-- Média de umidade e pH por status
SELECT status,
       ROUND(AVG(umidade / 100), 2) AS media_umidade,
       ROUND(AVG(ph / 100), 2) AS media_ph
FROM sensores
GROUP BY status;

-- Porcentagem de vezes que irrigou
SELECT 
ROUND(
    (COUNT(CASE WHEN status = 'LIGADA' THEN 1 END) * 100.0)
    / COUNT(*),
2) AS porcentagem_ligada
FROM sensores;

-- Porcentagem de vezes desligada
SELECT 
ROUND(
    (COUNT(CASE WHEN status = 'DESLIGADA' THEN 1 END) * 100.0)
    / COUNT(*),
2) AS porcentagem_desligada
FROM sensores;

-- Média da umidade por motivo
SELECT motivo,
       ROUND(AVG(umidade / 100), 2) AS media_umidade
FROM sensores
GROUP BY motivo;

-- Média do pH por motivo
SELECT motivo,
       ROUND(AVG(ph / 100), 2) AS media_ph
FROM sensores
GROUP BY motivo;

-- Condições ideais de irrigação
SELECT *
FROM sensores
WHERE status = 'LIGADA'
AND (ph / 100) BETWEEN 5.5 AND 7.5
AND (umidade / 100) < 55;