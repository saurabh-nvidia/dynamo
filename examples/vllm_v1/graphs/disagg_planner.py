# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
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

from components.frontend import Frontend
from components.simple_load_balancer import SimpleLoadBalancer
from components.worker import VllmDecodeWorker, VllmPrefillWorker

from dynamo.planner.planner_sla import Planner
from dynamo.planner.prometheus import Prometheus

load_balancer = Frontend.link(SimpleLoadBalancer)
load_balancer.link(VllmPrefillWorker)
load_balancer.link(VllmDecodeWorker)

Frontend.link(Planner)
Frontend.link(Prometheus)
