# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GlobalForgeConfig(Model):
    """GlobalForgeConfig.

    :param proxy_configuration: Proxy Configuration
    :type proxy_configuration: str
    :param log4j_monitor_interval_seconds: monitorInterval attribute in
     log4j2.xml
    :type log4j_monitor_interval_seconds: int
    :param log4j_trace_loggers: Comma separated list of logger names to enable
     TRACE level logging. For example
     akka.io.TcpListener,com.scaledata.metadatastore.CassandraEntityManager,com.scaledata.vmclient.vmware.impl.VmwareToolImpl,com.scaledata.util.package,com.amazonaws
    :type log4j_trace_loggers: str
    :param syslog_app_name: App name to use for messages sent to remote syslog
     servers
    :type syslog_app_name: str
    :param syslog_format: Format to use for messages sent to remote syslog
     servers
    :type syslog_format: str
    :param syslog_host: Syslog server hostname or IP address
    :type syslog_host: str
    :param syslog_mdc_id: MDC ID to use for messages sent to remote syslog
     servers
    :type syslog_mdc_id: str
    :param syslog_msg_id: MSGID to use for messages sent to remote syslog
     servers
    :type syslog_msg_id: str
    :param syslog_new_line: Whether to send a new line with each remote syslog
     message
    :type syslog_new_line: bool
    :param syslog_port: Syslog server port
    :type syslog_port: int
    :param syslog_protocol: Syslog server protocol
    :type syslog_protocol: str
    :param disk_checker_mount_partitions_rate: Mount device partitions every
     this many iterations in the DiskChecker
    :type disk_checker_mount_partitions_rate: int
    :param disk_checker_partition_mount_rate: Mount device partitions every so
     many iterations in the DiskChecker
    :type disk_checker_partition_mount_rate: int
    :param brik_aware_conversion_enabled: Automatically convert nodes to be
     Brik Aware when necessary
    :type brik_aware_conversion_enabled: bool
    :param verify_brik_serials_on_add: Sanity check brik serials while adding
     a node
    :type verify_brik_serials_on_add: bool
    :param blink_led_for_disk_status: Change LED state based on disk status
    :type blink_led_for_disk_status: bool
    :param block_cassandra_for_removed_nodes: Block Cassandra traffic to and
     from removed nodes using iptables
    :type block_cassandra_for_removed_nodes: bool
    :param auto_remove_job_in_memory_sem_shares: Maximum number of auto remove
     jobs per node
    :type auto_remove_job_in_memory_sem_shares: int
    :param auto_remove_dead_node_job_frequency_in_minutes: Frequency of job to
     automatically remove dead node
    :type auto_remove_dead_node_job_frequency_in_minutes: int
    :param auto_remove_max_allowed: Number of auto node removals the cluster
     is allowed to perform
    :type auto_remove_max_allowed: int
    :param auto_remove_dead_node_resurrection_window_multiplier: How stale
     should a node be before we auto remove it
    :type auto_remove_dead_node_resurrection_window_multiplier: int
    :param auto_remove_min_nodes_at_start: How many nodes should a cluster
     have for auto remove to run
    :type auto_remove_min_nodes_at_start: int
    :param auto_install_on_add_enabled: Is auto install enabled on node add
    :type auto_install_on_add_enabled: bool
    :param auto_install_min_version: Minimum supported version for auto
     install
    :type auto_install_min_version: str
    :param subrange_repair_on_node_removal: Whether to perform subrange repair
     on node removal
    :type subrange_repair_on_node_removal: bool
    :param cassandra_repair_num_threads: Num threads parameter passed to
     cassandra for repair
    :type cassandra_repair_num_threads: int
    :param cassandra_compaction_default_throughput: Default Cassandra
     compaction throughput in MBps
    :type cassandra_compaction_default_throughput: int
    :param cassandra_compaction_repair_throughput: Cassandra compaction
     throughput during a repair operation
    :type cassandra_compaction_repair_throughput: int
    :param cassandra_stream_default_throughput: Default Cassandra stream
     throughput in Mbps
    :type cassandra_stream_default_throughput: int
    :param cassandra_stream_repair_throughput: Cassandra stream throughput
     during a repair operation
    :type cassandra_stream_repair_throughput: int
    """

    _attribute_map = {
        'proxy_configuration': {'key': 'proxyConfiguration', 'type': 'str'},
        'log4j_monitor_interval_seconds': {'key': 'log4jMonitorIntervalSeconds', 'type': 'int'},
        'log4j_trace_loggers': {'key': 'log4jTraceLoggers', 'type': 'str'},
        'syslog_app_name': {'key': 'syslogAppName', 'type': 'str'},
        'syslog_format': {'key': 'syslogFormat', 'type': 'str'},
        'syslog_host': {'key': 'syslogHost', 'type': 'str'},
        'syslog_mdc_id': {'key': 'syslogMdcId', 'type': 'str'},
        'syslog_msg_id': {'key': 'syslogMsgId', 'type': 'str'},
        'syslog_new_line': {'key': 'syslogNewLine', 'type': 'bool'},
        'syslog_port': {'key': 'syslogPort', 'type': 'int'},
        'syslog_protocol': {'key': 'syslogProtocol', 'type': 'str'},
        'disk_checker_mount_partitions_rate': {'key': 'diskCheckerMountPartitionsRate', 'type': 'int'},
        'disk_checker_partition_mount_rate': {'key': 'diskCheckerPartitionMountRate', 'type': 'int'},
        'brik_aware_conversion_enabled': {'key': 'brikAwareConversionEnabled', 'type': 'bool'},
        'verify_brik_serials_on_add': {'key': 'verifyBrikSerialsOnAdd', 'type': 'bool'},
        'blink_led_for_disk_status': {'key': 'blinkLedForDiskStatus', 'type': 'bool'},
        'block_cassandra_for_removed_nodes': {'key': 'blockCassandraForRemovedNodes', 'type': 'bool'},
        'auto_remove_job_in_memory_sem_shares': {'key': 'autoRemoveJobInMemorySemShares', 'type': 'int'},
        'auto_remove_dead_node_job_frequency_in_minutes': {'key': 'autoRemoveDeadNodeJobFrequencyInMinutes', 'type': 'int'},
        'auto_remove_max_allowed': {'key': 'autoRemoveMaxAllowed', 'type': 'int'},
        'auto_remove_dead_node_resurrection_window_multiplier': {'key': 'autoRemoveDeadNodeResurrectionWindowMultiplier', 'type': 'int'},
        'auto_remove_min_nodes_at_start': {'key': 'autoRemoveMinNodesAtStart', 'type': 'int'},
        'auto_install_on_add_enabled': {'key': 'autoInstallOnAddEnabled', 'type': 'bool'},
        'auto_install_min_version': {'key': 'autoInstallMinVersion', 'type': 'str'},
        'subrange_repair_on_node_removal': {'key': 'subrangeRepairOnNodeRemoval', 'type': 'bool'},
        'cassandra_repair_num_threads': {'key': 'cassandraRepairNumThreads', 'type': 'int'},
        'cassandra_compaction_default_throughput': {'key': 'cassandraCompactionDefaultThroughput', 'type': 'int'},
        'cassandra_compaction_repair_throughput': {'key': 'cassandraCompactionRepairThroughput', 'type': 'int'},
        'cassandra_stream_default_throughput': {'key': 'cassandraStreamDefaultThroughput', 'type': 'int'},
        'cassandra_stream_repair_throughput': {'key': 'cassandraStreamRepairThroughput', 'type': 'int'},
    }

    def __init__(self, proxy_configuration=None, log4j_monitor_interval_seconds=None, log4j_trace_loggers=None, syslog_app_name=None, syslog_format=None, syslog_host=None, syslog_mdc_id=None, syslog_msg_id=None, syslog_new_line=None, syslog_port=None, syslog_protocol=None, disk_checker_mount_partitions_rate=None, disk_checker_partition_mount_rate=None, brik_aware_conversion_enabled=None, verify_brik_serials_on_add=None, blink_led_for_disk_status=None, block_cassandra_for_removed_nodes=None, auto_remove_job_in_memory_sem_shares=None, auto_remove_dead_node_job_frequency_in_minutes=None, auto_remove_max_allowed=None, auto_remove_dead_node_resurrection_window_multiplier=None, auto_remove_min_nodes_at_start=None, auto_install_on_add_enabled=None, auto_install_min_version=None, subrange_repair_on_node_removal=None, cassandra_repair_num_threads=None, cassandra_compaction_default_throughput=None, cassandra_compaction_repair_throughput=None, cassandra_stream_default_throughput=None, cassandra_stream_repair_throughput=None):
        self.proxy_configuration = proxy_configuration
        self.log4j_monitor_interval_seconds = log4j_monitor_interval_seconds
        self.log4j_trace_loggers = log4j_trace_loggers
        self.syslog_app_name = syslog_app_name
        self.syslog_format = syslog_format
        self.syslog_host = syslog_host
        self.syslog_mdc_id = syslog_mdc_id
        self.syslog_msg_id = syslog_msg_id
        self.syslog_new_line = syslog_new_line
        self.syslog_port = syslog_port
        self.syslog_protocol = syslog_protocol
        self.disk_checker_mount_partitions_rate = disk_checker_mount_partitions_rate
        self.disk_checker_partition_mount_rate = disk_checker_partition_mount_rate
        self.brik_aware_conversion_enabled = brik_aware_conversion_enabled
        self.verify_brik_serials_on_add = verify_brik_serials_on_add
        self.blink_led_for_disk_status = blink_led_for_disk_status
        self.block_cassandra_for_removed_nodes = block_cassandra_for_removed_nodes
        self.auto_remove_job_in_memory_sem_shares = auto_remove_job_in_memory_sem_shares
        self.auto_remove_dead_node_job_frequency_in_minutes = auto_remove_dead_node_job_frequency_in_minutes
        self.auto_remove_max_allowed = auto_remove_max_allowed
        self.auto_remove_dead_node_resurrection_window_multiplier = auto_remove_dead_node_resurrection_window_multiplier
        self.auto_remove_min_nodes_at_start = auto_remove_min_nodes_at_start
        self.auto_install_on_add_enabled = auto_install_on_add_enabled
        self.auto_install_min_version = auto_install_min_version
        self.subrange_repair_on_node_removal = subrange_repair_on_node_removal
        self.cassandra_repair_num_threads = cassandra_repair_num_threads
        self.cassandra_compaction_default_throughput = cassandra_compaction_default_throughput
        self.cassandra_compaction_repair_throughput = cassandra_compaction_repair_throughput
        self.cassandra_stream_default_throughput = cassandra_stream_default_throughput
        self.cassandra_stream_repair_throughput = cassandra_stream_repair_throughput
