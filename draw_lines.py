import os,matplotlib.pyplot as plt

def draw_plot_lines(methods):
    x = [(x+1)*0.1 for x in range(1,41)]
    ys=[]
    for method in methods:
        ys.append([])
        path = os.path.join(os.getcwd(), 'datas', method,'cars_MAE_file_in_'+str(method)+'.txt')
        file = open(path, 'r')
        line = file.readline()
        while line:
            line = line.split(':')
            ys[len(ys)-1].append(float(line[1]))
            line = file.readline()
        file.close()
    plt.plot(x, ys[0], label=methods[0], linewidth=3, color='r',marker='o',markerfacecolor='w', markersize=7)
    plt.plot(x, ys[1], label=methods[1], linewidth=3, color='b', marker='v', markerfacecolor='w', markersize=7)
    plt.plot(x, ys[2], label=methods[2], linewidth=3, color='y', marker='s', markerfacecolor='w', markersize=7)
    plt.show()

if __name__=='__main__':
    methods=['linprog','laplace','exponent']
    draw_plot_lines(methods)