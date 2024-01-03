from models.WeatherForecastModel import WeatherForecastModel
from models.DailyForecastModel import DailyForecastModel
from models.HourlyForecastModel import HourlyForecastModel


def AnalyzeReplyService(APIreply):
    obj = WeatherForecastModel("2023-12-29T16:33", "15", "77", "1", "8", "3", "10", "90",
                                                [
                                                    DailyForecastModel("2023-12-19", "0", "20", "25", "2023-12-29T07:17", "2023-12-29T14:59", "0", "0", "0"),
                                                    DailyForecastModel("2023-12-29", "55", "20", "25", "2023-12-29T07:17", "2023-12-29T14:59", "0", "0", "0"),
                                                    DailyForecastModel("2023-12-09", "78", "20", "25", "2023-12-29T07:17", "2023-12-29T14:59", "0", "0", "0")],
                                                [
                                                    HourlyForecastModel("2023-12-29T07:00", "10", "0"),
                                                    HourlyForecastModel("2023-12-29T08:00", "12", "1"),
                                                    HourlyForecastModel("2023-12-29T09:00", "15", "2"),
                                                    HourlyForecastModel("2023-12-29T10:00", "12", "55"),
                                                    HourlyForecastModel("2023-12-29T11:00", "0", "78"),
                                                    HourlyForecastModel("2023-12-29T12:00", "-5", "95"),
                                                    HourlyForecastModel("2023-12-29T13:00", "-1", "22"),
                                                    HourlyForecastModel("2023-12-29T14:00", "22", "lol"),
                                                    HourlyForecastModel("2023-12-29T15:00", "3", "-1"),
                                                    HourlyForecastModel("2023-12-29T16:00", "0", "0")]
                                                    )
    return obj