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
                    {
                        'name': '长城',
                        'ticket_price': 100,
                        'address': 'no1',
                        'visit_duration': 60,
                        'description': 'beautiful',
                        'rating': 5.0
                    },
                    {
                        'name': '故宫',
                        'ticket_price': 150,
                        'address': 'no2',
                        'visit_duration': 120,
                        'description': 'pretty',
                        'rating': 4.8
                    }
                ],
                'hotel': {
                    'name': '文华酒店',
                    'address': '150号',
                    'price_range': '1000-2000',
                    'rating': '4.7',
                    'distance': '1.5km',
                    'type': '豪华酒店'
                },
                'meals': [
                    {
                        'name': '面线糊',
                        'type': 'breakfast',
                        'description': 'delicious'
                    },
                    {
                        'name': '沙茶面',
                        'type': 'lunch',
                        'description': 'yummy'
                    }
                ],
            },
            {
                'date': request.end_date,
                'day_index': 1,
                'description': '当日行程描述',
                'transportation': '交通方式',
                'accommodation': '住宿',
                'attractions': [
                    {
                        'name': '天坛',
                        'ticket_price': 200,
                        'address': 'no3',
                        'visit_duration': 150,
                        'description': 'interesting',
                        'rating': 4.1
                    }
                ],
                'hotel': {
                    'name': '四季酒店',
                    'address': '100号',
                    'price_range': '5000-1000',
                    'rating': '4.5',
                    'distance': '1.2km',
                    'type': '标准酒店'
                },
                'meals': [
                    {
                        'name': '热干面',
                        'type': 'snack',
                        'description': 'good'
                    }
                ],
            }
        ]

        weather_info = [
            {
                'date': request.start_date,
                'day_weather': '晴',
                'night_weather': '晴',
                'day_temp': 15,
                'night_temp': 25,
                'wind_direction': '东南',
                'wind_power': '3',
            },
            {
                'date': request.end_date,
                'day_weather': '晴',
                'night_weather': '雨',
                'day_temp': 18,
                'night_temp': 10,
                'wind_direction': '西北',
                'wind_power': '8',
            }
        ]
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
