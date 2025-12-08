SELECT
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    COUNT(br.record_id) AS current_borrowers  -- Changed from COUNT(*)
FROM
    library_books lb
    LEFT JOIN borrowing_records br
        ON lb.book_id = br.book_id
        AND br.return_date IS NULL  -- MOVED HERE into the JOIN condition
GROUP BY
    lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, lb.total_copies
HAVING
    COUNT(br.record_id) = lb.total_copies  -- Changed from COUNT(*)
ORDER BY
    current_borrowers DESC,
    lb.title ASC;