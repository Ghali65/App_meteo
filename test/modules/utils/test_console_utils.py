from p_meteo.modules.utils.console_utils import clear_console


def test_clear_console_runs_without_error():
    # La fonction ne doit pas lever d'exception
    try:
        clear_console()
    except Exception as e:
        assert False, f"clear_console() a levé une exception : {e}"

    # Si on arrive ici, le test est réussi
    assert True
