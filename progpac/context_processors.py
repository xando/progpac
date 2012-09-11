def default(request):
    from progpac.core.models import Level

    return {
        'tutorial_levels': Level.objects.filter(tier__name="Tutorial"),
        'game_levels': Level.objects.exclude(tier__name="Tutorial")
    }
