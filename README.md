# financialapp

Aplicación 100% HTML que guarda activos y pasivos. Puedes usar `localStorage` o conectar Supabase (plan gratuito) para evitar depender del navegador. No requiere servidor ni dependencias locales.

## Cómo usar

1. Descarga o clona este repositorio.
2. Abre el archivo `index.html` en tu navegador preferido (doble clic o servirlo con `python -m http.server`).
3. Inicia sesión: usa el demo `demo@demo.test` / `demo123` o tus credenciales de Supabase si configuras URL y anon key en la sección de acceso.
4. Elige almacenamiento: local (navegador) o Supabase (gratis). Con Supabase se guardan/leen los registros en la tabla `registros_financieros` filtrados por tu correo.
5. Registra cualquier transacción (activo o pasivo) desde el único formulario: selecciona el tipo, elige una categoría de la lista desplegable según corresponda, completa monto, fecha (selector de calendario) y notas opcionales. Si necesitas otra categoría, elige "Otro" y escribe el nombre.
6. Consulta el dashboard con totales, desgloses por categoría y gráfico de distribución; revisa o elimina registros en la tabla inferior (el botón de eliminar funciona por fila).
7. Usa los botones "Generar PDF", "Exportar CSV", "Importar CSV" y "Borrar datos" para obtener un reporte imprimible, respaldar o recuperar datos precargados y limpiar tu información (local o Supabase según el modo).

## Alternativas gratuitas sin depender del almacenamiento local

1. **Supabase (recomendado)**: crea un proyecto gratuito en [supabase.com](https://supabase.com), habilita autenticación por correo/contraseña y una tabla `registros_financieros` con columnas `id (uuid PK)`, `type`, `name`, `category`, `amount (numeric)`, `currency`, `date`, `notes`, `owner (text)`, `created_at (timestamp default now())`. Copia la URL y la anon key en el formulario de acceso y usa tus credenciales para iniciar sesión. Los datos se guardarán en la nube y podrás accederlos desde cualquier dispositivo.
2. **CSV como respaldo**: aunque uses localStorage, puedes exportar/importar CSV para mover tus registros entre equipos gratis.

> Si eliges Supabase, los datos permanecen en la nube bajo tu cuenta gratuita. Si prefieres solo localStorage, recuerda que borrar caché elimina los registros.
