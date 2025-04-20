#### 1.a
Antes de la computación en la nube cada usuario/empresa que requiriera de una infraestructura de software debía comprar enteramente el hardware. Esto involucraba el diseño, el mantenimiento y el costo de esta tarea. Es decir, estaba sujeto a precios elevados de hardware y el costo de un equipo encargado del correcto funcionamiento y manutención, así como, si dado el caso de aumentar las necesidades de potencia, se debía comprar nuevamente hardware costoso.

La centralización en data centers se encargan de realizar estas tareas, a través de poner a disposición de sus clientes arquitecturas de hardware, a través de un costo (menor al de la compra y manutención), que además se puede escalar de manera eficiente y directa. 

#### 1.b
Se hace referencia como "the power wall" a la limitación de la frecuencia de CPU, diseño de CPU, y rendimiento de CPU causados por las restricciones térmicas o eléctricas que causarían inestabilidad en los procesadores.

#### 2.a
La necesidad de atender grandes volúmenes de tráfico en sitios web conlleva a la adopción de clústeres debido a que sumar más servidores con una misma capacidad y dividirse la carga es más costo-eficiente que aumentar la potencia del hardware utilizado. A esta solución se le conoce como adición de nodos al cluster, en la que cada nodo está ejecutando la aplicación. Así, también surge la técnica de load balancing, la cual permite evitar la sobrecarga de un servidor, particionándolo entre otros nodos.

#### 2.b
Un desarrollador de software, encargado de mantener el servicio de matrícula de una universidad, conoce que en la época de matrículas se produce un alto tráfico de usuarios y con muchas peticiones. Esto puede, y llega, a sobrecargar muchos sistemas. Así, tras el uso de un load balancer, se previene la caída completa de la página de matrícula, pues se mantiene varias instancias de la aplicación. 

#### 3.a
Es el dinamismo en el uso de hardware necesario para ejecutar una aplicación en la nube variante según la demanda presente en la aplicación.


#### 3.b
Para el uso de elastic computing, debemos notar que en el mismo hardware se ejecutan más de una aplicación. La virtualización permite la contenerización de las aplicaciones, facilitando el proceso de ejecución, pues si ocurren bugs dentro de una aplicación, esta no afecta a otras https://www.elastic.co/blog/how-to-handle-elasticsearch-virtualization

#### 3.c
Hemos de notar que el elastic computing nos permite no tener todo el hardware siendo utilizado al mismo tiempo. Así, si, por ejemplo, Amazon.com, deseara diseñar su plataforma sin elastic computing, teniendo en cuenta el alto tráfico que se genera en distintas épocas del año, sería complicado el diseño tomando en cuenta zonas, fechas y minimizando el costo. Esto resultaría en o bien una aplicación extremadamente cara de mantener, o una aplicación de poca confiabilidad en su estabilidad, pues caería ante altas fluctuaciones en el tráfico.

#### 4.a
Por ejemplo, para una aplicación la cual requiera de una base de datos sencilla sin la necesidad de especificación de versión de sistema operativo o control del versionado de kernel.


#### 5.a
Las ventajas de implementar una nube privada son la privacidad y seguridad de sus datos, control y flexibilidad, así como la libertad para hacer cambios a nivel arquitectura, elección de hardware y software a elección.

