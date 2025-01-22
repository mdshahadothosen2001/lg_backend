from engage.local_govt.models import Localgovt


def find_local_govt(request):
    division = request.query_params.get('division_id')
    district = request.query_params.get('district_id')
    upazila = request.query_params.get('upazila_id')
    union = request.query_params.get('union_id')
    try:
        if union:
            return Localgovt.objects.get(division=division, district=district, upazila=upazila, union=union).id
        elif upazila:
            return Localgovt.objects.get(division=division, district=district, upazila=upazila, union=None).id
        elif district:
            return Localgovt.objects.get(division=division, district=district, upazila=None, union=None).id
        elif division:
            return Localgovt.objects.get(division=division, district=None, upazila=None, union=None).id
    except:
        return None
