CREATE OR REPLACE FUNCTION select_count_pok_by_service(int4, date) returns setof accounts AS $$
begin
	RETURN QUERY
	select meter_pok.tarif, service, accounts.number, meter_pok.row_id
	from accounts
	inner join counters  on accounts.row_id = counters.row_id 
    inner join meter_pok on meter_pok.row_id = counters.row_id 
	where service = $1 and meter_pok."date" = $2;
end;
$$ language plpgsql


select select_count_pok_by_service('300', '20230227')

select meter_pok.tarif, service, number, "date" 
from accounts  
inner join counters  on accounts.row_id = counters.row_id 
inner join meter_pok on meter_pok.row_id = counters.row_id 
where service  = '300' and "date" = '20230227'

--______________________________________________________________
--Написать функцию select_value_by_house_and_month. Она получает номер дома и месяц
--и возвращает все лицевые в этом доме , для лицевых выводятся все счетчики с сумарным расходом за месяц ( суммирую все показания тарифов)
--Результатом вызова
--функции должна быть таблица с 3 колонками:
--
--- acc (Лицевой счет)
--- name (Наименование счетчика)
--- value (Расход)

CREATE OR REPLACE function select_value_by_house_and_month(int4, date) returns setof accounts AS $$
begin
	RETURN QUERY
	select accounts."number", value, "month" , counters."name" 
	from accounts
	inner join counters  on accounts.row_id = counters.row_id 
    inner join meter_pok on meter_pok.row_id = counters.row_id 
	where accounts."type" = $1 and meter_pok."month" = $2;
end;
$$ language plpgsql

select select_value_by_house_and_month('1', '20230101')

select accounts."number", value, "month", counters."name" 
from accounts  
inner join counters  on accounts.row_id = counters.row_id 
inner join meter_pok on meter_pok.row_id = counters.row_id 
where accounts."type" = 1 and "month" = '20230101'


--аписать функцию stack.select_last_pok_by_acc. Она получает номер лицевого
--и возвращает дату,тариф,объем последнего показания по каждой услуге
--Результатом вызова
--функции должна быть таблица с 5 колонками:
--- acc (Лицевой счет)
--- serv (Услуга)
--- date (Дата показания)
--- tarif (Тариф показания)
--- value (Объем)
select accounts."number", "date" , meter_pok.tarif, value , service
from accounts  
inner join counters  on accounts.row_id = counters.row_id 
inner join meter_pok on meter_pok.row_id = counters.row_id 
where accounts."number" = 1
