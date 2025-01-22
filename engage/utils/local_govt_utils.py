def find_local_govt(request):
    division = request.GET.get('division')
    district = request.GET.get('district')
    upazila = request.GET.get('upazila')
    union = request.GET.get('union')
    if union:
        return 'union'
    elif upazila:
        return 'upazila'
    elif district:
        return 'district'
    elif division:
        return 'division'
    return None
