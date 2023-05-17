CREATE OR REPLACE FUNCTION move_data_to_archive()
  RETURNS VOID AS
$$
DECLARE
  archive_table_name TEXT;
BEGIN
  archive_table_name := 'notifications_notification_archive_' || to_char(NOW(), 'YYYYMMDDHH24MISS');

  EXECUTE format('CREATE TABLE %I (LIKE notifications_notification INCLUDING CONSTRAINTS)', archive_table_name);

  EXECUTE format('INSERT INTO %I SELECT * FROM notifications_notification WHERE created_date < NOW() - INTERVAL ''6 months''', archive_table_name);

  DELETE FROM notifications_notification WHERE created_date < NOW() - INTERVAL '6 months';

  RAISE NOTICE 'Data moved to archive table: %', archive_table_name;
END;
$$
LANGUAGE plpgsql;



select cron.schedule('0 2 * * *',$$ SELECT move_data_to_archive()$$)