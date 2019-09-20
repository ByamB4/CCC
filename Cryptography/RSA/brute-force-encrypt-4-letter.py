n = 22211149480575639993429030519324903433947913532364781040868963328192510711356813047019777682976897694523708823502748768149007288902843985412808705624398873301639600888468250478096471710461804856036409585519537946352413960371213677893523940481424813184421465313214067723492301317054407961642320909213358344993453825109139928083868146685834149311590508677641684185974469669019522897333475910002506624356655715375691861599282035176111228787146595035293770294934083506588432931535561733381730924617763450268288785249430304809062568532772866407535937947253602671915278827388538023000320823892308918791287865032550658101647
e = 65537
c = 17092019895398435490936645877681389522100314381280314137324590582626113380519883878346612680436149571504342956062627199254592419000136198748264157134720216337534802137245374257104787163473593768075381161119603573787923015405105192411372689756878820005036480013443173993126005361536816259899310244534769833694660355126920566669139672444357708161337389888825104348833002955918763849005061351140425567156148202269336347554989169075541289307981444741551677799416273481457219933391047628725337828725080079301570909831609401028488393457876225318163558871115320155827798534306397644894097358075465535794590825299057956641732

#!/usr/bin/env python
from Crypto.Util.number import inverse, bytes_to_long

for i in 'abcdefghijklmnopqrstuvwxyz0123456789':
    for j in 'abcdefghijklmnopqrstuvwxyz0123456789':
        for k in 'abcdefghijklmnopqrstuvwxyz0123456789':
            for l in 'abcdefghijklmnopqrstuvwxyz0123456789':
                m = 'nactf{' + i + j + k + l + '}'
                print m
                m = bytes_to_long(m)
                if pow(m, e, n) == c:
                    print m
                    quit()
