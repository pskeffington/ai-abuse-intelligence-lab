"""Graph construction for normalized intelligence events."""

from __future__ import annotations

from dataclasses import dataclass

import networkx as nx

from ai_abuse_intel_lab.models import AbuseEvent


@dataclass(frozen=True)
class EventGraphSummary:
    """Compact graph metrics for analyst reporting."""

    node_count: int
    edge_count: int
    connected_component_count: int
    largest_component_size: int


class EventGraphBuilder:
    """Build an actor-artifact-event graph from normalized events."""

    def build(self, events: list[AbuseEvent]) -> nx.Graph:
        """Return an undirected graph connecting events to actors, artifacts, and tags."""

        graph = nx.Graph()
        for event in events:
            event_node = self._event_node_id(event)
            graph.add_node(
                event_node,
                node_type="event",
                event_type=event.event_type.value,
                observed_at=event.observed_at.isoformat(),
                narrative=event.narrative,
            )

            if event.actor and event.actor.handle:
                actor_node = self._actor_node_id(event.actor.handle)
                graph.add_node(
                    actor_node,
                    node_type="actor",
                    handle=event.actor.handle,
                    platform=event.actor.platform,
                )
                graph.add_edge(event_node, actor_node, relationship="observed_actor")

            if event.artifact:
                artifact_node = self._artifact_node_id(event.artifact.value)
                graph.add_node(
                    artifact_node,
                    node_type="artifact",
                    artifact_type=event.artifact.artifact_type,
                    value=event.artifact.value,
                )
                graph.add_edge(event_node, artifact_node, relationship="contains_artifact")

            for tag in event.tags:
                tag_node = self._tag_node_id(tag)
                graph.add_node(tag_node, node_type="tag", value=tag)
                graph.add_edge(event_node, tag_node, relationship="tagged_as")

        return graph

    def summarize(self, graph: nx.Graph) -> EventGraphSummary:
        """Return compact graph metrics."""

        component_sizes = [len(component) for component in nx.connected_components(graph)]
        return EventGraphSummary(
            node_count=graph.number_of_nodes(),
            edge_count=graph.number_of_edges(),
            connected_component_count=len(component_sizes),
            largest_component_size=max(component_sizes, default=0),
        )

    @staticmethod
    def _event_node_id(event: AbuseEvent) -> str:
        return f"event:{event.event_id}"

    @staticmethod
    def _actor_node_id(handle: str) -> str:
        return f"actor:{handle}"

    @staticmethod
    def _artifact_node_id(value: str) -> str:
        return f"artifact:{value}"

    @staticmethod
    def _tag_node_id(tag: str) -> str:
        return f"tag:{tag}"
