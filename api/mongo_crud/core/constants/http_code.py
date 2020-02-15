from collections import namedtuple

StatusCode = namedtuple('StatusCode', ['code', 'description'])

# Error
ERROR_500 = StatusCode(500, 'Internal error')
ERROR_100 = StatusCode(100, 'Continue')
ERROR_101 = StatusCode(101, 'Switching Protocols')
ERROR_203 = StatusCode(203, 'Non-Authoritative Information')
ERROR_204 = StatusCode(204, 'No Content')
ERROR_205 = StatusCode(205, 'Reset Content')
ERROR_206 = StatusCode(206, 'Partial Content')
ERROR_304 = StatusCode(304, 'Not Modified')
ERROR_305 = StatusCode(305, 'Use proxy is not set')
ERROR_400 = StatusCode(400, 'Bad Request')
ERROR_401 = StatusCode(401, 'Unauthorized')
ERROR_402 = StatusCode(402, 'Payment required')
ERROR_403 = StatusCode(403, 'Forbidden')
ERROR_404 = StatusCode(404, 'Not found')
ERROR_407 = StatusCode(407, 'Proxy Authentication required')
ERROR_408 = StatusCode(408, 'Request timeout')
ERROR_409 = StatusCode(409, 'Conflit')
ERROR_502 = StatusCode(502, 'Bad gateway')
ERROR_503 = StatusCode(503, 'Service Unavailable')
ERROR_504 = StatusCode(504, 'Gateway timeout')

# Success
SUCCESS_200 = StatusCode(200, 'Ok')
SUCCESS_201 = StatusCode(201, 'Created')
SUCCESS_202 = StatusCode(202, 'Accepted')
