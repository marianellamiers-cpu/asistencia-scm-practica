# main.py - Sistema de Asistencia (v2.1.0)
total_asistencias = 0
historial_registros = []


def registrar_asistencia(datos_alumno: dict):
    global total_asistencias
    dni = datos_alumno.get("dni", "").strip()
    materia = datos_alumno.get("materia", "Programación III")
    if len(dni) >= 7 and dni.isdigit():
        total_asistencias += 1
        historial_registros.append({"dni": dni, "materia": materia})
        print(f"[OK] Asistencia N°{total_asistencias} | DNI: {dni} | Materia: {materia}")
        return True
    print(f"[ERROR] Datos invalidos para DNI: {dni}")
    return False


def obtener_reporte_estadistico():
    return {
        "total_asistencias": total_asistencias,
        "detalle": list(historial_registros),
    }


if __name__ == "__main__":
    print("=== SISTEMA DE ASISTENCIA v2.1.0 ===")
    registrar_asistencia({"dni": "40123456", "materia": "Programación III"})
    registrar_asistencia({"dni": "38999111", "materia": "Práctica Profesional II"})
    print(obtener_reporte_estadistico())