SELECT
*
FROM
--sierra_view.phrase_entry AS p
sierra_view.record_metadata AS r
-- JOIN
-- sierra_view.record_metadata AS r
-- ON
-- r.id = p.record_id

WHERE
-- p.index_tag = 'o' 
-- AND 
-- p.varfield_type_code IS DISTINCT FROM 'y' 

AND r.record_type_code = 'i' 
AND r.deletion_date_gmt IS NULL 
AND r.campus_code = ''
AND r.creation_date_gmt IS NOT NULL
--AND i.location_code != 'kngle'
--AND i.item_status_code != --
--AND i.location_code IN ('kngl','kng')
AND r.record_last_updated_gmt::date > '2019-03-01'


LIMIT 100
--total OCLC numbers = 2,286,415
