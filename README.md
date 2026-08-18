# Football Analytics Platform
## Overview
The football analytics platform is an end-to-end data engineering and analytics project that ingests football data from an external API, transforms and models the data through multiple layers, and prepares it for analytics.

The project is designed to demonstrate a production-style data pipeline, including API ingestion, data processing, dimensional modelling, data warehousing, and business intelligence.

## Purpose

The main objectives of the project are to:
- Ingest football data from an external API
- Store the raw API responses for traceability and reproducibility
- Process and transform data through multiple layers
- Build a dimensional data warehouse using fact and dimension tables
- Create analytics-ready data marts
- Develop Power BI dashboards and visualizations
- Apply data engineering practices such as configuration management, logging, testing, and pipeline orchestration

## Architecture
- Football API
- Landing/Bronze -> Raw API layer
- Staging/Silver -> Cleaned & transformed data
- Data Warehouse/Gold -> Star Schema
- Data Marts
- Power BI Dashboards

## Data Warehouse
The warehouse follows a dimensional modelling/star schema approach
### Dimensions
| Dimension | Description |
|-----------|-------------|
| DimCompetition | Competition and tournament information |
| DimSeason | Football season information |
| DimTeam | Team information |
| DimVenue | Venue/Stadium information |
| DimDate | Calender and data atrributes |

### Fact Tables
| Fact Table | Description |
|------------|-------------|
| FactMatch | Match-level results and stats

This structure allows football events and performance metrics to be analyzed across different dimensions such as teams, seasons, competitions, and dates.

## Technology Stack
### Data Engineering
- Python
- Requests
- Pandas
- SQLAlchemy
- python-dotenv
- SQL

### Databases
- PostgreSQL
- DuckDB -> testing purposes

### Analytics and Visualizations
- PowerBI

### Development & Version Control
- VS Code
- Git
- GitHub

## Pipeline
The pipeline is being developed incrementally, with each stage responsible for a specific part of the data lifecycle.

### 1. API Ingestion
Football data is retrieved form an external API (SportsAPIPro) using Python

The ingestion layer is responsible for:
- Api authentication
- Request handling
- Response Validation
- Error handling
- Logging
- Saving raw responses

Raw data is retained so that transformations can be reproduced without repeatedly requesting the API.

### 2. Landing / Bronze

The Broze layer contains the raw data received from the API with minimal transformation.

This layer acts as the historical landing zone and provides a source of truth for subsequent processing.

### 3. Staging / Silver
The Silver layer will contain cleaned and standardized data.

Typical processing includes:
- Data type standardization
- Handling missing values
- Removing duplicates
- Normalizing nested API structures
- Validating records
- Preparing entities for warehouse loading

### 4. Data Warehouse / Gold
The Gold layer contains the analytical data warehouse.

Data is transformed into a dimensional model consisting of fact and dimension tables.

The warehouse is designed to support analytical queries such as:
- Team performance across seasons
- Competition performance
- Match results
- League standings
- Historical team performance
- Comparative analysis between teams and competitions

### 5. Data Marts
Data marts will provide specialized datasets designed for specific analytical use cases

Examples may include:
- Team Performance Mart
- Competition Performance Mart
- Match Analytics Mart
- League Standings Mart

### 6. Power BI
Power BI will consume the analytical data marts and provide dashboards for exploring football performance and trends

Potential dashboard areas include:
- League Standings
- Team Standings
- Match Results
- Competition Analysis
- Seasonal Trends

## Configuration
Sensitive configuration such as database credentials and API keys is stored in environment variables rather than commited to source control.

The *.env* file is excluded from version control through *.gitignore*.

## Development Approach
The project is being developed in phases:

1. Project setup and repository structure
2. API exploration and ingestion
3. Entity identification
4. Data warehouse design
5. Data transformation
6. Warehouse loading
7. Data marts
8. Analytics and Power BI
9. Testing and data quality
10. Pipeline orchestration and automation
11. Monitoring and documentation

The project is intentionally being developed incrementally so that each stage can be tested and validated before moving downstream.
## Key Learning Outcomes

This project is being used to develop practical experience with:
- API-based data ingestion
- ETL / ELT pipeline development
- Data modelling
- Dimensional modeling
- Data warehousing
- PostgreSQL
- Python for data engineering
- SQL
- Data quality and testing
- Logging and error handling
- Git and version control
- Business intelligence
- Pipeline orchestration
- Production-oriented data engineering practices

## Future Architecture

The long-term goal is to evolve the platform from a local development project into a more production-oriented analytics platform.

Potential future additions include:
- Cloud object storage
- Cloud-based data warehouses
- Workflow orchestration
- Automated data quality checks
- CI/CD pipelines
- Monitoring and alerting
- Incremental data loading
- Historical data tracking
- Advanced football analytics and machine learning
## Project Status: 🚧 Currently in Phase 5: ETL Loading

### Completed
- [X] Project repository setup
- [x] API exploration
- [x] API client development
- [x] Environment configuration
- [x] Raw data directory structure
- [x] Initial entity identification
- [x] Initial dimensional warehouse design
- [x] PostgreSQL warehouse planning

### In Progress
- [ ] Warehouse implementation
- [ ] Dimension table creation
- [ ] Fact table creation
- [ ] Data transformation pipelines
- [ ] Warehouse loading

### Planned
- [ ] Data marts
- [ ] Power BI dashboards
- [ ] Automated pipeline execution
- [ ] Data quality testing
- [ ] Pipeline monitoring
- [ ] CI/CD