from django.views.generic import TemplateView

from common.functions import get_data


class MainStatsView(TemplateView):
    """
    Страница с отображением всех данных по параметрам или же по умолчанию.
    """
    template_name = "main_task/statistics_from_keitaro.html"

    def get_context_data(self, *args, **kwargs):
        date_from = self.request.GET.get("date_from", False)
        date_to = self.request.GET.get("date_to", False)
        data = get_data(name="bogdan", date_from=date_from, date_to=date_to)
        return {"total_clicks": data["clicks"], "total_conversion": data["conversion"]}

