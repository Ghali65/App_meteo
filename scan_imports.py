import pkgutil
import importlib
import p_meteo

print("=== Scan des modules ===")

for module in pkgutil.walk_packages(p_meteo.__path__, prefix="p_meteo."):
    name = module.name
    try:
        importlib.import_module(name)
        print(f"[OK] {name}")
    except Exception as e:
        print(f"[ERREUR] {name} → {e}")
