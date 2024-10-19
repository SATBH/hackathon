drop schema public cascade;
create schema public;

CREATE TABLE paciente (id serial primary key , correo varchar(255) unique, nombre varchar(255), hash_clave varchar(255), fecha_nacimiento date, numero_telefono char(8), peso integer, fecha_registro date);
CREATE TABLE doctor (id serial primary key, correo varchar(255) unique, nombre varchar(255), hash_clave varchar(255), numero_telefono char(8));
CREATE TABLE variables_medicion (id serial primary key, nombre varchar(20));
CREATE TABLE especialidades_doctores (id serial primary key,nombre varchar(20));

CREATE TABLE puente_paciente_doctor(id_doctor integer, id_paciente integer);
CREATE TABLE puente_doctor_especialidad(id_doctor integer, id_especialidad integer);
CREATE TABLE medicion (id_variable integer, valor real);
CREATE TABLE rangos_aceptables(id_variable integer, valor_minimo real, valor_maximo real, id_paciente integer, id_doctor integer, primary key (id_paciente, id_doctor, id_variable));


ALTER TABLE puente_paciente_doctor ADD CONSTRAINT fk_puente_paciente_doctor_doctor FOREIGN KEY (id_doctor) REFERENCES doctor (id);
ALTER TABLE puente_paciente_doctor ADD CONSTRAINT fk_puente_paciente_doctor_paciente FOREIGN KEY (id_paciente) REFERENCES paciente (id);
ALTER TABLE puente_doctor_especialidad ADD CONSTRAINT fk_puente_doctor_especialidad_doctor FOREIGN KEY (id_doctor) REFERENCES doctor (id);
ALTER TABLE puente_doctor_especialidad ADD CONSTRAINT fk_puente_doctor_especialidad_especialidad FOREIGN KEY (id_especialidad) REFERENCES especialidades_doctores (id);
ALTER TABLE medicion ADD CONSTRAINT fk_medicion FOREIGN KEY (id_variable) REFERENCES variables_medicion (id);
ALTER TABLE rangos_aceptables ADD CONSTRAINT fk_rangos_doctor FOREIGN KEY (id_doctor) REFERENCES doctor (id);
ALTER TABLE rangos_aceptables ADD CONSTRAINT fk_rangos_paciente FOREIGN KEY (id_paciente) REFERENCES paciente (id);
ALTER TABLE rangos_aceptables ADD CONSTRAINT fk_rangos_variable FOREIGN KEY (id_variable) REFERENCES variables_medicion (id);

