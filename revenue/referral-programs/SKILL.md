---
name: referral-programs
description: "Designs referral and affiliate programs. Incentive structure, mechanics, timing, fraud control, and word-of-mouth amplification. Use this to build a referral or affiliate program, diagnose one that is not producing, decide what incentive to offer, or judge whether referral is a realistic channel for a product."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: revenue
metadata:
  hermes:
    category: revenue
    tags: [revenue, referral, affiliate, incentives, fraud]
    related_skills: [retention, activation, partnership-marketing, chief-revenue-officer]
---

# Referral programs

Referral programs amplify existing word of mouth. They do not create it.

## When to Use

- Building a referral or affiliate program.
- Diagnosing one that is not producing.
- Deciding what incentive to offer.
- Judging whether referral is a realistic channel for a product.

## Prerequisites

Qualify the channel first. If customers are not already recommending you unprompted, a program will
not produce them — it will produce incentive-motivated signups that churn. Check first: is anyone
referring today, and what do they say when they do?

## Procedure

### Incentive design

- **Two-sided beats one-sided** in most cases. It gives the referrer something to offer rather than
  something to gain, which removes the awkwardness that stops most referrals.
- **Match the reward to the product's value**, not to a round number. Account credit usually
  outperforms cash, and costs less.
- **Reward the outcome you want.** Paying on signup buys signups; paying on a retained, activated
  customer buys customers.
- **Cash rewards attract fraud**, and fraud scales faster than the program does. Budget for
  detection before launch, not after.

### Mechanics

The referral has to be effortless at the moment of enthusiasm, which means the ask must appear right
after a success moment — not in a settings page nobody visits.

- One-click share with pre-written text the referrer can edit.
- A link that works everywhere and survives being pasted into any app.
- Visible status: who was invited, what stage they reached, what has been earned. Ambiguity kills
  repeat referrals.
- The referred person's experience must be better than a normal signup. Landing them on the generic
  homepage wastes the introduction.

### Fraud control

Self-referral, disposable accounts, and coordinated rings. Minimum viable controls: reward only on a
qualifying event well past signup, hold a payout window, deduplicate on payment method and device,
and cap per-referrer volume pending review.

### Affiliates are a different program

Affiliates are a paid channel with commercial terms, not enthusiastic customers. They need
attribution rules, cookie windows, prohibited-methods terms — brand bidding and coupon-site
behavior in particular — and monitoring.

## Pitfalls

- Launching a program where nobody refers unprompted. It buys churn.
- Paying on signup, which buys signups.
- Putting the ask in a settings page rather than after a success moment.
- Landing the referred person on the generic homepage.
- Budgeting for fraud detection after launch.
- Running affiliates without terms — you will pay commission on customers you already had.

## Verification

Track referred-customer retention against baseline. If referred customers retain worse, the
incentive is buying the wrong behavior and the program is losing money while appearing to work.

Report referrals by referrer volume as well as in aggregate — a concentration is either an advocate
worth cultivating or a fraud ring, and the difference is worth checking before paying out.

## Related

- `enterprise/revenue/retention` — the baseline referred customers are measured against.
- `enterprise/marketing/partnership-marketing` — borrowing someone else's audience instead.
- `enterprise/revenue/activation` — the qualifying event worth paying on.
