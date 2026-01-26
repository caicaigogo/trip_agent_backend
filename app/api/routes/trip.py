from fastapi import APIRouter, HTTPException
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

        budget = {
            'total_attractions': 1000,
            'total_hotels': 2000,
            'total_meals': 3000,
            'total_transportation': 4000,
            'total': 10000
        }
        days = [
            {
                'date': request.start_date,
                'day_index': 0,
                'description': '当日行程描述',
                'transportation': '交通方式',
                'accommodation': '住宿',
                'attractions': [
                    {'name': '长城'},
                    {'name': '故宫'}
                ]
            },
            {
                'date': request.end_date,
                'day_index': 1,
                'description': '当日行程描述',
                'transportation': '交通方式',
                'accommodation': '住宿',
                'attractions': [
                    {'name': '天坛'}
                ]
            }
        ]
        weather_info = [{'date': request.start_date}, {'date': request.end_date}]
        data = {
            'city': request.city,
            'start_date': request.start_date,
            'end_date': request.end_date,
            'days': days,
            'weather_info': weather_info,
            'overall_suggestions': "总体建议",
            'budget': budget
        }

        return TripPlanResponse(
            success=True,
            message="旅行计划生成成功",
            data=data
        )

    except Exception as e:
        print(f"❌ 生成旅行计划失败: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"生成旅行计划失败: {str(e)}"
        )
