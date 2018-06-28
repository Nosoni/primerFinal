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
es_email_de('algo@gmail.com', '3828622').
es_email_de('algo@gmail.com', '3485730').

% Hecho: es_red_social_de(X, Y) X es el telefono de Y
es_red_social_de('021 576576', '3828622').
es_red_social_de('021 576576', '3485730').

%%%% Hechos de los clientes. En todos los casos Y es el C.I. (Identificador)

% Hecho: es_ruc_de(X, Y) X es el Ruc de Y
es_ruc_de('111111111-1', '3828622').

%%%% Hechos de los empleados. En todos los casos Y es el C.I. (Identificador)

% Hecho: es_salario_de(X, Y) X es sueldo de Y
es_salario_de('1900000', '3485730').

%%% ==========================================================================
%%% Hechos de los repuestos. En todos los casos Y es el Codigo (Identificador)
%%% ==========================================================================

repuesto('0001').
repuesto('0002').

% Hecho: es_tipo_de_repuesto(X, Y) X es el tipo de Y
es_tipo_de_repuesto('disco', '0001').
es_tipo_de_repuesto('memoria', '0002').

% Hecho: es_marca_de_repuesto(X, Y) X es la marca de Y
es_marca_de_repuesto('Seagate', '0001').
es_marca_de_repuesto('Samsung', '0002').

% Hecho: es_modelo_de_repuesto(X, Y) X es el modelo de Y
es_modelo_de_repuesto('HK-50', '0001').
es_modelo_de_repuesto('DDR3', '0002').

% Hecho: es_costo_de_repuesto(X, Y) X es el costo de Y
es_costo_de_repuesto('500000', '0001').
es_costo_de_repuesto('250000', '0002').

%%%% Hechos de los discos. En todos los casos Y es el Codigo (Identificador)

% Hecho: es_capacidad_de_repuesto(X, Y) X es la capacidad de Y
es_capacidad_de_repuesto('1000', '0001').

%%%% Hechos de los memorias. En todos los casos Y es el Codigo (Identificador)

% Hecho: es_tamanho_de_repuesto(X, Y) X es la tamanho de Y
es_tamanho_de_repuesto('8', '0002').


%%% ==========================================================================
%%% Hechos de las solicitudes. En todos los casos Y es el Codigo (Identificador)
%%% ==========================================================================

solicitud('1').

% Hecho: es_fecha_de_solicitud(X, Y) X es el fecha de Y
es_fecha_de_solicitud('22/11/15', '1').

% Hecho: es_cliente_de_solicitud(X, Y) X es el cliente de Y
es_cliente_de_solicitud('3828622', '1').

% Hecho: es_empleado_de_solicitud(X, Y) X es el empleado de Y
es_empleado_de_solicitud('3485730', '1').

% Hecho: es_equipo_de_solicitud(X, Y) X es el equipo de Y
es_equipo_de_solicitud('321', '1').
es_equipo_de_solicitud('322', '1').


%%% ----------------------------------------------------------------------------
%%% Hechos de los equipos. En todos los casos Y es el Codigo (Identificador)
%%% Las solicitudes se componen de equipos que se crean en la propia solicitud
	
equipo('321').
equipo('322').

% Hecho: es_tipo_de_equipo(X, Y) X es el tipo de Y
es_tipo_de_equipo('notebook', '321').
es_tipo_de_equipo('impresora', '322').

% Hecho: es_marca_de_equipo(X, Y) X es el marca de Y
es_marca_de_equipo('Acer', '321').
es_marca_de_equipo('HP', '322').

% Hecho: es_modelo_de_equipo(X, Y) X es el modelo de Y
es_modelo_de_equipo('Aspire 15', '321').
es_modelo_de_equipo('Deskjet', '322').

% Hecho: es_detalle_de_equipo(X, Y) X es el detalle de Y
es_detalle_de_equipo('15 pulgadas, color negro', '321').
es_detalle_de_equipo('color blanco', '322').

% Hecho: es_problema_de_equipo(X, Y) X es el problema de Y
es_problema_de_equipo('No enciende', '321').
es_problema_de_equipo('No estira hojas', '322').

% Hecho: es_costo_de_equipo(X, Y) X es el costo de mantenimiento de Y
es_costo_de_equipo('180000', '321').
es_costo_de_equipo('150000', '322').

% Hecho: es_estado_de_equipo(X, Y) X es el estado de mantenimiento de Y
es_estado_de_equipo('pendiente', '321').
es_estado_de_equipo('pendiente', '322').

%%% ----------------------------------------------------------------------------
%%% Los repuestos se pueden agregar a los equipos

% Hecho: es_repuesto_de_equipo(X, Y) X es repuesto del equipo de Y
es_repuesto_de_equipo('0001', '321').
es_repuesto_de_equipo('0002', '321').


%%% ==========================================================================
%%% ===============================REGLAS=====================================
%%% ==========================================================================

%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del cliente con Cedula, los datos:
%%% nombre, apellido, direccion, celular, telefono, celular, email y ruc

son_datos_de_cliente(Cedula, Nombre, Apellido, Direccion, Cel, Tel, Mail, Ruc) :-
	es_nombre_de(Nombre, Cedula), es_apellido_de(Apellido, Cedula),
	es_direccion_de(Direccion, Cedula), es_celular_de(Cel, Cedula),
	es_red_social_de(Tel, Cedula), es_email_de(Mail, Cedula), es_ruc_de(Ruc, Cedula).


%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del empleado con Cedula, los datos:
%%% nombre, apellido, direccion, celular, telefono, celular, email, tecnico y sueldo

son_datos_de_empleado(Cedula, Nombre, Apellido, Direccion, Cel, Tel, Mail, Tec, Sueldo) :-
	es_nombre_de(Nombre, Cedula), es_apellido_de(Apellido, Cedula),
	es_direccion_de(Direccion, Cedula), es_celular_de(Cel, Cedula),
	es_red_social_de(Tel, Cedula), es_email_de(Mail, Cedula), 
	es_tecnico_de(Tec, Cedula), es_salario_de(Sueldo, Cedula).

	
%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del repuesto con Codigo, los datos:
%%% tipo, marca, modelo, costo y dato adicional (Solo para discos y memoria)

son_datos_de_repuesto(Codigo, Tipo, Marca, Modelo, Costo, Dato) :-
	Tipo = 'disco', !, es_tipo_de_repuesto(Tipo, Codigo), es_marca_de_repuesto(Marca, Codigo),
	es_modelo_de_repuesto(Modelo, Codigo), es_costo_de_repuesto(Costo, Codigo), 
	es_capacidad_de_repuesto(Dato, Codigo).
	
son_datos_de_repuesto(Codigo, Tipo, Marca, Modelo, Costo, Dato) :-
	Tipo = 'memoria', !, es_tipo_de_repuesto(Tipo, Codigo), es_marca_de_repuesto(Marca, Codigo),
	es_modelo_de_repuesto(Modelo, Codigo), es_costo_de_repuesto(Costo, Codigo), 
	es_tamanho_de_repuesto(Dato, Codigo).

%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos de la solicitud con Codigo, los datos:
%%% fecha, cliente, empleado, equipo

son_datos_de_solicitud(Codigo, Fecha, Cliente, Empleado, Equipo) :-
	es_fecha_de_solicitud(Fecha, Codigo), es_cliente_de_solicitud(Cliente, Codigo), 
	es_empleado_de_solicitud(Empleado, Codigo), es_equipo_de_solicitud(Equipo, Codigo).

%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos de la equipo con Codigo, los datos:
%%% tipo, marca, modelo, detalle, problema, costo y estado

son_datos_de_equipo(Codigo, Tipo, Marca, Modelo, Detalle, Problema, Costo, Estado) :-
	es_tipo_de_equipo(Tipo, Codigo), es_marca_de_equipo(Marca, Codigo), 
	es_modelo_de_equipo(Modelo, Codigo), es_detalle_de_equipo(Detalle, Codigo), 
	es_problema_de_equipo(Problema, Codigo), es_costo_de_equipo(Costo, Codigo), 
	es_estado_de_equipo(Estado, Codigo).


%%% ----------------------------------------------------------------------------
%%% ----------------------------------------------------------------------------
