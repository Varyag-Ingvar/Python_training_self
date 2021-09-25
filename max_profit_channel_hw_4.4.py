stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# max_val = max(stats.items()) # вернёт и ключ и значение в виде кортежа ('yandex', 120)
#
# print(max_val[0])  # вернёт только yandex






m_channel = ''
for channel in stats.keys():
    if stats[channel]> stats.get(m_channel,0):
        m_channel = channel

print(m_channel)


#
# k_list = []
# v_list = []
#
# for k,v in stats.items():
#     k_list.append(k)
#     v_list.append(v)
#
# print(k_list)
# print(v_list)
#
# t_list = (list(zip(k_list, v_list)))
# print(t_list)
# max_val = max(t_list)
# print(max_val[0])
# #
# #
# # # print(list(zip((stats.values(), stats.keys()))))
# # # max_v = max(zip(stats.values(), stats.keys()))
# # # print(max_v[1])
# #
# # print(max(stats))
#
# #
# # d = {'y': 96, 'i': 98, 'p': 110, 'z': 100}
# # print(max(d))

