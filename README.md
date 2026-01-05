# financialapp

Aplicación 100% HTML que guarda activos y pasivos directamente en el navegador con `localStorage`. No requiere servidor ni dependencias adicionales.

## Cómo usar

1. Descarga o clona este repositorio.
2. Abre el archivo `index.html` en tu navegador preferido (doble clic o servirlo con `python -m http.server`).
3. Registra cualquier transacción (activo o pasivo) desde el único formulario: selecciona el tipo, elige una categoría de la lista desplegable según corresponda, completa monto, fecha (selector de calendario) y notas opcionales. Si necesitas otra categoría, elige "Otro" y escribe el nombre.
4. Consulta el dashboard con totales, desgloses por categoría y gráfico de distribución; revisa o elimina registros en la tabla inferior (el botón de eliminar funciona por fila).
5. Usa los botones "Generar PDF", "Exportar JSON" y "Borrar datos" para obtener un reporte imprimible, respaldar o limpiar tu información local.

> Los datos permanecen únicamente en el dispositivo donde abras la página. Si limpias el caché del navegador, también se eliminarán.
