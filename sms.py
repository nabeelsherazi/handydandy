class SMS_store:
    def __init__(self):
        self.inbox = []
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS, has_been_viewed=False):
        self.inbox.append((has_been_viewed, from_number, time_arrived, text_of_SMS))
    def message_count(self):
        return len(self.inbox)
    def get_unread_indexes(self):
        unread_indexes =  []
        for (ix, msg) in enumerate(self.inbox):
            if msg[0] == False:
                unread_indexes.append(ix)
        return unread_indexes
    def get_message(self, i):
        try:
            self.inbox[i] = (True, self.inbox[i][1], self.inbox[i][2], self.inbox[i][3])
            return self.inbox[i]
        except:
            return None
    def delete(self, i):
        try:
            self.inbox.pop(i)
        except:
            return None
    def clear(self):
        self.inbox = []

if __name__ == '__main__':
    import testsuite
    test_inbox = SMS_store()
    testsuite.test(test_inbox.inbox == [])
    testsuite.test(test_inbox.get_unread_indexes == [])
    test_inbox.add_new_arrival('2033066399', '9:02pm', "Hi, it's Jimmy!")
    test_inbox.add_new_arrival('2033066399', '9:03pm', "I'm just trying to chill!")
    testsuite.test(test_inbox.message_count == 2)
    testsuite.test(test_inbox.get_unread_indexes == [0, 1])
    testsuite.test(test_inbox.get_message(3) == None)
    testsuite.test(test_inbox.get_message(1) == (True, '2033066399', '9:03pm', "I'm just trying to chill!"))
    testsuite.test(test_inbox.get_unread_indexes == [0])
    testsuite.test(test_inbox.delete(3) == None)
    test_inbox.delete(1)
    testsuite.test(test_inbox.message_count == 1)
    test_inbox.clear()
    testsuite.test(test_inbox.inbox == [])
    input()
