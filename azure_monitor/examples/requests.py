import requests
from azure_monitor import AzureMonitorSpanExporter
from opentelemetry import trace
from opentelemetry.ext import http_requests
from opentelemetry.sdk.trace import Tracer
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor

trace.set_preferred_tracer_implementation(Tracer)

http_requests.enable(trace.tracer())
span_processor = SimpleExportSpanProcessor(
    AzureMonitorSpanExporter(instrumentation_key="<INSTRUMENTATION KEY HERE>")
)
trace.tracer().add_span_processor(span_processor)

with trace.tracer().start_as_current_span("parent"):
    response = requests.get("<URL HERE>", timeout=5)

