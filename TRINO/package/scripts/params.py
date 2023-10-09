#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from resource_management.libraries.script.script import Script

# config object that holds the configurations declared in the config xml file
config = Script.get_config()

node_properties = config['configurations']['node.properties']
jvm_config = config['configurations']['jvm.config']
config_properties = config['configurations']['config.properties']

t_resource_groups_json = config['configurations']['resource-groups.json']
t_resource_groups_properties = config['configurations']['resource-groups.properties']
t_session_property_config_json = config['configurations']['session-property-config.json']
t_session_property_config_properties = config['configurations']['session-property-config.properties']

# 如果是组件补充这几个
# select * from am.clusterconfig c where c.type_name in(
# 'resource-groups.json',
# 'resource-groups.properties',
# 'session-property-config.json',
# 'session-property-config.properties'
# )
# and config_id  in (
# select config_id from `am`.`serviceconfigmapping` a where a.service_config_id ='454'
# )
# select * from `am`.`serviceconfig` a where a.service_name ='Trino';
# select * from `am`.`serviceconfigmapping` a where a.service_config_id ='454';


connectors_to_add = config['configurations']['connectors.properties']['connectors.to.add']
connectors_to_delete = config['configurations']['connectors.properties']['connectors.to.delete']

daemon_control_script = '/etc/init.d/trino'
config_directory = '/etc/trino'

memory_configs = ['query.max-memory-per-node', 'query.max-memory']

host_info = config['clusterHostInfo']

host_level_params = config['ambariLevelParams']
java_home = '/usr/lib/jdk17.0.7'
