--to count the items attached to bib records whose bib location is multi, looking for one or fewer items

SELECT 
m.record_type_code || m.record_num || 'a' AS bib_rec,
count(*) as count

FROM
sierra_view.bib_record AS b
JOIN
sierra_view.bib_record_item_record_link AS l
ON
l.bib_record_id = b.record_id
JOIN
sierra_view.bib_record_location AS loc
ON
loc.bib_record_id = b.record_id
JOIN 
sierra_view.record_metadata AS m
ON
m.id = b.record_id

WHERE
b.bcode2 != '@' --exclude eresources
AND
b.bcode1 = 'm' --exclude serials
AND
loc.location_code  = 'multi'
AND
loc.location_code  != 'onl'

GROUP BY bib_rec
ORDER BY count DESC
