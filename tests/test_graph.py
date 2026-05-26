from pathlib import Path

from ai_abuse_intel_lab.analysis import EventGraphBuilder
from ai_abuse_intel_lab.ingestion import CsvEventLoader


def test_event_graph_builder_connects_events_to_shared_tags_and_actors() -> None:
    events = CsvEventLoader(Path("examples/sample_events.csv")).load()
    builder = EventGraphBuilder()

    graph = builder.build(events)
    summary = builder.summarize(graph)

    assert graph.has_node("actor:@alpha")
    assert graph.has_node("tag:synthetic")
    assert summary.node_count == graph.number_of_nodes()
    assert summary.edge_count == graph.number_of_edges()
    assert summary.connected_component_count == 1
    assert summary.largest_component_size == graph.number_of_nodes()
