from fastapi import Depends
from fastapi_limiter.depends import RateLimiter

global_rate_limit = Depends(RateLimiter(times=100, seconds=60))
login_rate_limit = Depends(RateLimiter(times=5, seconds=60))