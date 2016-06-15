# Derived from ckite.thrift
namespace py raft

struct LogEntry {
	1: required i32 term;
	2: required i64 index;
	3: required binary command;
}

struct AppendEntries {
	1: required i32 term;
	2: required string leaderId; 
	3: optional i64 commitIndex = -1; 
	4: optional i64 prevLogIndex = -1;
	5: optional i32 prevLogTerm = -1;
	6: optional list<LogEntry> entries;
}

struct AppendEntriesResponse {
	1: required i32 term;
	2: required bool success;
}

struct RequestVote {
	1: required string memberId;
	2: required i32 term;
	3: optional i64 lastLogIndex = -1;
	4: optional i32 lastLogTerm = -1; 
}

struct RequestVoteResponse {
	1: required i32 currentTerm;
	2: required bool granted;
}

struct Snapshot {
	1: required binary stateMachineState;
	2: required i64 lastLogEntryIndex;
	3: required i32 lastLogEntryTerm;
	4: required binary membershipState;
}

struct InstallSnapshot {
	1: required i32 term;
	2: required string leaderId;
	3: required Snapshot snapshot;
}

struct InstallSnapshotResponse {
	1: required bool success;
}

struct JoinMember {
	1: required string memberId;
}

struct JoinMemberResponse {
	1: required bool success;
}

service RaftService {
	RequestVoteResponse sendRequestVote(1:RequestVote requestVote);
	AppendEntriesResponse sendAppendEntries(1:AppendEntries appendEntries);
	binary sendCommand(1:binary command);
	InstallSnapshotResponse sendInstallSnapshot(
          1:InstallSnapshot installSnapshot);
	JoinMemberResponse sendJoinMember(1:JoinMember memberId);
}
