# [API Name] API Reference

**Author:** [Full Name]
**Created:** [Month DD, YYYY]
**Last Updated:** [Month DD, YYYY]
**Version:** [x.x.x]

---

## Overview

[One to three sentences describing the API's purpose, what it exposes, and who it is intended for.]

## Base URL

```text
https://[base-url]/[version]
```

## Authentication

[Describe the authentication method (API key, OAuth 2.0, JWT, etc.) and how to include credentials in requests.]

```http
Authorization: Bearer [token]
```

## Request Format

All requests must include the following headers unless otherwise noted:

| Header          | Value              | Required |
| --------------- | ------------------ | -------- |
| `Content-Type`  | `application/json` | Yes      |
| `Authorization` | `Bearer [token]`   | Yes      |

## Response Format

All responses return JSON in the following structure:

```json
{
  "data": {},
  "error": null,
  "meta": {
    "timestamp": "2026-05-05T00:00:00Z"
  }
}
```

## Endpoints

### [Resource Name]

#### `GET /[resource]`

Returns a list of [resource] records.

**Query Parameters:**

| Parameter | Type    | Required | Description                                         |
| --------- | ------- | -------- | --------------------------------------------------- |
| `limit`   | integer | No       | Maximum number of results to return. Default: `20`. |
| `offset`  | integer | No       | Number of results to skip. Default: `0`.            |

**Example Request:**

```http
GET /[resource]?limit=10&offset=0
Authorization: Bearer [token]
```

**Example Response:**

```json
{
  "data": [],
  "meta": {
    "total": 0,
    "limit": 10,
    "offset": 0
  }
}
```

---

#### `POST /[resource]`

Creates a new [resource] record.

**Request Body:**

| Field       | Type   | Required | Description                 |
| ----------- | ------ | -------- | --------------------------- |
| `fieldName` | string | Yes      | [Description of the field.] |

**Example Request:**

```http
POST /[resource]
Authorization: Bearer [token]
Content-Type: application/json

{
  "fieldName": "value"
}
```

**Example Response:**

```json
{
  "data": {
    "id": "abc123",
    "fieldName": "value"
  }
}
```

---

## Error Codes

| Code               | Status | Description                                                             |
| ------------------ | ------ | ----------------------------------------------------------------------- |
| `UNAUTHORIZED`     | 401    | The request is missing a valid authentication token.                    |
| `FORBIDDEN`        | 403    | The authenticated user does not have permission to perform this action. |
| `NOT_FOUND`        | 404    | The requested resource does not exist.                                  |
| `VALIDATION_ERROR` | 422    | The request body contains invalid or missing fields.                    |
| `INTERNAL_ERROR`   | 500    | An unexpected error occurred on the server.                             |

## Rate Limiting

[Describe rate limits, headers returned, and what to do when limits are exceeded.]

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for a history of API changes.
