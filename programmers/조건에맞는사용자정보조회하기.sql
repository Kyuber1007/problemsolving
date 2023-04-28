-- 코드를 입력하세요
select user_id, nickname,concat(city, ' ', street_address1, ' ', street_address2) as address, concat(substr(tlno, 1, 3), '-', substr(tlno, 4, 4), '-', substr(tlno, 8, 4)) as tlno
from (SELECT user.user_id as id, count(*) as count
    from used_goods_board as board, used_goods_user as user
    where board.writer_id = user.user_id
    group by user.user_id) as T, used_goods_user as U
where T.count >= 3 and T.id = U.user_id
order by user_id desc
