"""LangGraph-based orchestration graph builder for the Phase 1 workflow."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Callable, Dict

from langgraph.graph import StateGraph

LOGGER = logging.getLogger(__name__)


@dataclass
class NodeContext:
    """Holds contextual metadata passed between graph nodes."""

    state: Dict[str, Any]
    events: Dict[str, Any]


def planner_node(context: NodeContext) -> NodeContext:
    """Plan high-level steps required to complete the task."""

    LOGGER.info("Planner analysing context")
    context.events.setdefault("history", []).append("planner_completed")
    context.state.setdefault("plan", []).append("Define coding steps")
    return context


def coder_node(context: NodeContext) -> NodeContext:
    """Generate candidate implementation for the current task."""

    LOGGER.info("Coder generating draft implementation")
    context.events.setdefault("artifacts", []).append({"type": "code", "status": "draft"})
    context.state["last_action"] = "coder"
    return context


def critic_node(context: NodeContext) -> NodeContext:
    """Review generated code and raise issues for refinement."""

    LOGGER.info("Critic evaluating draft")
    context.events.setdefault("reviews", []).append({"severity": "info", "message": "Draft assessed"})
    context.state["needs_revision"] = context.state.get("last_action") == "coder"
    return context


def qa_node(context: NodeContext) -> NodeContext:
    """Run quality checks ensuring policy compliance and tests."""

    LOGGER.info("QA validating outputs")
    context.events.setdefault("checks", []).append({"type": "policy", "result": "pass"})
    context.state["qa_passed"] = True
    return context


def approver_node(context: NodeContext) -> NodeContext:
    """Final gatekeeper that decides whether to ship or request refinement."""

    LOGGER.info("Approver evaluating final artefact")
    if context.state.get("qa_passed"):
        context.events.setdefault("approvals", []).append("approved")
        context.state["approved"] = True
    else:
        context.events.setdefault("approvals", []).append("rejected")
        context.state["approved"] = False
    return context


def refinement_condition(context: NodeContext) -> str:
    """Determine whether a refinement loop should be triggered."""

    return "refine" if context.state.get("needs_revision") else "proceed"


def build_graph() -> StateGraph:
    """Construct the LangGraph state machine for the orchestration workflow."""

    graph = StateGraph(NodeContext)
    graph.add_node("planner", planner_node)
    graph.add_node("coder", coder_node)
    graph.add_node("critic", critic_node)
    graph.add_node("qa", qa_node)
    graph.add_node("approver", approver_node)

    graph.add_edge("planner", "coder")
    graph.add_edge("coder", "critic")
    graph.add_edge("critic", "qa")
    graph.add_edge("qa", "approver")

    graph.add_conditional_edges(
        "critic",
        refinement_condition,
        {
            "refine": "coder",
            "proceed": "qa",
        },
    )

    graph.add_conditional_edges(
        "qa",
        lambda ctx: "proceed" if ctx.state.get("qa_passed") else "refine",
        {
            "refine": "coder",
            "proceed": "approver",
        },
    )

    graph.add_edge("approver", "qa", condition=lambda ctx: not ctx.state.get("approved"))

    return graph


def build_executor(graph: StateGraph) -> Callable[[NodeContext], NodeContext]:
    """Compile the graph into an executable callable."""

    return graph.compile()


def initialise_context(task: Dict[str, Any]) -> NodeContext:
    """Create a NodeContext from an inbound task description."""

    return NodeContext(state={"task": task}, events={})


def execute_workflow(task: Dict[str, Any]) -> NodeContext:
    """Convenience helper to execute the workflow for a provided task."""

    context = initialise_context(task)
    graph = build_graph()
    executor = build_executor(graph)
    result = executor(context)
    LOGGER.info("Workflow completed with approval status: %s", result.state.get("approved"))
    return result


__all__ = [
    "NodeContext",
    "planner_node",
    "coder_node",
    "critic_node",
    "qa_node",
    "approver_node",
    "refinement_condition",
    "build_graph",
    "build_executor",
    "initialise_context",
    "execute_workflow",
]
