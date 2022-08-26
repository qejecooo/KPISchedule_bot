async def get_normal_view(one_day):
    lessons = [one_day.first_lesson, one_day.second_lesson, one_day.third_lesson, one_day.fourth_lesson,
               one_day.fifth_lesson]

    one_day_schedule = []
    temp = 1
    for i in range(0, (len(lessons))):
        try:
            lessons[i + 1]
        except IndexError:
            if lessons[i] == "Вікно":
                continue
            if lessons[i] != "Вікно":
                lesson = str(temp) + "\ufe0f\u20e3: <code>" + lessons[i] + "</code>" + "\n"
                one_day_schedule.append(lesson)
                break

        if lessons[i] != "Вікно":
            lesson = str(temp) + "\ufe0f\u20e3: <code>" + lessons[i] + "</code>" + "\n"
            one_day_schedule.append(lesson)
        elif lessons[i] == "Вікно" and lessons[i+1] != "Вікно":
            lesson = str(temp) + "\ufe0f\u20e3: <code>" + lessons[i] + "</code>" + "\n"
            one_day_schedule.append(lesson)
        else:
            lesson = "\n"
            one_day_schedule.append(lesson)
        temp += 1

    text = ""
    for temp in range(0, 5):
        try:
            text += one_day_schedule[temp]
        except IndexError:
            continue
    return text
