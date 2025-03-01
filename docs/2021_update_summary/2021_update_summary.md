# CS Metrics 2021 Edition

> Last updated 20 June 2021

A summary of institution rank changes (across all CS areas/venues) between the 2019 and 2021 version is [here](https://github.com/csmetrics/csmetrics.org/blob/master/docs/2021_update_summary/2021_update_report.pdf).

## Summary of main system and data changes


### 1. Paper filters for DBLP

[Current: June 2021]
* Rankings are generated using papers published from 2007 to 2020, appearing in 229 conferences and 90 journals from 6793 institutions.
* Filters for conferences: `['senior member',"what's hot", "invited", 'doctoral', 'demo', 'demonstration', 'keynote', 'student','speaker', 'tutorial', 'workshop', 'panel','competition', 'challenge']` (same as previous version.)
* Filters for journals: `['editor', 'special issue','state of the journal', 'in memory']`
(same as previous version.)

[Previous: July 2019]
* Rankings are generated using papers published from 2007 to 2018, appearing in 221 conferences and 87 journals from 6466 institutions.
* Filters for conferences: `['senior member',"what's hot", "invited", 'doctoral', 'demo', 'demonstration', 'keynote', 'student','speaker', 'tutorial', 'workshop', 'panel','competition', 'challenge']`
(Note: Short, Poster and Oral keywords are removed)
* We use the page numbers to filter short papers -- see [here](https://github.com/csmetrics/csmetrics.org/blob/master/docs/Overview.md#filtering) for more details. Among the five options, we choose 'Header + Page Num (k)' filter. The minimum page length is 4.
* Filters for journals: `['editor', 'special issue','state of the journal', 'in memory']`

### 2. Method for querying for citations

[Current: June 2021]
* We use MAG data dump (2021-02-15 version) to query paper titles.
2.87% of the papers did not match from title search.
MAG data now support multiple affiliations per author.

[Previous: July 2019]
* We use MAG data dump (2019-01-01 version) to query paper titles.
2.47% of the papers did not match from title search.

### 3. Added new venues and categories

Updated venue list: [venue_list](https://github.com/csmetrics/csmetrics.org/blob/master/app/data/venue_list.csv)

Duplicated name fixed:
* fixed the full name of [ACSAC](https://dblp.uni-trier.de/db/conf/acsac/index.html) to `Annual Computer Security Applications Conference`
(from the incorrect name `Asia-Pacific Computer Systems Architecture Conference`)

Type fixed:
* [FSE](https://dblp.uni-trier.de/db/conf/sigsoft/index.html): journal --> conference

New venues added:
* [TPLP](https://dblp.org/db/journals/tplp/): Theory and Practice of Logic Programming (journal)
* [TACL](https://dblp.org/db/journals/tacl/): Transactions of the Association for Computational Linguistics (journal)
* [PoPETs](https://dblp.uni-trier.de/db/journals/popets/): Proceedings on Privacy Enhancing Technologies (journal)

* [AsiaCCS](https://dblp.org/db/conf/asiaccs/): ACM Asia Conference on Computer and Communications Security (conference)
* [EuroS&P](https://dblp.org/db/conf/eurosp/): European Symposium on Security and Privacy, (conference)
* [ACSAC](https://dblp.org/db/conf/acsac/): Annual Computer Security Applications Conference (conference)
* [SOUPS](https://dblp.uni-trier.de/db/conf/soups/): Symposium On Usable Privacy and Security (conference)
* [WiSec](https://dblp.uni-trier.de/db/conf/wisec): Wireless Network Security (conference)
* [DSN](https://dblp.uni-trier.de/db/conf/dsn/): Dependable Systems and Networks (conference)
* [AISTATS](https://dblp.uni-trier.de/db/conf/aistats/): International Conference on Artificial Intelligence and Statistics (conference)
* [ICLR](https://dblp.uni-trier.de/db/conf): International Conference on Learning Representations (conference)

New categories added: None
