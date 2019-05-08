SELECT 
DISTINCT(p.index_entry)

FROM
sierra_view.phrase_entry AS p
JOIN
sierra_view.record_metadata AS r
ON
p.record_id = r.id
JOIN
sierra_view.bib_record AS b
ON
b.record_id = r.id
JOIN
sierra_view.bib_record_location AS l
ON
l.bib_record_id = b.record_id

WHERE
p.index_tag = 'o' 
AND 
p.varfield_type_code IS DISTINCT FROM 'y' 
AND 
r.deletion_date_gmt IS NULL 
AND
r.campus_code = '' 
AND 
r.creation_date_gmt IS NOT NULL 
AND
b.bcode2 != '@' 
AND
b.bcode1 = 'm' 
AND
l.location_code != 'onl'
AND
b.is_suppressed = 'f'
AND
l.location_code 
IN 
('kngl', 
'imc', 
'aal',
'spe',
'mic',
'scl',
'mul',
'ref',
'doc')


