# N’KEMBA OpenShell Audit Ledger

This is the public index of the audit series. Titles are intentionally concise; the detailed experimental procedures and evidence classification remain the authoritative parts of each entry.

## #001–#050
#001 Policy & Evidence Boundary
#002 Evidence model boundary
#003 Proof versus observation
#004 Reproduction chain
#005 Audit-chain reproduction
#006 What Policy Prover proves
#007 Freeze version and evidence context
#008 Coverage boundary
#009 Audit versus enforce
#010 Destination-side proof of blocked request
#011 Log-chain loss
#012 Evidence integrity
#013 OCSF downgrade and attribution
#014 Temporal reconstruction
#015 Process attribution
#016 Process lineage
#017 Tool authority inheritance
#018 Policy hot reload
#019 Governance of policy changes
#020 Verification/approval race
#021 Approved versus loaded
#022 Invalid policy fail-closed
#023 Middleware failure mode
#024 Protocol coverage
#025 L4 versus L7
#026 Full versus read-only access
#027 Effective policy reconstruction
#028 Prover/effective-policy identity
#029 Policy change after proof
#030 Provider/credential context fingerprint
#031 Authorization versus model decision
#032 Full evidence chain
#033 Concurrent execution identity
#034 Process death and child continuation
#035 Exec boundary
#036 Authority inheritance
#037 Authority propagation depth
#038 OS identity versus executable identity
#039 Interpreter identity
#040 Script mutation
#041 Script filesystem protection
#042 Modifiable dependencies
#043 Dynamic code loading
#044 Filesystem protection degradation
#045 Policy Prover versus kernel enforcement
#046 Cryptographic policy binding
#047 Historical versus current effective policy
#048 Accepted versus validated versus loaded
#049 Loaded versus governed action
#050 Persistent connections and policy generation

## #051–#100
#051 Request start versus result time
#052 Concurrent executions
#053 Original process death
#054 PID reuse
#055 Same path, different binary
#056 Interpreter versus script identity
#057 Dependency changes
#058 Dynamic code identity
#059 Dynamic-code provenance
#060 Evidence integrity layers
#061 Silent evidence gap
#062 External storage failure
#063 Execution without evidence
#064 Fail-closed audit/control
#065 Denial with evidence unavailable
#066 Audit plus middleware denial
#067 WebSocket binary coverage
#068 WebSocket directionality
#069 HTTP response limitations
#070 Fail-open
#071 Fail-open stream state
#072 Middleware transformation and re-check
#073 Middleware order
#074 Middleware configuration identity
#075 Invalid middleware replacement
#076 Runtime middleware availability
#077 End-to-end middleware availability
#078 Capability negotiation
#079 Sandbox identity in middleware
#080 JWT token versus request identity
#081 Middleware before credential injection
#082 Header mutation and credential injection
#083 Ordered middleware chain
#084 Provider receipt
#085 External receipt
#086 Internal event to external receipt correlation
#087 Concurrent executions
#088 Process death
#089 PID reuse
#090 Same path, different binary
#091 Digest in enforcement versus audit evidence
#092 Interpreter/script mutation
#093 Script immutability
#094 Dependency integrity
#095 Dynamic code loading
#096 Dynamic-code provenance
#097 Dynamic-code TOCTOU
#098 Authorized network channel versus code provenance
#099 Same path/name, different dynamic content
#100 Transitive dependencies

## #101–#150
#101 Native library identity
#102 Library write protection
#103 Landlock best-effort versus hard requirement
#104 Policy Prover versus kernel enforcement
#105 Prover → policy → enforcement → behaviour
#106 Unsupported is not PASS
#107 Boundary versus enforcement mode
#108 Audit plus middleware DENY
#109 Transformation then policy re-check
#110 Middleware transformation chain
#111 Transformation-chain integrity
#112 Mixed concurrent events
#113 Same process, two operations
#114 PID reuse across operations
#115 Same path, new process/content
#116 Executable replacement in same session
#117 Runtime module identity
#118 Dynamic library containment
#119 Landlock best-effort degradation
#120 Finding versus consequence proof
#121 Configuration proof versus behaviour proof
#122 Static enforcement state
#123 Landlock enforcement identity
#124 Enforcement environment identity
#125 Base versus effective policy
#126 Provider change with unchanged base
#127 Provider change during in-flight operation
#128 Provider detach and existing process
#129 Persisted versus revoked
#130 Superseded changes
#131 Timed-out changes
#132 Mutation storage uncertainty
#133 Action during revocation uncertainty
#134 Pending-to-revoked race
#135 Base policy versus effective policy
#136 Provider A to Provider B
#137 Provider profile V1 to V2
#138 Detected but not applied
#139 Action before/after loaded boundary
#140 Existing process after config load
#141 Old process after credential revocation
#142 Forward before versus after revocation
#143 Revocation race
#144 Action before revocation, response after
#145 Concurrent executions across revocation
#146 Two operations in same process
#147 Completion versus causal order
#148 Concurrent channel loss
#149 Reconnect after loss
#150 Gateway restart and cursor continuity

## #151–#200
#151 Gateway replica change
#152 Duplicate observation versus execution
#153 Event identity versus operation identity
#154 Persistent connection versus request identity
#155 Policy reload on keep-alive
#156 Policy reload on WebSocket
#157 In-flight WebSocket message
#158 Fragmented WebSocket across reload
#159 Incomplete WebSocket message
#160 Payload limit and fail-open/closed
#161 Declared size versus consumed body
#162 Fail-open after payload limit
#163 Stage-specific middleware failure
#164 Transformation followed by re-evaluation
#165 Re-evaluation between successive transformations
#166 Later transformation cannot broaden authorization
#167 Intermediate result is not authorization shortcut
#168 Validated state passed to next stage
#169 Transformation continuity versus delivery
#170 Final authorized state versus destination state
#171 Last re-check versus final wire state
#172 Credential injection after re-check
#173 Credential availability versus destination authorization
#174 Network and credential barriers
#175 Network expansion does not expand credential scope
#176 Overlapping network rules do not compose credentials
#177 Explicit network deny
#178 Allow does not neutralize deny
#179 Provider-layer deny
#180 Provider allow versus base deny
#181 Provider deny versus broad base allow
#182 Global policy replacement
#183 Removing global policy
#184 Global deletion versus restored effective state
#185 Global deletion versus execution state
#186 Global policy effective timing
#187 Exact loaded revision identity
#188 Accepted revision superseded before load
#189 Loaded revision versus governed action
#190 Agent policy snapshot
#191 Stale agent policy snapshot
#192 Proposal versus authorized/effective policy
#193 Proposal context re-check
#194 Proposal staleness
#195 Pending proposal invalidation
#196 Old risk result
#197 Recheck-window boundary
#198 Fresh approval authority check
#199 Approved candidate identity
#200 Approved versus loaded

## #201–#250
#201 Loaded revision versus approved revision
#202 Loaded versus concrete action
#203 Loaded versus effective authority at action time
#204 Prover PASS versus auto-approval
#205 Prover coverage versus risk coverage
#206 Context-bound risk result
#207 Presented versus valid proposal
#208 Proposal identity versus candidate identity
#209 Approval changes other proposals
#210 Old versus current risk result
#211 Recheck window versus validity window
#212 Bulk approval is not one proof
#213 Bulk operation versus bulk evidence
#214 Security-flagged bulk approval
#215 Partial batch success
#216 Skipped versus rejected versus approved
#217 Rejection identity and motive
#218 Rejected proposal and iteration history
#219 Corrected proposal linkage
#220 Validation result version binding
#221 Validation versus enforcement
#222 Agent current policy snapshot
#223 Agent snapshot TOCTOU
#224 Current versus historical state
#225 Historical revision versus historical governance
#226 Historical policy versus complete authority
#227 Provider context for historical authority
#228 Shared provider profile
#229 Provider sync divergence
#230 Provider update versus effective authority
#231 Ready versus all processes updated
#232 Ready versus existing-process credential state
#233 Credential rotation versus process rotation
#234 Stable credential handle versus secret value
#235 Credential authorization epoch
#236 Action started before revocation
#237 Concurrent authorization epochs
#238 Absence of evidence versus absence of action
#239 OUT_OF_RANGE and recovery
#240 Gateway restart and observation continuity
#241 Gateway restart during execution
#242 External execution proof versus temporal position
#243 External receipt versus internal attribution
#244 Same request versus same execution
#245 Same request versus same authorization
#246 Same process, two operations
#247 Partial identity with an evidence gap
#248 Internal execution versus external effect
#249 External receipt without internal authorship
#250 Authorized state versus delivered state

## #251–#284
#251 Credential injection and final wire proof
#252 Transformation chain and delivery
#253 Policy change between transformations
#254 Policy effective during middleware execution
#255 Policy generation and connection continuity
#256 WebSocket policy generation
#257 In-flight WebSocket action
#258 Fragmented WebSocket across policy change
#259 Fragment versus operation
#260 Payload limit versus session
#261 Capacity/failure versus policy denial
#262 Stage-specific middleware failure
#263 Fail-open after transformation
#264 Multiple transformed policy states
#265 Last re-check versus final wire
#266 External proof of final request
#267 External receipt versus internal authorship
#268 JWT/event/sandbox identity boundaries
#269 OCSF event versus execution
#270 Missing event with external receipt
#271 OUT_OF_RANGE recovery boundary
#272 Gateway restart versus execution continuity
#273 Execution across observation boundary
#274 Gateway restart and sandbox lifecycle
#275 Current policy after restart versus historical policy
#276 Provider altered with unchanged base policy
#277 Divergence in effective provider state between sandboxes
#278 Two processes with different provider generations
#279 Revocation with an old process still running
#280 Action forwarded before revocation, response after
#281 Concurrent operations crossing revocation
#282 External receipt without internal event
#283 Internal evidence without external receipt
#284 Same content, two executions

## Publication status

The ledger is a research/audit record, not a certification. Entries marked as documentary are grounded in public NVIDIA documentation; proposed runtime experiments remain explicitly experimental until executed and archived with raw evidence.

## Primary source

NVIDIA OpenShell documentation: https://docs.nvidia.com/openshell/
