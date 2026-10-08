---
name: network-administration
description: "Designs and operates the corporate network. Segmentation, remote access, wireless, DNS and addressing, and diagnosing network problems. Use this to segment a network, set up or fix remote access, diagnose intermittent connectivity, plan addressing or DNS, or assess whether the network's trust assumptions still hold."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: it-operations
metadata:
  hermes:
    category: it-operations
    tags: [it-operations, network, segmentation, dns, remote-access]
    related_skills: [chief-information-officer, systems-administration, access-and-identity, security-architecture-review]
---

# Network administration

The network is the substrate everything else assumes works. It gets attention when it fails and is
otherwise expected to be invisible, which is why its design debts persist for years.

## When to Use

- Segmenting a network.
- Setting up or fixing remote access.
- Diagnosing intermittent connectivity.
- Planning addressing or DNS.
- Assessing whether the network's trust assumptions still hold.

## Procedure

### Segment by trust, and mean it

A flat network means one compromised laptop reaches the finance server. Segmentation is the
highest-value structural control available and the most commonly deferred.

Separate at minimum: user devices, servers, management interfaces, guest, and anything unmanaged —
printers, cameras, building systems, contractor equipment. That last category is the recurring entry
point, because it is rarely patched and rarely owned.

Default deny between segments, and permit specific flows. Rules that accumulate without review become
an allow-all with extra steps; review them on a cadence and remove what no longer has a reason.

### Remote access

The perimeter stopped being a perimeter when the workforce and the workloads left it. Treat network
location as weak evidence of trust: being on the corporate network should not by itself grant access
to anything sensitive.

Prefer per-application access over full network access. A remote user needing one internal
application does not need a route to the entire internal estate, which is what a traditional VPN
grants by default.

Authentication and authorization policy belongs to `enterprise/security/access-and-identity`; this
skill implements the network path.

### DNS and addressing are load-bearing

DNS failure presents as everything being broken, which is why it is misdiagnosed for the first
twenty minutes of many incidents. Run it redundantly, monitor resolution from the client's
perspective rather than the server's, and keep records under change control.

Plan addressing with room to grow and document it. Overlapping private ranges is the problem that
surfaces years later during an acquisition or a site merge and is expensive at exactly that moment.

### Diagnose in layers

Work bottom-up and prove each layer before moving on: physical, then addressing, then routing, then
name resolution, then the application. Most misdiagnosis comes from starting at the application
because that is where the complaint originated.

## Pitfalls

- Running a flat network and relying on host controls alone.
- Granting full network access where application access would do.
- Treating network location as sufficient evidence of trust.
- Diagnosing from the application layer down.
- Letting inter-segment rules accumulate without review, which produces an allow-all with extra steps.
- Leaving unmanaged devices — printers, cameras, building systems — on a trusted segment.

## Verification

Intermittent problems are the hard case and need data over time, not a test at the moment someone
complains. Capture continuously at the affected point; a test that passes while nobody is suffering
proves nothing.

For a segmentation change, prove default-deny holds by testing a denied flow, not by reading the
rule. For DNS, monitor resolution from the client's perspective rather than the server's. Report the
layer at which the fault was proven, bottom-up.

## Related

- `enterprise/security/access-and-identity` — the authorization policy this implements a path for.
- `enterprise/it-operations/systems-administration` — the systems on the segments.
- `enterprise/security/security-architecture-review` — reviewing the trust assumptions themselves.
