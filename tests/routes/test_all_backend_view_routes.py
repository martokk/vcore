import pytest
from fastapi.testclient import TestClient
from httpx import Cookies


@pytest.mark.asyncio
async def test_all_page_routes(client: TestClient, normal_user_cookies: Cookies) -> None:
    """Test that all page routes load successfully."""

    # Define all routes to test with their expected status codes
    routes = [
        # Public routes (no auth required)
        ("/login", 200),
        ("/favicon.ico", 200),
        # Protected routes (auth required)
        ("/", 200),
        ("/dashboard", 200),
        ("/jobs", 200),
        ("/jobs/create", 200),
    ]

    # Set cookies for authentication
    client.cookies = normal_user_cookies

    # Test each route
    for route, expected_status in routes:
        response = client.get(route)

        assert (
            response.status_code == expected_status
        ), f"Route {route} failed with status {response.status_code}"
