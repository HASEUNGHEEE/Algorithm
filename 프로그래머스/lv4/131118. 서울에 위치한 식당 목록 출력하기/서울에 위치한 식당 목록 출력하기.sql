-- 코드를 입력하세요
SELECT i.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, round(avg(REVIEW_SCORE),2) as SCORE
FROM REST_INFO i, REST_REVIEW r 
WHERE i.REST_ID = r.REST_ID AND i.ADDRESS LIKE "서울%"
GROUP BY i.REST_ID
ORDER BY SCORE DESC, i.FAVORITES DESC;