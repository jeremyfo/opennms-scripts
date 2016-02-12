#events.py
This script displays the top 20 events stored in the events table of the OpenNMS database.
For more information please read ![OpenNMS Event Maintenance](http://opennms.org/wiki/Event_Maintenance)

##Requirements
```
pip install tabulate
pip install psycopg2 or yum install python-psycopg2
```
##Usage
It is important to keep track of your events table and to ensure OpenNMS performance especially as
your node count increases.

## TODO
- Add the ability to prune events from the events table

##Output
```
╒═══════════════════════════════════════════════════════════╤════════════════════╕
│ Event ID                                                  │ Number of Events   │
╞═══════════════════════════════════════════════════════════╪════════════════════╡
│ uei.opennms.org/internal/provisiond/nodeScanCompleted     │ 77242              │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/internal/linkd/nodeLinkDiscoveryStarted   │ 58704              │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/internal/linkd/nodeLinkDiscoveryCompleted │ 58344              │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/reinitializePrimarySnmpInterface    │ 56869              │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeUpdated                         │ 15008              │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/internal/rtc/subscribe                    │ 14000              │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/serviceDeleted                      │ 7387               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/dataCollectionSucceeded             │ 5730               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/dataCollectionFailed                │ 5598               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeGainedService                   │ 5441               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/threshold/highThresholdExceeded           │ 4310               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeLostService                     │ 4184               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeRegainedService                 │ 4146               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeDown                            │ 3140               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeUp                              │ 3105               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeCategoryMembershipChanged       │ 3103               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/IETF/OSPF/ospfIfStateChangeOtherDR        │ 2781               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/IETF/OSPF/ospfIfStateChange               │ 2683               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/interfaceDeleted                    │ 2122               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ uei.opennms.org/nodes/nodeGainedInterface                 │ 2028               │
├───────────────────────────────────────────────────────────┼────────────────────┤
│ Total Number of Events                                    │ 335925             │
╘═══════════════════════════════════════════════════════════╧════════════════════╛
```
