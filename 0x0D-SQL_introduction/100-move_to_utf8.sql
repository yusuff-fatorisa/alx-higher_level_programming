-- This script contains some SQL commands that converts 'hbtn_0c_0'
-- database to 'UTF*' in the MySQL server

ALTER database hbtn_0c_0 CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci
