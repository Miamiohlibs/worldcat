SELECT
*
FROM
sierra_view.item_record AS i
JOIN
sierra_view.bib_record_item_record_link AS l
ON
i.id = l.item_record_id


JOIN
sierra_view.record_metadata AS r
ON 
r.id = i.id


JOIN
sierra_view.phrase_entry AS p
p.record_id = l.bib_record_id

LIMIT 100