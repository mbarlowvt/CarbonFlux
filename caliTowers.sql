-- Simple query from the tower data table to determine towers located in California (loose box around the borders)
SELECT *
FROM "TOWER_DATA"."Ameriflux_tower_list"
WHERE "Latitude" BETWEEN 32.39851580247402 AND 42.22851735620852
    AND "Longitude" BETWEEN -124.93652343749999 AND -113.9501953125;