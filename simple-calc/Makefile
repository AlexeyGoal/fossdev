.PHONY: help install dev-install test lint format clean build upload-test

help:
	
	@echo "  install      - Установка пакета"
	@echo "  dev-install  - Установка с dev зависимостями"
	@echo "  test         - Запуск тестов"
	@echo "  lint         - Проверка стиля кода"
	@echo "  format       - Форматирование кода"
	@echo "  clean        - Очистка временных файлов"
	@echo "  build        - Сборка пакета"
	@echo "  upload-test  - Загрузка на TestPyPI"

install:
	pip install .

dev-install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v --cov=simplecalc --cov-report=html --cov-report=term

lint:
	flake8 src/ tests/ --max-line-length=88

format:
	black src/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

build: clean
	python -m build

upload-test: build
	python -m twine upload --repository testpypi dist/*