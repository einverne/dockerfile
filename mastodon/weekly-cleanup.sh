#!/bin/bash
# Weekly Mastodon cache cleanup (cron, Sunday 04:00). Added 2026-10-21.
cd /home/einverne/dockerfile/mastodon || exit 1
T="/usr/bin/docker compose exec -T web bin/tootctl"
echo "$(date '+%F %T') start"
for args in "media remove --days=7" "media remove --prune-profiles --days=7" "preview_cards remove --days=14"; do
  echo "== tootctl $args"
  $T $args < /dev/null 2>&1 | grep -v obsolete | tr '\r' '\n' | grep -E "Removed|Visited|removed" | tail -1
done
echo "$(date '+%F %T') done"
