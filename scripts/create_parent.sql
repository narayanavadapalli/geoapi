-- This is for partition table for satellite data

CREATE TABLE geospatial_data (
    identifier BIGSERIAL,
    boundary geography(POLYGON,4267),
    date_of_pass date not null,
    satellite varchar(20) not null,
    sensor varchar(20) not null,
    metadata jsonb,
    CONSTRAINT geospatial_data_pkey  PRIMARY KEY (identifier,satellite,date_of_pass)
    ) partition by list(satellite);

create table geospatial_data_c2e partition of geospatial_data for values in ('CARTOSAT-2E') partition by range(date_of_pass);

create table geospatial_data_c2e_2022_01 partition of geospatial_data_c2e for values from ('2022-01-01') TO ('2022-01-31');