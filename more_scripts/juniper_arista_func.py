# Functions - Juniper and Arista


# Place right below the master_list = [] code

def arista_dev(line)
        if noise in line:
            pass
        elif "SUCCESS" in line:
            # The split() func. will create a list of your string of text, 
            # splitting on empty spaces
            my_list = line.split()
            master_list.append(my_list[0])
            target_dev = my_list[0]
            dev_shape(target_dev)

        else:
            my_list = line.split()
            del my_list[-1]
            local_port = my_list[0]
            local_port = local_port.strip('"')
            neigh_port = my_list[2]
            lldp_neigh = my_list[1]
            lldp_link = "%s -->|%s <br><br>%s|%s\n" % (target_dev, local_port, neigh_port, lldp_neigh)
            lldp_diagram.write(lldp_link)

def juniper_dev(line)
        if noise in line:
            pass
        elif "SUCCESS" in line:
            # The split() func. will create a list of your string of text, 
            # splitting on empty spaces
            my_list = line.split()
            master_list.append(my_list[0])
            target_dev = my_list[0]
            dev_shape(target_dev)

        else:
            my_list = line.split()
            if my_list[-1] == '",':
                del my_list[-1]
            local_port = my_list[0]
            local_port = local_port.strip('"')
            neigh_port = my_list[1]
            lldp_neigh = my_list[-1]
            lldp_neigh = lldp_neigh.strip('",')        
            lldp_link = "%s -->|%s <br><br>%s|%s\n" % (target_dev, local_port, neigh_port, lldp_neigh)
            lldp_diagram.write(lldp_link)