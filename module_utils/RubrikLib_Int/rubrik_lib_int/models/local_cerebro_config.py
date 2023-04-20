# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LocalCerebroConfig(Model):
    """LocalCerebroConfig.

    :param create_vmware_snapshot_job_in_memory_sem_shares: Maximum number of
     concurrent create snapshot jobs per node
    :type create_vmware_snapshot_job_in_memory_sem_shares: int
    :param max_concurrent_ingests_per_vm: Maximum number of ingest streams per
     virtual machine
    :type max_concurrent_ingests_per_vm: int
    :param expire_job_in_memory_sem_shares: Maximum number of concurrent
     expire jobs per node
    :type expire_job_in_memory_sem_shares: int
    :param mount_job_in_memory_sem_shares: Maximum number of concurrent mount
     jobs per node
    :type mount_job_in_memory_sem_shares: int
    :param unmount_job_in_memory_sem_shares: Maximum number of concurrent
     unmount jobs per node
    :type unmount_job_in_memory_sem_shares: int
    :param pull_mssql_log_replicate_job_in_memory_sem_shares: Maximum number
     of concurrent pull mssql log replicate jobs per node
    :type pull_mssql_log_replicate_job_in_memory_sem_shares: int
    :param pull_replicate_job_in_memory_sem_shares: Maximum number of
     concurrent pull replicate jobs per node
    :type pull_replicate_job_in_memory_sem_shares: int
    :param pull_replicate_requests_per_node: Maximum number of concurrent pull
     replicate requests from target cluster supported per node
    :type pull_replicate_requests_per_node: int
    :param refresh_remote_snapshots_in_memory_sem_shares: Maximum number of
     concurrent refresh remote snapshots jobs per node
    :type refresh_remote_snapshots_in_memory_sem_shares: int
    :param upload_job_in_memory_sem_shares: Maximum number of concurrent
     upload jobs per node
    :type upload_job_in_memory_sem_shares: int
    :param upload_index_job_in_memory_sem_shares: Maximum number of concurrent
     upload index jobs per node
    :type upload_index_job_in_memory_sem_shares: int
    :param snappable_index_job_in_memory_sem_shares: Maximum number of
     concurrent index jobs per node
    :type snappable_index_job_in_memory_sem_shares: int
    :param fileset_snapshot_job_in_memory_sem_shares: Maximum number of
     concurrent fileset snapshot jobs per node
    :type fileset_snapshot_job_in_memory_sem_shares: int
    :param mssql_snapshot_job_in_memory_sem_shares: Maximum number of
     concurrent mssql snapshot jobs per node
    :type mssql_snapshot_job_in_memory_sem_shares: int
    :param nutanix_snapshot_job_in_memory_sem_shares: Maximum number of
     concurrent create Nutanix snapshot jobs per node
    :type nutanix_snapshot_job_in_memory_sem_shares: int
    :param sqlite_cache_size_per_node_in_ki_b: Size of memory cache per SQLite
     process in kibibytes. These SQLite dbs are used for producing reports.
    :type sqlite_cache_size_per_node_in_ki_b: int
    :param hyperv_snapshot_job_in_memory_sem_shares: Maximum number of
     concurrent hyperv snapshot jobs per node
    :type hyperv_snapshot_job_in_memory_sem_shares: int
    :param hyperv_server_refresh_job_in_memory_sem_shares: Maximum number of
     concurrent hyperv server refresh jobs per node
    :type hyperv_server_refresh_job_in_memory_sem_shares: int
    :param delete_host_job_in_memory_sem_shares: Maximum number of concurrent
     delete host jobs per node
    :type delete_host_job_in_memory_sem_shares: int
    :param remote_cluster_service_min_worker_threads: Minimum number of worker
     threads in remote cluster server thread pool
    :type remote_cluster_service_min_worker_threads: int
    :param jfl_server_min_worker_threads: Minimum number of worker threads in
     jfl server thread pool
    :type jfl_server_min_worker_threads: int
    :param jfl_server_max_worker_threads: Maimum number of worker threads in
     jfl server thread pool
    :type jfl_server_max_worker_threads: int
    :param fileset_max_parallel_copy_streams_per_snapshot: Maximum number of
     MJF to Patch file streams per job.
    :type fileset_max_parallel_copy_streams_per_snapshot: int
    :param fileset_max_parallel_fetch_connections_per_snapshot: Maximum number
     of parallel fetch connections per snapshot.
    :type fileset_max_parallel_fetch_connections_per_snapshot: int
    :param fileset_nas_max_parallel_fetch_connections_per_snapshot: Maximum
     number of parallel fetch connections per snapshot on top of a NAS share.
    :type fileset_nas_max_parallel_fetch_connections_per_snapshot: int
    """

    _attribute_map = {
        'create_vmware_snapshot_job_in_memory_sem_shares': {'key': 'createVmwareSnapshotJobInMemorySemShares', 'type': 'int'},
        'max_concurrent_ingests_per_vm': {'key': 'maxConcurrentIngestsPerVm', 'type': 'int'},
        'expire_job_in_memory_sem_shares': {'key': 'expireJobInMemorySemShares', 'type': 'int'},
        'mount_job_in_memory_sem_shares': {'key': 'mountJobInMemorySemShares', 'type': 'int'},
        'unmount_job_in_memory_sem_shares': {'key': 'unmountJobInMemorySemShares', 'type': 'int'},
        'pull_mssql_log_replicate_job_in_memory_sem_shares': {'key': 'pullMssqlLogReplicateJobInMemorySemShares', 'type': 'int'},
        'pull_replicate_job_in_memory_sem_shares': {'key': 'pullReplicateJobInMemorySemShares', 'type': 'int'},
        'pull_replicate_requests_per_node': {'key': 'pullReplicateRequestsPerNode', 'type': 'int'},
        'refresh_remote_snapshots_in_memory_sem_shares': {'key': 'refreshRemoteSnapshotsInMemorySemShares', 'type': 'int'},
        'upload_job_in_memory_sem_shares': {'key': 'uploadJobInMemorySemShares', 'type': 'int'},
        'upload_index_job_in_memory_sem_shares': {'key': 'uploadIndexJobInMemorySemShares', 'type': 'int'},
        'snappable_index_job_in_memory_sem_shares': {'key': 'snappableIndexJobInMemorySemShares', 'type': 'int'},
        'fileset_snapshot_job_in_memory_sem_shares': {'key': 'filesetSnapshotJobInMemorySemShares', 'type': 'int'},
        'mssql_snapshot_job_in_memory_sem_shares': {'key': 'mssqlSnapshotJobInMemorySemShares', 'type': 'int'},
        'nutanix_snapshot_job_in_memory_sem_shares': {'key': 'nutanixSnapshotJobInMemorySemShares', 'type': 'int'},
        'sqlite_cache_size_per_node_in_ki_b': {'key': 'sqliteCacheSizePerNodeInKiB', 'type': 'int'},
        'hyperv_snapshot_job_in_memory_sem_shares': {'key': 'hypervSnapshotJobInMemorySemShares', 'type': 'int'},
        'hyperv_server_refresh_job_in_memory_sem_shares': {'key': 'hypervServerRefreshJobInMemorySemShares', 'type': 'int'},
        'delete_host_job_in_memory_sem_shares': {'key': 'deleteHostJobInMemorySemShares', 'type': 'int'},
        'remote_cluster_service_min_worker_threads': {'key': 'remoteClusterServiceMinWorkerThreads', 'type': 'int'},
        'jfl_server_min_worker_threads': {'key': 'jflServerMinWorkerThreads', 'type': 'int'},
        'jfl_server_max_worker_threads': {'key': 'jflServerMaxWorkerThreads', 'type': 'int'},
        'fileset_max_parallel_copy_streams_per_snapshot': {'key': 'filesetMaxParallelCopyStreamsPerSnapshot', 'type': 'int'},
        'fileset_max_parallel_fetch_connections_per_snapshot': {'key': 'filesetMaxParallelFetchConnectionsPerSnapshot', 'type': 'int'},
        'fileset_nas_max_parallel_fetch_connections_per_snapshot': {'key': 'filesetNasMaxParallelFetchConnectionsPerSnapshot', 'type': 'int'},
    }

    def __init__(self, create_vmware_snapshot_job_in_memory_sem_shares=None, max_concurrent_ingests_per_vm=None, expire_job_in_memory_sem_shares=None, mount_job_in_memory_sem_shares=None, unmount_job_in_memory_sem_shares=None, pull_mssql_log_replicate_job_in_memory_sem_shares=None, pull_replicate_job_in_memory_sem_shares=None, pull_replicate_requests_per_node=None, refresh_remote_snapshots_in_memory_sem_shares=None, upload_job_in_memory_sem_shares=None, upload_index_job_in_memory_sem_shares=None, snappable_index_job_in_memory_sem_shares=None, fileset_snapshot_job_in_memory_sem_shares=None, mssql_snapshot_job_in_memory_sem_shares=None, nutanix_snapshot_job_in_memory_sem_shares=None, sqlite_cache_size_per_node_in_ki_b=None, hyperv_snapshot_job_in_memory_sem_shares=None, hyperv_server_refresh_job_in_memory_sem_shares=None, delete_host_job_in_memory_sem_shares=None, remote_cluster_service_min_worker_threads=None, jfl_server_min_worker_threads=None, jfl_server_max_worker_threads=None, fileset_max_parallel_copy_streams_per_snapshot=None, fileset_max_parallel_fetch_connections_per_snapshot=None, fileset_nas_max_parallel_fetch_connections_per_snapshot=None):
        self.create_vmware_snapshot_job_in_memory_sem_shares = create_vmware_snapshot_job_in_memory_sem_shares
        self.max_concurrent_ingests_per_vm = max_concurrent_ingests_per_vm
        self.expire_job_in_memory_sem_shares = expire_job_in_memory_sem_shares
        self.mount_job_in_memory_sem_shares = mount_job_in_memory_sem_shares
        self.unmount_job_in_memory_sem_shares = unmount_job_in_memory_sem_shares
        self.pull_mssql_log_replicate_job_in_memory_sem_shares = pull_mssql_log_replicate_job_in_memory_sem_shares
        self.pull_replicate_job_in_memory_sem_shares = pull_replicate_job_in_memory_sem_shares
        self.pull_replicate_requests_per_node = pull_replicate_requests_per_node
        self.refresh_remote_snapshots_in_memory_sem_shares = refresh_remote_snapshots_in_memory_sem_shares
        self.upload_job_in_memory_sem_shares = upload_job_in_memory_sem_shares
        self.upload_index_job_in_memory_sem_shares = upload_index_job_in_memory_sem_shares
        self.snappable_index_job_in_memory_sem_shares = snappable_index_job_in_memory_sem_shares
        self.fileset_snapshot_job_in_memory_sem_shares = fileset_snapshot_job_in_memory_sem_shares
        self.mssql_snapshot_job_in_memory_sem_shares = mssql_snapshot_job_in_memory_sem_shares
        self.nutanix_snapshot_job_in_memory_sem_shares = nutanix_snapshot_job_in_memory_sem_shares
        self.sqlite_cache_size_per_node_in_ki_b = sqlite_cache_size_per_node_in_ki_b
        self.hyperv_snapshot_job_in_memory_sem_shares = hyperv_snapshot_job_in_memory_sem_shares
        self.hyperv_server_refresh_job_in_memory_sem_shares = hyperv_server_refresh_job_in_memory_sem_shares
        self.delete_host_job_in_memory_sem_shares = delete_host_job_in_memory_sem_shares
        self.remote_cluster_service_min_worker_threads = remote_cluster_service_min_worker_threads
        self.jfl_server_min_worker_threads = jfl_server_min_worker_threads
        self.jfl_server_max_worker_threads = jfl_server_max_worker_threads
        self.fileset_max_parallel_copy_streams_per_snapshot = fileset_max_parallel_copy_streams_per_snapshot
        self.fileset_max_parallel_fetch_connections_per_snapshot = fileset_max_parallel_fetch_connections_per_snapshot
        self.fileset_nas_max_parallel_fetch_connections_per_snapshot = fileset_nas_max_parallel_fetch_connections_per_snapshot