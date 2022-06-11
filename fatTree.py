from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
 
class MyTopo(Topo):
 
    def __init__(self):
        super(MyTopo,self).__init__()
 
        #Marking the number of switch for per level
        k=4
        pod=k
        L1 = (pod//2)**2
        L2 = pod*pod//2
        L3 = L2
 
        #Starting create the switch
        c = []    #core switch
        a = []    #aggregate switch
        e = []    #edge switch
 
        #notice: switch label is a special data structure
        for i in range(L1):
            c_sw = self.addSwitch('c{}'.format(i+1))    #label from 1 to n,not start with 0
            c.append(c_sw)
 
        for i in range(L2):
            a_sw = self.addSwitch('a{}'.format(L1+i+1))
            a.append(a_sw)
 
        for i in range(L3):
            e_sw = self.addSwitch('e{}'.format(L1+L2+i+1))
            e.append(e_sw)
 
        #Starting create the link between switchs
        #first the first level and second level link
        for i in range(L1):
            c_sw=c[i]
            start=i%(pod//2)
            for j in range(pod):
                self.addLink(c_sw,a[start+j*(pod//2)])
 
        #second the second level and third level link
        for i in range(L2):
            group=i//(pod//2)
            for j in range(pod//2):
                self.addLink(a[i],e[group*(pod//2)+j])
 
        #Starting create the host and create link between switchs and hosts
        for i in range(L3):
            for j in range(2):
                hs = self.addHost('h{}'.format(i*2+j+1))
                self.addLink(e[i],hs)
 
 
topos = {"mytopo":(lambda:MyTopo())}
————————————————
版权声明：本文为CSDN博主「简vae」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_49588762/article/details/115296838
