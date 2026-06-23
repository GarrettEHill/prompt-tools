# Mapper: Data Flow

**Class:** map

## You map

- how data moves between modules (request paths, events, DB, queues)
- read/write boundaries

## Read-only checks

- trace imports/calls from entrypoints inward
- note persistence and external IO

## Output

`data_flows` edges and module `depends_on` per map-result-schema.
