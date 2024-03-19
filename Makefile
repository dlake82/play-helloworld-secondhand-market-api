DIR?=.

.PHONY: container
setup:
	git config commit.template .gitmessage.txt
	poetry install
	poetry run pre-commit install
	chmod -R +x ./scripts

clean:
	rm -vrf ./build ./dist ./*.tgz ./*.egg-info .pytest_cache .mypy_cache
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm .coverag
	e

format:
	bash ./scripts/format.sh ${DIR}

typecheck:
	bash ./scripts/typecheck.sh ${DIR}

lint:
	bash ./scripts/lint.sh ${DIR}

test:
	bash ./scripts/test.sh

pre-commit:
	poetry run pre-commit


my:
	docker compose down
	docker build -t dfs .
	docker compose up -d
	docker logs --tail 100 dfs -f