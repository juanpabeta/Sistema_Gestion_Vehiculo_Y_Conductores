### 🚗 Sistema de gestión de vehículos y conductores
Este repositorio contiene el código de mi proyecto final para el curso de python cohorte 5 de DevSeniorCode .

## 🗒️ Descripción del Proyecto
Este programa es un sistema de gestión de vehiculos desarrollado en Python con la programción orientada a objetos. 
Este sistema le permite a la empresa **Transporte Seguro S.A** registrar diferentes vehículos(motos,carros y camiones), asignarles un conductor, iniciar y finalizar una jornada laboral

## 🎯 Objetivo del proyecto
- Aplicar los principios de la Programación Orientada a Objetos.
- Utilizar herencia, clases abstractas e interfaces.
- Implementar validaciones de datos.
- Separar responsabilidades usando el modelo de capas (models y services).

## 🧠 Conceptos de POO aplicados

- **Encapsulamiento:**  
  Uso de atributos privados y propiedades (`@property`) para proteger los datos.

- **Herencia:**  
  Las clases `Moto`, `Carro` y `Camion` heredan de la clase abstracta `Vehiculo`.`

- **Abstracción:**  
  La clase `Vehiculo` define métodos abstractos como `iniciarJornada()` y `finalizarJornada()`.

- **Polimorfismo:**  
  Cada tipo de vehículo implementa su propio comportamiento para moverse e iniciar la jornada.

- **Composición:**  
  Un vehículo tiene un motor (`Motor`) y puede tener un conductor (`Conductor`).
