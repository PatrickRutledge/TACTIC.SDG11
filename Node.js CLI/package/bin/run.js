#!/usr/bin/env -S node --no-deprecation

// eslint-disable-next-line n/shebang
import {execute} from '@oclif/core'

await execute({dir: import.meta.url})
