import pytest
from fastapi.testclient import TestClient
from httpx import Cookies


@pytest.mark.asyncio
async def test_all_page_routes(client: TestClient, normal_user_cookies: Cookies) -> None:
    """Test that all page routes load successfully."""

    # Define all routes to test with their expected status codes
    unprotected_routes = [
        # Public routes (no auth required)
        ("/", 200),
        ("/dashboard", 404),
        ("/login", 200),
        ("/favicon.ico", 200),
    ]

    protected_routes = [
        # Protected routes (auth required)
        ("/", 404),
        ("/dashboard", 404),
        ("/jobs", 200),
    ]

    def test_routes(routes: list[tuple[str, int]]) -> None:
        for route, expected_status in routes:
            response = client.get(route)
            assert (
                response.status_code == expected_status
            ), f"Route {route} failed with status {response.status_code}"

    # Test each route
    test_routes(unprotected_routes)

    # Set cookies for authentication
    client.cookies = normal_user_cookies
    test_routes(protected_routes)
