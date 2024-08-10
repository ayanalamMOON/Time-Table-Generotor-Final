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
            item['start_hr']), 'end_hr': int(item['end_hr'])}
        if item["duration"] != 1:
            consecutive_subjects[item["name"]] = item["duration"]

    if constraints['consecutive_subjects'][0] == "":
        diff_consecutive_mode = False

    if constraints['non_consecutive_subjects'][0] == "":
        diff_non_consecutive_mode = False

    time_slots, slot_time, mapping = get_time_slots(
        constraints_dict, start_times)
    
    Scheduling = Problem()
    Scheduling.addVariables(time_slots, subjects)

    def everySubject(*args):
        Timetable = args
        for subject in subjects:
            if Timetable.count(subject) != subject_hrs[subject]:
                return False
        return True
    
    def sameConsecutive(*args):
        Timetable = args
        for key, vakue in consecutive_subjects.items():
            index = Timetable.index(key)
            if (value == 2 index in end_time[2]) or (value == 3 and index in end_times[3]):
                return False
        return True
    
    def teacherTimings(*args):
        Timetable = args
        for index, value in enumerate(constraints['consecutive_subjects']):
            index = [i for i, letter in enumerate(
                Timetable) if letter == value]
            for i in indexs:
                if index == 0:
                    if i ==0:
                        if Timetable[i + 1] != constraints['consecutive_subjects'][1]:
                            return False
                    elif i == len(Timetable) - 1:
                        if Timetable[i - 1] != constraints['consecutive_subjects'][1]:
                            return False
                    else:
                        if Timetable[i + 1]  != constraints['consecutive_subjects'][1] or Timetable[i - 1] != constraints['consecutive_subjects'][1]:
                            return False
                
                else:
                    if i == 0:
                        if Timetable[i + 1] != constraints['consecutive_subjects'][0]:
                            return False
                    elif i == len(Timetable) - 1:
                        if Timetable[i - 1] != constraints['consecutive_subjects'][0]:
                            return False
                    else:
                        if Timetable[i + 1] != constraints['consecutive_subjects'][0] or Timetable[i - 1] != constraints['consecutive_subjects'][0]:
                            return False
            return True
        Scheduling.addConstraints(everySubject)

    




    
