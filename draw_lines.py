import os,matplotlib.pyplot as plt

def draw_plot_lines(methods):
    x = [(x+1)*0.1/20 for x in range(1,41)]
    ys=[]
    for method in methods:
        if method == 'linprog':
            deltas = [1.1, 1.2, 1.3, 1.4, 1.5]
            for delta in deltas:
                ys.append([])
                path = os.path.join(os.getcwd(), 'datas', method,'cars_MAE_file_in_'+str(method)+str(delta)+'.txt')
                file = open(path, 'r')
                line = file.readline()
                while line:
                    line = line.split(':')
                    ys[len(ys)-1].append(float(line[1]))
                    line = file.readline()
                file.close()
        else:
            ys.append([])
            path = os.path.join(os.getcwd(), 'datas', method, 'cars_MAE_file_in_' + str(method) + '.txt')
            file = open(path, 'r')
            line = file.readline()
            while line:
                line = line.split(':')
                ys[len(ys) - 1].append(float(line[1]))
                line = file.readline()
            file.close()
    lines=[]
    for i in range(len(ys)-1):
        L,=plt.plot(x, ys[i], label='EGeoIndis'+' $\delta=1.'+str(i+1)+'$', linewidth=3, color=[i*0.2]*3,marker='o',markerfacecolor='w', markersize=7)
        lines.append(L)
    L,=plt.plot(x, ys[len(ys)-1], label='Laplace', linewidth=3, color='r', marker='v', markerfacecolor='w', markersize=7)
    lines.append(L)
    #plt.plot(x, ys[2], label=methods[2], linewidth=3, color='y', marker='s', markerfacecolor='w', markersize=7)
    font = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 18,
             }
    plt.xlabel('$\epsilon$',font)
    plt.ylabel('MAER',font)
    plt.legend(handles=lines,prop=font)
    plt.show()

if __name__=='__main__':
    methods=['linprog','laplace']
    draw_plot_lines(methods)