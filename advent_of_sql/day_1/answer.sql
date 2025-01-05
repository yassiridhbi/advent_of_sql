select
    c.name as name,
    w.wishes ->> '$.first_choice' as primary_wish,
    w.wishes ->> '$.second_choice' as backup_wish,
    w.wishes ->> '$.colors[0]' as favorite_color,
json_array_length(w.wishes.colors) as color_count,
    case
        when t.difficulty_to_make = 1 then 'Simple Gift'
        when t.difficulty_to_make = 2 then 'Moderate Gift'
        when t.difficulty_to_make >= 3 then 'Complex Gift'
    end as gift_complexity,
    case
        t.category
        when 'outdoor' then 'Outside Workshop'
        when 'educational' then 'Learning Workshop'
        else 'General Workshop'
    end as workshop_category
from
    wish_lists w
    join children c on w.child_id = c.child_id
    join toy_catalogue t on w.wishes ->> '$.first_choice' = t.toy_name
order by
    c.name asc
limit
    5;