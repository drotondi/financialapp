# financialapp

Aplicación 100% HTML que guarda activos, pasivos e inversiones directamente en el navegador con `localStorage`. No requiere servidor ni dependencias adicionales.

## Cómo usar

1. Descarga o clona este repositorio.
2. Abre el archivo `index.html` en tu navegador preferido (doble clic o servirlo con `python -m http.server`).
3. Registra cualquier transacción (activo, pasivo o inversión) desde el único formulario: selecciona el tipo, completa monto, categoría, fecha (selector de calendario) y notas opcionales.
4. Consulta el dashboard con totales, desgloses por categoría y gráfico de distribución; revisa o elimina registros en la tabla inferior.
5. Usa los botones "Exportar JSON" y "Borrar datos" para respaldar o limpiar tu información local.

> Los datos permanecen únicamente en el dispositivo donde abras la página. Si limpias el caché del navegador, también se eliminarán.
