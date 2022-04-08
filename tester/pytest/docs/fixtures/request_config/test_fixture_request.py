

def test_request(request):
    assert "address" in request.config.inicfg.keys()
    assert request.config.inicfg["address"] == "192.168.1.100"
