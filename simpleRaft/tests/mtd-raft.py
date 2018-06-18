#!/usr/bin/env python3

import unittest
import sys

sys.path.append('..')

from boards.memory_board import MemoryBoard
from messages.request_addr_change import RequestAddrChangeMessage
from messages.append_entries import AppendEntriesMessage
from messages.request_vote import RequestVoteMessage
from messages.base import BaseMessage
from servers.server import ZeroMQServer
from states.leader import Leader
from states.follower import Follower

N = 5


class TestRaft(unittest.TestCase):

    # helper function, output logs
    def printLogs(self):
        print("LOGS:")
        for i in range(0,N-1):
            print("Neighbor %d:" % i, self.leader._neighbors[i]._log)

        print("Leader:", self.leader._log)

    @classmethod
    def setUpClass(self):
        self.servers = []
        for i in range(N):
            if i == 0:
                state = Leader()
            else:
                state = Follower()
            s = ZeroMQServer("S%d" % i, state, [], MemoryBoard(), [], 6666 + i)
            if (i == 0):
                self.leader = s
            self.servers.append(s)
        for i in range(N):
            me = self.servers[i]
            neighbors = [n for n in self.servers if n != me]
            me.set_neighbors(neighbors)

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        for i in range(N):
            self.servers[i]._state.__init__()
            self.servers[i]._messageBoard.__init__()
            self.servers[i]._log.clear()
            self.servers[i]._clear()

    def _perform_hearbeat(self):
        self.leader._state._send_heart_beat()
        # get messages from followers' message boards and act accordingly
        for i in self.leader._neighbors:
            i.on_message(i._messageBoard.get_message())

        # get messages from leader's message board and act accordingly
        for i in self.leader._messageBoard._board:
            self.leader.on_message(i)

    def test_heartbeat(self):
        self._perform_hearbeat()
        expected = dict(('S%d' % i, 0) for i in range(1, N))    # dict with values 'Si':0 for every i != leader
        self.assertEqual(expected, self.leader._state._nextIndexes)

    def test_mtd(self):
        print("\n\n***test_mtd***")
        print("---perform_heartbeat---")
        self._perform_hearbeat()

        self.leader._log.append({"term": 1, "value": "10.0.1.1"})

        # form and add typical entry
        msg = AppendEntriesMessage(0, None, 1, {
            "prevLogIndex": 0,
            "prevLogTerm": 0,
            "leaderCommit": 0,
            "entries": [{"term": 1, "value": "10.0.1.1"}]})

        self.leader.send_message(msg)

        for i in self.leader._neighbors:
            i.on_message(i._messageBoard.get_message())

        # for i in self.leader._neighbors:
        #     self.assertEqual([{"term": 1, "value": 100}], i._log)

        self.printLogs()

        # print("---perform_heartbeat---")
        # self._perform_hearbeat()

        self.leader._log.append({"term": 1, "value": "10.0.1.2"})

        # form and add another typical entry
        msg = AppendEntriesMessage(0, None, 1, {
            "prevLogIndex": 0,
            "prevLogTerm": 1,
            "leaderCommit": 0,
            "entries": [{"term": 1, "value": "10.0.1.2"}]})

        self.leader.send_message(msg)

        for i in self.leader._neighbors:
            i.on_message(i._messageBoard.get_message())

        # for i in self.leader._neighbors:
        #     self.assertEqual([{"term": 1, "value": 100.100.100.100}, {"term": 1, "value": 200}], i._log)

        self.printLogs()

        print("---Regular entries added. Request change---")

        # self._perform_hearbeat()

        self.leader._log.append({"term": 1, "value": "hashthis"})
        # attack detected, leader requests address change via AppendEntries
        # value of 999 signifies an attack was detected
        msg = AppendEntriesMessage(0, None, 1, {
            "prevLogIndex": 0,
            "prevLogTerm": 1,
            "leaderCommit": 1,
            "entries": [{"term": 1, "value": 999, "addr": "hashthis"}]
        });

        self.leader.send_message(msg)

        for i in self.leader._neighbors:
            i.on_message(i._messageBoard.get_message())

        # for i in self.leader._neighbors:
        #     self.assertEqual([{"term": 1, "value": 100}, {"term": 1, "value": 200}, {"term": 1, "value": 999}], i._log)

        self.printLogs()


if __name__ == '__main__':
    unittest.main()
