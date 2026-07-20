import random
import datetime
import statistics
from collections import Counter

# Diccionario de configuración de rubros con sus métricas de negocio
SECTORS = {
    "1": {
        "rubro": "Banco", 
        "prefix": "banco", 
        "endpoints": ["/api/login", "/api/transfer"],
        "biz_started_label": "Intentos de Transferencia",
        "biz_success_label": "Transferencias Liquidadas"
    },
    "2": {
        "rubro": "Clínica", 
        "prefix": "clinica", 
        "endpoints": ["/api/auth", "/api/triage"],
        "biz_started_label": "Intentos de Reserva de Hora",
        "biz_success_label": "Horas Médicas Agendadas"
    },
    "3": {
        "rubro": "Fintech", 
        "prefix": "fintech", 
        "endpoints": ["/api/trade", "/api/settle"],
        "biz_started_label": "Órdenes de Trading Creadas",
        "biz_success_label": "Órdenes Ejecutadas (Match)"
    },
    "4": {
        "rubro": "E-commerce", 
        "prefix": "ecommerce", 
        "endpoints": ["/api/checkout", "/api/invoice"],
        "biz_started_label": "Carritos de Compra Creados",
        "biz_success_label": "Checkouts Pagados"
    },
    "5": {
        "rubro": "Contabilidad", 
        "prefix": "contabilidad", 
        "endpoints": ["/api/ledger", "/api/audit"],
        "biz_started_label": "Asientos Contables Recibidos",
        "biz_success_label": "Asientos Cuadrados y Cerrados"
    }
}

def simulate_latency_and_status(error_rate_modifier):
    """Simula una transacción técnica generando latencia y códigos HTTP."""
    dice_roll = random.random()
    if dice_roll < 0.80:
        latency = random.uniform(0.05, 0.30)
    elif dice_roll < 0.95:
        latency = random.uniform(0.50, 1.50)
    else:
        latency = random.uniform(2.00, 5.00)

    status_roll = random.random()
    if status_roll < error_rate_modifier:
        status_code = random.choice([500, 502, 503, 504])
    elif status_roll < (error_rate_modifier + 0.05): 
        status_code = random.choice([400, 401, 403, 404])
    else:
        status_code = random.choice([200, 201])
        
    return latency, status_code

def calculate_percentile(data, percentile):
    """Calcula el percentil de una lista numérica."""
    if not data: return 0.0
    sorted_data = sorted(data)
    idx = min(int(len(sorted_data) * percentile / 100), len(sorted_data) - 1)
    return sorted_data[idx]

def run_sre_budget_lab():
    print("=== LABORATORIO SRE: DEFINICIÓN DE SLIs TÉCNICOS Y DE NEGOCIO ===")
    for key, val in SECTORS.items():
        print(f"[{key}] {val['rubro']}")
    
    choice = input("\nSelecciona el rubro (1-5): ").strip()
    if choice not in SECTORS:
        print("Opción inválida.")
        return

    sector = SECTORS[choice]
    TOTAL_WINDOW_DAYS = 30
    elapsed_days = random.randint(5, 28) 
    
    # 2 TPS aprox, fluctuando ligeramente
    tps = random.uniform(1.85, 2.15)
    seconds_elapsed = elapsed_days * 24 * 60 * 60
    current_trx = int(seconds_elapsed * tps)
    run_error_rate = random.uniform(0.005, 0.025) 

    print(f"\nRecopilando telemetría hasta el día {elapsed_days} para: {sector['rubro']}")
    print(f"Calculando logs técnicos a {tps:.2f} TPS (Procesando millones de registros)...")
    
    status_counts = Counter()
    latencies = []

    for _ in range(current_trx):
        latency, status = simulate_latency_and_status(run_error_rate)
        status_counts[status] += 1
        latencies.append(latency)

    server_errors = sum(v for k, v in status_counts.items() if k >= 500)
    client_errors = sum(v for k, v in status_counts.items() if 400 <= k < 500)
    successful_req = sum(v for k, v in status_counts.items() if k < 400)
    
    # ==========================================
    # CÁLCULO DE MÉTRICA DE NEGOCIO
    # ==========================================
    # Asumimos que entre un 15% y 30% del tráfico total corresponde al flujo core del negocio
    biz_started = int(current_trx * random.uniform(0.15, 0.30))
    
    # La tasa de conversión (éxito comercial) varía aleatoriamente entre 82% y 94%
    # El resto son caídas lógicas (ej. fondos insuficientes, cliente se arrepiente, fraude)
    biz_conversion_rate = random.uniform(0.82, 0.94)
    biz_success = int(biz_started * biz_conversion_rate)
    biz_failed = biz_started - biz_success

    execution_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')

    print("\n" + "="*75)
    print("📋 EVIDENCIA DE EJECUCIÓN - LABORATORIO SRE")
    print("="*75)
    print(f"   Fecha y Hora de Generación        : {execution_timestamp}")
    print(f"   Sector Analizado                  : {sector['rubro'].upper()}")
    print(f"   Ventana de Tiempo Analizada       : Día {elapsed_days} de {TOTAL_WINDOW_DAYS}")
    print("-" * 75)
    print("   [Métricas de Infraestructura y Red]")
    print(f"   Peticiones Procesadas hasta hoy   : {current_trx:,}")
    print(f"   Respuestas Exitosas (2xx/3xx)     : {successful_req:,}")
    print(f"   Errores de Cliente (4xx)          : {client_errors:,}")
    print(f"   Errores de Servidor (5xx)         : {server_errors:,}")
    print("-" * 75)
    print("   [Métricas de Rendimiento (Latencia)]")
    print(f"   Promedio : {statistics.mean(latencies):.4f}s")
    print(f"   p50      : {calculate_percentile(latencies, 50):.4f}s")
    print(f"   p90      : {calculate_percentile(latencies, 90):.4f}s")
    print(f"   p95      : {calculate_percentile(latencies, 95):.4f}s")
    print("-" * 75)
    print("   [Métricas de Impacto en el Negocio]")
    print(f"   {sector['biz_started_label']:<32}: {biz_started:,}")
    print(f"   {sector['biz_success_label']:<32}: {biz_success:,}")
    print(f"   Mermas lógicas (No técnicas)      : {biz_failed:,}")
    print("="*75)
    
if __name__ == "__main__":
    run_sre_budget_lab()