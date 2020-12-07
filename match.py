import pandas as pd
import sys
import random
random.seed(11200416)


def create_reader_dictionary(df):
    readers = {}
    for i, row in df.iterrows():
        readers[row['Name']] = {'email': row['Email'], 'address1': row['Address1'],
                                'address2': row['Address2'], 'city': row['City'],
                                'state': row['State'], 'country': row['Country'],
                                'zip': row['Zip'], 'body':row['Body']}
            
    return readers


def create_mailing_dictionary(df):
    mailers = {}
    # populate dictionary with names and send and receive keys
    for i, row in df.iterrows():
        mailers[row['Name']] = {'send_to': None, 'receive_from': None}
    
    return mailers


def choose_random_reader(num_readers, already_received, current_reader_index, reader_names, reader_states):
    unavailable_indexes = already_received + [current_reader_index]
    # make list of available indexes not in the same state
    outofstate_indexes = []
    for j, state in enumerate(reader_states):
        if state != reader_states[current_reader_index]:
            outofstate_indexes.append(j)
    available_outofstate_indexes = [i for i in range(0, num_readers) if i not in unavailable_indexes and i in outofstate_indexes]
    # make list of all available indexes
    available_indexes = [i for i in range(0, num_readers) if i not in unavailable_indexes]
    print("AVAILABLE", available_indexes)
    if len(available_outofstate_indexes) > 0:
        rindex = random.choice(available_outofstate_indexes)
    elif len(available_indexes) > 0:
        # import pdb; pdb.set_trace()
        rindex = random.choice(available_indexes)
    else:
        print('END OF THE LINE, ASSIGN 0 BC START READER')
        rindex = 0
    
    return rindex
    

def assign_mailings(mailers, readers):
    # choose reader
    reader_names = list(readers.keys())
    reader_states = [readers[name]['state'] for name in reader_names]
    print(reader_states)
    start_reader = reader_names[0]
    current_reader = reader_names[0]
    print("START WITH", current_reader)

    # keep track of who has already sent or received
    already_sent = []
    already_received = [reader_names.index(start_reader)]

    # find the first receiver
    num_readers = len(reader_names)
    send_to_index = choose_random_reader(num_readers, already_sent, 0, reader_names, reader_states)
    print("First send to index", send_to_index)

    while send_to_index != 0:
        current_receiver = reader_names[send_to_index]
        print("Current reader", current_reader, "from", readers[current_reader]['state'])
        print("Current receiver", current_receiver, "from", readers[current_receiver]['state'])
        # assign current readers sent to and the receivers receive from
        mailers[current_reader]['send_to'] = current_receiver
        mailers[current_receiver]['receive_from'] = current_reader
        # add to the already sent and already received list
        if reader_names.index(current_reader) in already_sent:
            print('Already already sent', current_reader)
            import pdb; pdb.set_trace()
        else:
            already_sent.append(reader_names.index(current_reader))
        if send_to_index in already_received:
            print('Already already received', reader_names[send_to_index])
            import pdb; pdb.set_trace()
        else:
            already_received.append(send_to_index)
        # pick the current_receivers receiver and reassign receiver as reader
        current_reader = current_receiver
        send_to_index = choose_random_reader(num_readers, already_received, reader_names.index(current_reader), reader_names, reader_states)
        print('\n')
        print("Current send_to_index", send_to_index)

    current_receiver = reader_names[send_to_index]
    print("Current reader", current_reader, "from", readers[current_reader]['state'])
    print("Current receiver", current_receiver, "from", readers[current_receiver]['state'])
    # assign current readers sent to and the receivers receive from
    mailers[current_reader]['send_to'] = current_receiver
    mailers[current_receiver]['receive_from'] = current_reader
    # add to the already sent and already received list
    if reader_names.index(current_reader) in already_sent:
        print('Already already sent', current_reader)
    else:
        already_sent.append(reader_names.index(current_reader))
    if send_to_index in already_received:
        print('Already already received', reader_names[send_to_index])
    else:
        already_received.append(send_to_index)
    # pick the current_receivers receiver and reassign receiver as reader
    current_reader = current_receiver
    send_to_index = choose_random_reader(num_readers, already_received, reader_names.index(current_reader), reader_names, reader_states)
    print('\n')
    print("Current send_to_index", send_to_index)
    
    print(len(set(already_sent)))

    print(len(set(already_received)))
    
    return mailers


if __name__ == "__main__":
    df = pd.read_csv(sys.argv[-1])
    # create a list of reader objects
    readers = create_reader_dictionary(df)
    # make dictionary of who to send an receive books
    mailers = create_mailing_dictionary(df)

    mailers = assign_mailings(mailers, readers)

    print('\n\n\n')
    print(mailers)
