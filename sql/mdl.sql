SELECT 
-- *
-- count(*)  --total OCLC numbers = 1,387,592
-- count(DISTINCT(p.index_entry)) --should only be OCLC numbers
DISTINCT(p.index_entry)

-- for the greenglass project prep
-- DISTINCT(r.record_type_code || r.record_num || 'a') AS bib_rec
-- count(DISTINCT(r.record_type_code || r.record_num || 'a')) AS bib_rec

-- DISTINCT(l.location_code)  --unique list of location codes
-- l.location_code

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


-- sierra_view.item_record AS i 

WHERE
p.index_tag = 'o' --excludes anything that isn't an oclc number in theory
AND 
p.varfield_type_code IS DISTINCT FROM 'y' -- excludes 24k
AND 
r.deletion_date_gmt IS NULL --excludes deleted records
AND
r.campus_code = '' -- excludes virtual metadata from Ohiolink
AND 
r.creation_date_gmt IS NOT NULL  --excludes deleted records
AND
b.bcode2 != '@' --exclude eresources
AND
b.bcode1 = 'm' --exclude serials
AND
l.location_code != 'onl' -- excludes more eresources
AND
b.is_suppressed = 'f'
AND
l.location_code  = 'mdl'
-- IN 
-- ('kngl', --KING MAIN
-- 'imc', --YOU KNOW
-- 'aal', --ART/ARCH
-- 'spe', --SPEC
-- 'mic', --SPEC
-- 'scl', --BEST
-- 'mul', --MUSIC
-- 'ref', --KING REF
-- 
-- 
-- --locations to exclude in production
-- 	'doc') --,'mdl','hal','swdep', 'multi'


-- for production monthly
-- AND r.record_last_updated_gmt::date > '2019-03-01'


-- LIMIT 100
-- ORDER BY bib_rec DESC
