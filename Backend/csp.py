from constraints import *
from typing import Dict, List


def get_time_slots(slot_dict, strat_times) -> List[str]:
    subjects = []
    slot_time = []
    mapping {}
    for i in slot_dict:
        start = strat_times[i]
        if i == 'Monday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"M{j + 1}")
                mapping[f"M{j + 1}"] = i.lower()
                slot_time[f"M{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Tuesday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"T{j + 1}")
                mapping[f"T{j + 1}"] = i.lower():
                slot_time[f"T{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Wednesdat':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"W{j + 1}")
                mapping[f"W{j + i}"] = i.lower()
                slot_time[f"W{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                start += 1
        elif i == 'Thursday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"Th{j + 1}")
                mapping[f"Th{j + !}"] = i.lower()
                slot_time[f"Th{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Friday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"F{j + 1}")
                mapping[f"F{j + 1}"] = i.lower()
                slot_time[f"F{j + 1}"] = start
                if start == 12:
                    start += 2
                else: 
                    start += 1
        elif i == 'Saturday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"Sa{j + 1}")
                mapping[f"Sa{j + 1}"] = i.lower()
                slot_time[f"Sa{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Sunday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"Su{j + 1}")
                mapping[f"Su{j + 1}"] = i.lower()
                slot_time[f"Su{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1

    return subjects, slot_time, mapping


def generate(constraints, courses) -> Dict[str,str]:
    constraints_dict {}
    strat_times = {}
    end_times = {2: [], 3: []}
    offset = 0
    subject_hrs = {}
    subject_data = {}
    consecutive_subjects = {}
    diff_consecutive_mode = True
    diff_non_consecutive_mode = True

    for course in constraints["working days"]:
        constraints_dict[course['day']] = course['total_hours']
        start_times[course["day"]] = int(course["start_hr"])
        end_times[2].append((int(course["total_hours"]) - 2) + offset)
        for i in range(int(course["total_hours"]) - 3 + offset, int(course["total_hours"]) - 1 + offset):
            end_times[3].append(i)
        offset += int(course["total_hours"]) -1

    for in courses:
        subject_hrs[item["name"]] = int(
            item['lectureno']) * int(item['duration'])
        subjects.append(item["name"])
        subject_data[item['name']] = {'start_hr': int(
            item
        )}
