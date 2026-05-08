from itertools import pairwise

from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph

from og_agents.state import GenerationState
from og_agents.workflows.nodes import BaseNode
from og_agents.workflows.workflow_context import WorkflowContext
from og_agents.workflows.requests import GenerateOntologyRequest


class OntologyGenerationWorkflowBuilder:

    def __init__(self, nodes: list[BaseNode]):
        if not nodes:
            raise ValueError("OntologyGenerationWorkflowBuilder requires at least one node")
        self._nodes = nodes

    @classmethod
    def of(cls, nodes: list[BaseNode]) -> "OntologyGenerationWorkflowBuilder":
        return cls(nodes)

    def build(
        self,
    ) -> CompiledStateGraph[GenerationState, WorkflowContext, GenerateOntologyRequest]:
        graph = StateGraph(GenerationState)
        node_names = [
            f"{i:02d}_{node.__class__.__name__}" for i, node in enumerate(self._nodes)
        ]
        for node, name in zip(self._nodes, node_names):
            graph.add_node(name, node)
        graph.add_edge(START, node_names[0])
        for src, dst in pairwise(node_names):
            graph.add_edge(src, dst)
        graph.add_edge(node_names[-1], END)
        return graph.compile()
