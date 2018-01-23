#!/usr/bin/env python3


def run():

    packages = {}
    with open('packages') as f:
        for line in f.readlines():
            try:
                g, a, v = line.split(',')
            except ValueError:
                # ?
                continue
            ga = g + ',' + a
            v = v.strip()
            if packages.get(ga) is None:
                packages[ga] = [v]
            else:
                packages[ga].append(v)

    with open('packages', 'w') as f:
        for package in packages:
            f.write(package + ',')
            for v in packages[package]:
                f.write(v+' ')
            f.write('\n')


if __name__ == '__main__':
    run()
