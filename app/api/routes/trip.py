from fastapi import APIRouter
from ...models.schemas import (
    TripRequest,
    TripPlanResponse
)

router = APIRouter(prefix="/trip", tags=["旅行规划"])


@router.post(
    "/plan",
    response_model=TripPlanResponse,
    summary="生成旅行计划",
    description="根据用户输入的旅行需求,生成详细的旅行计划"
)
async def plan_trip(request: TripRequest):
    """
    生成旅行计划

    Args:
        request: 旅行请求参数

    Returns:
        旅行计划响应
    """
    try:
        print(f"\n{'=' * 60}")
        print(f"📥 收到旅行规划请求:")
        print(f"   城市: {request.city}")
        print(f"   日期: {request.start_date} - {request.end_date}")
        print(f"   天数: {request.travel_days}")
        print(f"{'=' * 60}\n")

        data = [
            {'id': 1, 'name': 'name', 'email': 'email'}
        ]

        return TripPlanResponse(
            success=True,
            message="旅行计划生成成功",
            data=data
        )

    except Exception as e:
        print(f"❌ 生成旅行计划失败: {str(e)}")
