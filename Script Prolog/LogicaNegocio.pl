%%% =======================================================================
%%% Hechos de las personas. En todos los casos Y es el C.I. (Identificador)
%%% =======================================================================
cliente('3828622').
empleado('3485730').

% Hecho: es_nombre_de(X, Y) X es el nombre de Y
es_nombre_de('Francisco', '3828622').
es_nombre_de('Tamara', '3485730').

% Hecho: es_apellido_de(X, Y) X es el apellido de Y
es_apellido_de('Recalde', '3828622').
es_apellido_de('Ocampos', '3485730').

% Hecho: es_direccion_de(X, Y) X es el direccion de Y
es_direccion_de('Villa Elisa', '3828622').
es_direccion_de('Fdo. de la Mora', '3485730').

% Hecho: es_celular_de(X, Y) X es el celular de Y
es_celular_de('0983 111111', '3828622').
es_celular_de('0983 222222', '3485730').

% Hecho: es_email_de(X, Y) X es el email de Y
es_email_de('pepito@gmail.com', '3828622').
es_email_de('pepito@gmail.com', '3485730').

% Hecho: es_red_social_de(X, Y) X es el telefono de Y
es_red_social_de('021 576576', '3828622').
es_red_social_de('021 576576', '3485730').

%%%% Hechos de los clientes. En todos los casos Y es el C.I. (Identificador)

% Hecho: es_ruc_de(X, Y) X es el Ruc de Y
es_ruc_de('99999-9', '3828622').

%%%% Hechos de los empleados. En todos los casos Y es el C.I. (Identificador)

% Hecho: es_salario_de(X, Y) X es sueldo de Y
es_salario_de('1900000', '3485730').

%%% ==========================================================================
%%% ===============================REGLAS=====================================
%%% ==========================================================================

%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del cliente con Cedula, los datos:
%%% nombre, apellido, direccion, celular, email, red social y ruc

son_datos_de_cliente(Cedula, Nombre, Apellido, Direccion, Cel, Tel, Mail, Ruc) :-
	es_nombre_de(Nombre, Cedula), es_apellido_de(Apellido, Cedula),
	es_direccion_de(Direccion, Cedula), es_celular_de(Cel, Cedula),
	es_red_social_de(Tel, Cedula), es_email_de(Mail, Cedula), 
	es_ruc_de(Ruc, Cedula).


%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del empleado con Cedula, los datos:
%%% nombre, apellido, direccion, celular, email, red social  y sueldo

son_datos_de_empleado(Cedula, Nombre, Apellido, Direccion, Cel, Tel, Mail, Tec, Sueldo) :-
	es_nombre_de(Nombre, Cedula), es_apellido_de(Apellido, Cedula),
	es_direccion_de(Direccion, Cedula), es_celular_de(Cel, Cedula),
	es_red_social_de(Tel, Cedula), es_email_de(Mail, Cedula), 
	es_salario_de(Sueldo, Cedula).

%%% ----------------------------------------------------------------------------
%%% ----------------------------------------------------------------------------
