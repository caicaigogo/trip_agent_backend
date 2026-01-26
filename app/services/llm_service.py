# 全局LLM实例
_llm_instance = None

HelloAgentsLLM = None


def get_llm() -> HelloAgentsLLM:
    """
    获取LLM实例(单例模式)

    Returns:
        HelloAgentsLLM实例
    """
    global _llm_instance
