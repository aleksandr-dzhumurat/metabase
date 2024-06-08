prepare-dirs:
	rm -rf data/pg_data && \
	rm -rf data/metabase_data && \
	mkdir -p data/pg_data || true && \
    mkdir -p data/metabase_data || true && \
    mkdir -p data/sqlite_db || true