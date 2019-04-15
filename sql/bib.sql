SELECT
*
-- count(*)  --total OCLC numbers = 1,530,387
-- DISTINCT(p.index_entry) --should only be OCLC numbers
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


-- sierra_view.item_record AS i 

WHERE
p.index_tag = 'o' 
AND 
p.varfield_type_code IS DISTINCT FROM 'y' -- excludes 24k
AND 
r.deletion_date_gmt IS NULL 
AND
r.campus_code = '' -- excludes virtual metadata
AND 
r.creation_date_gmt IS NOT NULL  --excludes deleted records
AND
b.bcode2 != '@' --exclude eresources


-- i.location_code != 'kngle'
-- i.item_status_code != -- in copy cat (23 or n) ?!
-- AND i.location_code IN ('kngl','kng') -- over-limits
-- r.record_type_code = 'i'

-- for production monthly
-- AND r.record_last_updated_gmt::date > '2019-03-01'


LIMIT 100

