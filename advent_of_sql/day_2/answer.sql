with full_letter as (
    select
        *
    from
        letters_a
    union
    all
    select
        *
    from
        letters_b
),
filtered_letter as (
    select
        chr(value) as chars
    from
        full_letter
    where
        chr(value) ~ '^[A-Za-z !"''(),\-.:;?]$'
    order by
        id
)
select
    string_agg(chars, '')
from
    filtered_letter;