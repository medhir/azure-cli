# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sql mi link update",
)
class Update(AAZCommand):
    """Update a distributed availability group between Sql On-Prem and Sql Managed Instance.
    """

    _aaz_info = {
        "version": "2022-02-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.sql/managedinstances/{}/distributedavailabilitygroups/{}", "2022-02-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.distributed_availability_group_name = AAZStrArg(
            options=["-n", "--name", "--distributed-availability-group-name"],
            help="Distributed availability group name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.managed_instance_name = AAZStrArg(
            options=["--mi", "--instance-name", "--managed-instance", "--managed-instance-name"],
            help="Name of the managed instance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.primary_availability_group_name = AAZStrArg(
            options=["--primary-ag", "--primary-availability-group-name"],
            arg_group="Properties",
            help="Primary availability group name",
            nullable=True,
        )
        _args_schema.replication_mode = AAZStrArg(
            options=["--replication-mode"],
            arg_group="Properties",
            help="Replication mode of a distributed availability group. Parameter will be ignored during link creation.",
            nullable=True,
            enum={"Async": "Async", "Sync": "Sync"},
        )
        _args_schema.secondary_availability_group_name = AAZStrArg(
            options=["--secondary-ag", "--secondary-availability-group-name"],
            arg_group="Properties",
            help="Secondary availability group name",
            nullable=True,
        )
        _args_schema.source_endpoint = AAZStrArg(
            options=["--source-endpoint"],
            arg_group="Properties",
            help="Source endpoint",
            nullable=True,
        )
        _args_schema.target_database = AAZStrArg(
            options=["--target-db", "--target-database"],
            arg_group="Properties",
            help="Name of the target database",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.DistributedAvailabilityGroupsGet(ctx=self.ctx)()
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        yield self.DistributedAvailabilityGroupsCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DistributedAvailabilityGroupsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/distributedAvailabilityGroups/{distributedAvailabilityGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "distributedAvailabilityGroupName", self.ctx.args.distributed_availability_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-02-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_distributed_availability_group_read(cls._schema_on_200)

            return cls._schema_on_200

    class DistributedAvailabilityGroupsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/distributedAvailabilityGroups/{distributedAvailabilityGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "distributedAvailabilityGroupName", self.ctx.args.distributed_availability_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-02-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _build_schema_distributed_availability_group_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("primaryAvailabilityGroupName", AAZStrType, ".primary_availability_group_name")
                properties.set_prop("replicationMode", AAZStrType, ".replication_mode")
                properties.set_prop("secondaryAvailabilityGroupName", AAZStrType, ".secondary_availability_group_name")
                properties.set_prop("sourceEndpoint", AAZStrType, ".source_endpoint")
                properties.set_prop("targetDatabase", AAZStrType, ".target_database")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_distributed_availability_group_read = None


def _build_schema_distributed_availability_group_read(_schema):
    global _schema_distributed_availability_group_read
    if _schema_distributed_availability_group_read is not None:
        _schema.id = _schema_distributed_availability_group_read.id
        _schema.name = _schema_distributed_availability_group_read.name
        _schema.properties = _schema_distributed_availability_group_read.properties
        _schema.type = _schema_distributed_availability_group_read.type
        return

    _schema_distributed_availability_group_read = AAZObjectType()

    distributed_availability_group_read = _schema_distributed_availability_group_read
    distributed_availability_group_read.id = AAZStrType(
        flags={"read_only": True},
    )
    distributed_availability_group_read.name = AAZStrType(
        flags={"read_only": True},
    )
    distributed_availability_group_read.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    distributed_availability_group_read.type = AAZStrType(
        flags={"read_only": True},
    )

    properties = _schema_distributed_availability_group_read.properties
    properties.distributed_availability_group_id = AAZStrType(
        serialized_name="distributedAvailabilityGroupId",
        flags={"read_only": True},
    )
    properties.last_hardened_lsn = AAZStrType(
        serialized_name="lastHardenedLsn",
        flags={"read_only": True},
    )
    properties.link_state = AAZStrType(
        serialized_name="linkState",
        flags={"read_only": True},
    )
    properties.primary_availability_group_name = AAZStrType(
        serialized_name="primaryAvailabilityGroupName",
    )
    properties.replication_mode = AAZStrType(
        serialized_name="replicationMode",
    )
    properties.secondary_availability_group_name = AAZStrType(
        serialized_name="secondaryAvailabilityGroupName",
    )
    properties.source_endpoint = AAZStrType(
        serialized_name="sourceEndpoint",
    )
    properties.source_replica_id = AAZStrType(
        serialized_name="sourceReplicaId",
        flags={"read_only": True},
    )
    properties.target_database = AAZStrType(
        serialized_name="targetDatabase",
    )
    properties.target_replica_id = AAZStrType(
        serialized_name="targetReplicaId",
        flags={"read_only": True},
    )

    _schema.id = _schema_distributed_availability_group_read.id
    _schema.name = _schema_distributed_availability_group_read.name
    _schema.properties = _schema_distributed_availability_group_read.properties
    _schema.type = _schema_distributed_availability_group_read.type


__all__ = ["Update"]
