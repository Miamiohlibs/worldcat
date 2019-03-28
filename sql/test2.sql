--to find all oclc numbers for items updated in the last month
--need to remove duplicates using distinct or nested query that doesn't
--take so long (distinct is slow)
SELECT
*
--DISTINCT (p.index_entry)
FROM
sierra_view.bib_record_item_record_link AS l
JOIN
sierra_view.phrase_entry AS p
ON
p.record_id = l.bib_record_id

JOIN
sierra_view.record_metadata AS r
ON
r.id = l.bib_record_id

LEFT OUTER JOIN
sierra_view.item_record AS i
ON
i.id = l.item_record_id


WHERE
p.index_tag = 'o'
AND
r.campus_code = ''
AND
r.creation_date_gmt IS NOT NUll
AND
(i.location_code != 'kngle'
AND
i.location_code LIKE 'kng%') --starts with
AND
r.record_last_updated_gmt::date > '2019-03-01'
AND
p.varfield_type_code IS DISTINCT FROM 'y'
AND
r.deletion_date_gmt IS NULL 
AND
r.campus_code = ''
AND 
r.creation_date_gmt IS NOT NULL

--AND i.item_status_code != --
LIMIT 10